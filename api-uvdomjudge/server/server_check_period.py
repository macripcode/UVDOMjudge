#!/usr/bin/env python
# -*- coding: utf-8 -*-.
import pika
import requests


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='queue_check_period')

def check_period(id_period):

    url = "http://127.0.0.1:8001/uv-domjudge/v1/periods/"+id_period

    response = requests.get(url)

    print("desde check period")

    return str(response.status_code).encode('utf-8')


def on_request(ch, method, props, body):
    id_period = body.decode('utf-8')

    print("Get Current period")
    response = check_period(id_period)
    print(response)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='queue_check_period')

print(" [x] Awaiting RPC requests")
channel.start_consuming()


"""
from server import server_courses
"""