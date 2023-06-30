import pika, json, os, django

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
# django.setup()

# from products.models import Product

params = pika.URLParameters('amqps://coampnoh:Jkt8Grl-PClAF9AwLemu3Jl8CGAnooT8@rattlesnake.rmq.cloudamqp.com/coampnoh')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in main')
    # id = json.loads(body)
    # print(id)
    # product = Product.objects.get(id=id)
    # product.likes = product.likes + 1
    # product.save()
    # print('Product likes increased!')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)
# channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()