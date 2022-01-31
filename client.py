"""Implementation of Client"""

from __future__ import print_function

import logging

import grpc
import orchestra_pb2
import orchestra_pb2_grpc


# Start the client stub- will send the name of user to server @ 9000
def run():
    with grpc.insecure_channel('localhost:9000') as channel:
        stub = orchestra_pb2_grpc.MetricsStub(channel)
        response = stub.GetUserByName(orchestra_pb2.User(name=input('enter dummy name\n')))

    print("Client received from 9000<--9001<--10000: \n" + str(response))



if __name__ == '__main__':
    logging.basicConfig()
    run()