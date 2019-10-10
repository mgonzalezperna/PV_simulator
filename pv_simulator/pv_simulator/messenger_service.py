"""
Module to wrap comunication with a broker.
"""
import pika

class MessengerService:
    """
    This service provides an interface to send messages to any consumer.
    """
    def __init__(self, queue_name, broker_hostname='localhost',
                 broker_port=5672, broker_user='guest', broker_passwd='guest'):
        """ Constructor. Param queue_name is the queue routing key """
        self.broker_hostname = broker_hostname
        self.broker_port = broker_port
        self.broker_user = broker_user
        self.broker_passwd = broker_passwd
        self.queue_name = queue_name
        self.config_connection()
        self.set_queue(queue_name)

    def config_connection(self):
        """ Creates a new global_connection with a message broker. """
        credentials = pika.PlainCredentials(
            self.broker_user, self.broker_passwd)
        parameters = pika.ConnectionParameters(
            self.broker_hostname, self.broker_port, '/', credentials)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

    def set_queue(self, queue_name):
        """ Setups the broker queue and returns the channel. """
        self.channel.queue_declare(queue=queue_name)

    def send_measurement(self, measurement, queue_name=None):
        """ Method to send measurement through channel. """
        if queue_name is None:
            queue_name = self.queue_name
        self.channel.basic_publish(
            exchange='', routing_key=queue_name, body=measurement)
        print("[x] Sent message")

    def consume_measurements(self, callback, queue_name=None):
        """ Method to listen to measurement through channel.
        The callback parameter must be a function with an interface like >
        def callback(ch, method, properties, body)."""
        if queue_name is None:
            queue_name = self.queue_name
        self.channel.basic_consume(
            queue=queue_name, auto_ack=True, on_message_callback=callback)
        self.channel.start_consuming()

    def close_connection(self):
        """ Method to close gracefully the global_connection with broker. """
        self.connection.close()
