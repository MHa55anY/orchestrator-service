from __future__ import print_function

import logging

import grpc
import dummy_pb2
import dummy_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:10000') as channel:
        stub = dummy_pb2_grpc.MetricsStub(channel)
        response = stub.GetMockUserData(dummy_pb2.User(name= input("enter user name\n")))

        print("Response Received: \n" + str(response) )


if __name__ == '__main__':
    logging.basicConfig()
    run()
