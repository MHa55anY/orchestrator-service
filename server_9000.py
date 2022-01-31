""" Implementation of Orchestration GRPC Server 9000"""
from concurrent import futures
import logging

import grpc
import orchestra_pb2
import orchestra_pb2_grpc
import dummy_pb2
import dummy_pb2_grpc


# Implementation of interface for service- Will return a user object(obtained from 9001)
class Metrics(orchestra_pb2_grpc.MetricsServicer):
    def GetUserByName(self, request, context):

        #run client on port 9001 - talking to server @9001 to send UserName
        def run():
            with grpc.insecure_channel('localhost:9001') as channel:
                stub = orchestra_pb2_grpc.MetricsStub(channel)
                # response = stub.GetMockUserData(dummy_pb2.User(name=request.name))
                response = stub.UserName(orchestra_pb2.User(name=request.name))
                # return response
            # x = run()
            print("from 9001(received @ 9000)\n " + str(response))
            # return orchestra_pb2.UserRes(str(response))
            return response
        # return orchestra_pb2.UserRes(nameOf="Hello %s" % (request.name))
        x = run()
        y = x
        return orchestra_pb2.UserRes(nameOf=y.nameOf,grade=y.grade,roll=y.roll,err=y.err) #to return User Object to client
        # return nil, errors.New("not implemented yet. Hassan will implement me")

#Start the server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    orchestra_pb2_grpc.add_MetricsServicer_to_server(Metrics(), server)
    server.add_insecure_port('[::]:9000')
    server.start()
    print("Server Started at 9000...")
    # run()
    server.wait_for_termination()



if __name__ == '__main__':
    logging.basicConfig()
    serve()