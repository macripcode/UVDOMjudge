#!/usr/bin/env python
import pika
import requests


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='get_image_detail')

def get_image(id_image):
    url = "http://127.0.0.1:8001/uv-domjudge/v1/images/"+id_image
    response = requests.get(url)
    return response.text


def on_request(ch, method, props, body):
    id_image = str(body.decode("utf-8"))
    response = (get_image(id_image)).encode('utf-8')
    print(response)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='get_image_detail')

print(" [x] Awaiting RPC requests")
channel.start_consuming()


"""
from server import server_image

"""