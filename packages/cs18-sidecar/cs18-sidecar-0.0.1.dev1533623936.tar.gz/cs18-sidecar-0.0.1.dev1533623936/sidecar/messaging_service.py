import uuid
import pika
from logging import Logger
from jsonpickle import json


class MessagingConnectionProperties:
    def __init__(self, host: str,
                 user: str,
                 password: str,
                 queue: str,
                 exchange: str,
                 routingkey: str,
                 virtualhost: str,
                 port: int,
                 queuetype: str,
                 expires,
                 usessl: bool):
        self.host = host
        self.user = user
        self.password = password
        self.queue = queue
        self.exchange = exchange
        self.routingkey = routingkey
        self.virtualhost = virtualhost
        self.port = port
        self.queuetype = queuetype
        self.expires = expires
        self.usessl = usessl


class MessagingService:
    def __init__(self, connection_props: MessagingConnectionProperties, logger: Logger):
        self._connection = None
        self._logger = logger

        protocol = "amqp" if connection_props.usessl is not True else "amqps"

        url = "{protocol}://{user}:{password}@{host}/{virtual_host}?heartbeat_interval=0" \
            .format(protocol=protocol,
                    user=connection_props.user,
                    password=connection_props.password,
                    host=connection_props.host,
                    virtual_host=connection_props.virtualhost)
        self._url_params = pika.URLParameters(url=url)
        self._destination = "rabbitmq://{host}/{virtual_host}/".format(host=connection_props.host,
                                                                       virtual_host=connection_props.virtualhost)
        self.endpoint = connection_props.queue

    def publish(self, message_type: str, message):
        try:

            self._connection = pika.BlockingConnection(self._url_params)

            if self._connection is not None:
                channel = self._connection.channel()
                # arguments = {"x-expires": self._connection_props.expires}
                # channel.queue_declare(queue=self._connection_props.queue, durable=True, arguments=arguments)

                message_id = uuid.uuid1()
                payload = {
                    "messageId": str(message_id),
                    "conversationId": str(message_id),
                    "destinationAddress": self._destination + message_type,
                    "messageType": [
                        "urn:message:{}".format(message_type)
                    ],
                    "message": message,
                    "headers": {}
                }

                channel.basic_publish(exchange=self.endpoint, routing_key="", body=json.dumps(payload))

        except Exception as exc:
            self._logger.exception("an error occurred while connecting to a queue {exc}".format(exc=exc))
        finally:
            self._close_connection()
            self._connection = None

    def _close_connection(self):
        try:
            if self._connection is not None:
                self._connection.close()
        except Exception as exc:
            self._logger.exception("an error occurred while closing the RabbitMQ connection {exc}".format(exc=exc))
