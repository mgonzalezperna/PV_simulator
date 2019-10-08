"""
Project Test Suite.
"""
import pika
from pv_emulator.src.messenger_service import MessengerService

AMQP_HOSTNAME = 'localhost'
AMQP_PORT = 5672
AMQP_USER = 'guest'
AMQP_PASSWD = 'guest'

def test_amqp_connection():
    """Broker testcheck"""
    global AMQP_HOSTNAME
    global AMQP_PORT
    global AMQP_USER
    global AMQP_PASSWD
    credentials = pika.PlainCredentials(AMQP_USER, AMQP_PASSWD)
    parameters = pika.ConnectionParameters(
        AMQP_HOSTNAME, AMQP_PORT, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    assert connection.is_open
    connection.close()

"""
MessengerService test suite
"""
def test_messenger_creates_a_global_connection():
    """Test if the MessengerService creates a new global connection"""
    connection = MessengerService("test").create_connection()
    assert isinstance(connection, pika.adapters.blocking_connection.BlockingConnection)
    # Must close connections before end method.
    connection.close()

def test_messenger_creates_a_channel():
    """Test if the MessengerService creates a new global connection"""
    service = MessengerService("test")
    connection = service.create_connection()
    channel = service.set_channel(connection, "channel_test")
    assert isinstance(channel, pika.adapters.blocking_connection.BlockingChannel)
    # Must close channel and connection before end method.
    channel.close()
    connection.close()
