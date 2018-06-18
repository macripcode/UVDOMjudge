#!/usr/bin/env python
# -*- coding: utf-8 -*-.
import pika
import requests
import json


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='queue_create_period')


def create_period(period):
    url = "http://127.0.0.1:8001/uv-domjudge/v1/periods/"
    response = requests.post(url, json=period)

    return response.status_code


def on_request(ch, method, props, body):
    period = json.loads(body.decode('utf-8'))
    print(type(period))
    print(period)

    response = create_period(period)
    print(response)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='queue_create_period')

print(" [x] Awaiting RPC requests")
channel.start_consuming()


"""
from server import server_courses
"""