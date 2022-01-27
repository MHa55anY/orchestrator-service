from __future__ import print_function

import logging

import grpc
import orchestra_pb2
import orchestra_pb2_grpc


# Start the client stub- will send a user defined name and predifined grade and roll
def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = orchestra_pb2_grpc.MetricsStub(channel)
        response = stub.GetUserByName(orchestra_pb2.User(name=input('enter dummy name\n'),grade="12", roll=34))

    print("Client received: " + response.nameOf)


if __name__ == '__main__':
    logging.basicConfig()
    run()