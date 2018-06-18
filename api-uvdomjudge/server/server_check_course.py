#!/usr/bin/env python
# -*- coding: utf-8 -*-.
import pika
import requests


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='queue_check_course')

def check_course(id_course):

    url = "http://127.0.0.1:8001/uv-domjudge/v1/courses/"+id_course

    response = requests.get(url)

    print("desde check course")

    return str(response.status_code).encode('utf-8')


def on_request(ch, method, props, body):
    id_course = body.decode('utf-8')

    print("Get current course")
    response = check_course(id_course)
    print(response)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='queue_check_course')

print(" [x] Awaiting RPC requests")
channel.start_consuming()


"""
from server import server_courses
"""