# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from saturn_sync_protocol.v1 import grpc_controller_pb2 as saturn__sync__protocol_dot_v1_dot_grpc__controller__pb2


class GRPCControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Shutdown = channel.unary_unary(
                '/saturn_sync_protocol.v1.GRPCController/Shutdown',
                request_serializer=saturn__sync__protocol_dot_v1_dot_grpc__controller__pb2.Empty.SerializeToString,
                response_deserializer=saturn__sync__protocol_dot_v1_dot_grpc__controller__pb2.Empty.FromString,
                )


class GRPCControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Shutdown(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GRPCControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Shutdown': grpc.unary_unary_rpc_method_handler(
                    servicer.Shutdown,
                    request_deserializer=saturn__sync__protocol_dot_v1_dot_grpc__controller__pb2.Empty.FromString,
                    response_serializer=saturn__sync__protocol_dot_v1_dot_grpc__controller__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'saturn_sync_protocol.v1.GRPCController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GRPCController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Shutdown(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/saturn_sync_protocol.v1.GRPCController/Shutdown',
            saturn__sync__protocol_dot_v1_dot_grpc__controller__pb2.Empty.SerializeToString,
            saturn__sync__protocol_dot_v1_dot_grpc__controller__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
