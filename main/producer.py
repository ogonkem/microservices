import pika, json

params = pika.URLParameters('amqps://coampnoh:Jkt8Grl-PClAF9AwLemu3Jl8CGAnooT8@rattlesnake.rmq.cloudamqp.com/coampnoh')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
