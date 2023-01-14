import pika
import os


def publish(chat_id):

    user_login = os.environ['LOGIN_USER']
    user_pass = os.environ['LOGIN_PASS']
    hostname = os.environ['RABBIT_HOST']
    port = os.environ['RABBIT_PORT']

    url = 'amqp://' + user_login + ':' + user_pass + '@' + hostname + ':' + port

    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='bot-network')
    channel.basic_publish(exchange='', routing_key='bot-network', body=chat_id)
    connection.close()
