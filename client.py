from __future__ import print_function
import logging

import grpc

import recognizer_pb2
import recognizer_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = recognizer_pb2_grpc.DeseaseRecognizerStub(channel)
        response = stub.Recognize(recognizer_pb2.RecognizeRequest(picture=b"KHARTOV ZHOPA")) #? Convert image to array of bytes
        print("DeseaseRecognizer client received: " + response.desease)


if __name__ == '__main__':
    logging.basicConfig()
    run()