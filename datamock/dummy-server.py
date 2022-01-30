""" Implementation of Dummy GRPC Server"""
from concurrent import futures
import logging

import grpc
import dummy_pb2
import dummy_pb2_grpc

#Implementation of interface
class Metrics(dummy_pb2_grpc.MetricsServicer):

    def GetMockUserData(self, request, context):
        
            if (len(request.name) < 6):
                # return (dummy_pb2.Error(err = "Name too short"))
                return (dummy_pb2.UserRes(err = "Name too short!"))
            else:
                return (dummy_pb2.UserRes(nameOf = request.name, grade= len(request.name), roll= len(request.name)*10 ))

#Start the server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dummy_pb2_grpc.add_MetricsServicer_to_server(Metrics(), server)
    server.add_insecure_port('[::]:10000')
    server.start()
    print("Server Started...")
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()