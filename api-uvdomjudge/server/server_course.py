#!/usr/bin/env python
# -*- coding: utf-8 -*-.
import pika
import requests


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='queue_get_course_detail')

def get_course(id_course):

    url = "http://127.0.0.1:8001/uv-domjudge/v1/courses/"+id_course

    headers = { 'content-type': "application/json",'authorization': "Token fc38c8f651af1392b04b5c7d5af652ac664217ff", }

    response = requests.get(url, headers=headers)
    print("desde get course")
    return str(response.text).encode('utf-8')


def on_request(ch, method, props, body):
    id_course = body.decode('utf-8')
    response = get_course(id_course)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='queue_get_course_detail')

print(" [x] Awaiting RPC requests")
channel.start_consuming()


"""
from server import server_courses
"""