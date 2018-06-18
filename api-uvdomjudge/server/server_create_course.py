#!/usr/bin/env python
# -*- coding: utf-8 -*-.

import pika
import requests
import json


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='queue_create_course')


def create_course(course):
    url="http://127.0.0.1:8001/uv-domjudge/v1/courses/"
    response = requests.post(url=url, json=course)
    
    return response.status_code


def on_request(ch, method, props, body):
    print("desde create course request")
    print(body)
    course = json.loads(body.decode('utf-8'))
    response = create_course(course)




    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)



channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='queue_create_course')

print(" [x] Awaiting RPC requests")
channel.start_consuming()




"""
{'id_course': '201701750001M01', 'code_course': '750001M', 'name_course': 'Algoritmia y Programación', 'credits_course': '4', 'professor_course': '1144049795', 'group_course': '01', 'programming_language': '1', 'period_course': '01', 'year_course': '2017', 'academic_period': '201701'}



from server.server_create_course import create_course
from server import server_create_course
"""


