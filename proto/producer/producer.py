import pika
import time

for x in range(1,3):
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('my-rabbit',
            5672,
            '/',
            credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='message')
    channel.basic_publish(exchange='',
                routing_key='message',
                body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    connection.close()
    time.sleep(10)
