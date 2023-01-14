import pika
import os

import network as nn
import send_generated as snd


def callback(ch, method, properties, body):
    chat_id = body.decode("utf-8")
    gen_lyrics = nn.generate_text('<BOS>', 200)
    snd.respond(chat_id, gen_lyrics)


user_login = os.environ['LOGIN_USER']
user_pass = os.environ['LOGIN_PASS']
hostname = os.environ['RABBIT_HOST']
port = os.environ['RABBIT_PORT']

url = 'amqp://' + user_login + ':' + user_pass + '@' + hostname + ':' + port

params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='bot-network')
channel.basic_consume(queue='bot-network', auto_ack=True, on_message_callback=callback)

print("OK")
channel.start_consuming()
