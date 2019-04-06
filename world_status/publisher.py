from world_status.log import log
from zmq import PUSH, Context


class Publisher:
    protocol = "tcp"

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.uri = "{}://{}:{}".format(self.protocol, self.host, self.port)
        self.context = Context()
        self.client = self.context.socket(PUSH)
        self.client.connect(self.uri)

    def publish(self, data, message_type):
        self.client.send_json({
            "message_type": message_type,
            "data": data
        })
