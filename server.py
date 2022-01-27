""" Implementation of Orchestration GRPC Server"""
from concurrent import futures
import logging

import grpc
import orchestra_pb2
import orchestra_pb2_grpc

# Implementation of interface for service- Will return a string with the name of User
class Metrics(orchestra_pb2_grpc.MetricsServicer):
    def GetUserByName(self, request, context):
        return orchestra_pb2.UserRes(nameOf="Hello %s" % (request.name))
        # return nil, errors.New("not implemented yet. Hassan will implement me")

#Start the server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    orchestra_pb2_grpc.add_MetricsServicer_to_server(Metrics(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server Started...")
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()