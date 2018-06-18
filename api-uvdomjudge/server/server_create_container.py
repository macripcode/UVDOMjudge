#!/usr/bin/env python
import pika
import requests
import json


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='queue_create_container')


def create_container(container):
    url= 'http://127.0.0.1:8001/uv-domjudge/v1/containers/'
    response = requests.post(url, json=container)
    return response.status_code


def on_request(ch, method, props, body):
    container = json.loads(body.decode('utf-8'))
    response = create_container(container)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='queue_create_container')

print(" [x] Awaiting RPC requests")
channel.start_consuming()





"""
from server import server_create_container
from server.server_create_container import create_container


{"id_container": "0716e1589fd50534daa19064e757060bee72f16049e8e53687a7fbf6171bbe36", "name_container": "201702750017M02", "port_number_80_container": "32777", "port_number_3306_container": "32776", "base_image_container": "uv-domjudge-scilab:1.0", "address_volume_db_host_container": "/var/lib/docker/volumes/201702750017M02_backup_db/_data", "ip_address_container": "172.17.0.2", "running_container": "true", "associated_course": "201702750017M02"}


"""