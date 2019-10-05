"""
Module to wrap comunication with a broker.
"""
import pika


class MessengerService:
    """
    This service provides an interface to send messages to any consumer.
    """
    broker_hostname = 'localhost'
    broker_port = 5672
    broker_user = 'guest'
    broker_passwd = 'guest'
    global_connection = None
    channel = None

    def create_connection(self):
        """ Creates a new global_connection with a message broker. """
        credentials = pika.PlainCredentials(
            self.broker_user, self.broker_passwd)
        parameters = pika.ConnectionParameters(
            self.broker_hostname, self.broker_port, '/', credentials)
        connection = pika.BlockingConnection(parameters)
        return connection

    def set_channel(self, connection, queue_name):
        """ Setups the broker queue and returns the channel. """
        channel = connection.channel()
        channel.queue_declare(queue=queue_name)
        return channel

    def send_measurement(self, measurement):
        """ Method to send measurement through channel. """
        self.channel.basic_publish(
            exchange='', routing_key=self.queue_name, body=measurement)
        print("[x] Sent message")

    def consume_measurements(self, callback):
        """ Method to listen to measurement through channel.
        The callback parameter must be a function with an interface like >
        def callback(ch, method, properties, body)."""
        self.channel.basic_consume(
            queue=self.queue_name, auto_ack=True, on_message_callback=callback)
        self.channel.start_consuming()

    def close_connection(self):
        """ Method to close gracefully the global_connection with broker. """
        self.global_connection.close()

    def __init__(self, queue_name=None):
        """ Constructor. Param queue_name is the queue routing key """
        if queue_name is None:
            raise Exception('Queue name is undefined.')
        self.queue_name = queue_name
        self.global_connection = self.create_connection()
        self.channel = self.set_channel(self.global_connection, queue_name)
