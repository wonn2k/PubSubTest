import os
from google.cloud import pubsub_v1


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\KKW\PycharmProjects\PubSubTest\key.json'
os.environ['GOOGLE_CLOUD_PROJECT'] = 'aqueous-impact-441809-r5'
os.environ['TOPIC_DATA_RECEIVED'] = 'data_received_IoT'


print('Hi')
print(os.getenv('GOOGLE_CLOUD_PROJECT'))
print('Hi2')
print(os.getenv('TOPIC_DATA_RECEIVED'))
print('Hi3')

publisher = pubsub_v1.PublisherClient()
topic_name = 'projects/{project_id}/topics/{topic}'.format(
    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
    topic=os.getenv('TOPIC_DATA_RECEIVED'),  # Set this to something appropriate.
)

publisher.create_topic(name=topic_name)
future = publisher.publish(topic_name, b'My first message!', spam='eggs')
future.result()