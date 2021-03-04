"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc

import recognizer_pb2
import recognizer_pb2_grpc


class DeseaseRecognizer(recognizer_pb2_grpc.DeseaseRecognizerServicer):
        def Recognize(self, request, context):
            print('Gotten image:')
            print(request.picture)
            # something do with a picture
            return recognizer_pb2.RecognizeResponse(
                desease='Ass desease',
            )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    recognizer_pb2_grpc.add_DeseaseRecognizerServicer_to_server(DeseaseRecognizer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('DeseaseRecognizer started')
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()