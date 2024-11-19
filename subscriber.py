import os
from google.cloud import pubsub_v1

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\KKW\PycharmProjects\PubSubTest\key.json'
os.environ['GOOGLE_CLOUD_PROJECT'] = 'aqueous-impact-441809-r5'
os.environ['TOPIC_DATA_RECEIVED'] = 'data_received_IoT'
os.environ['SUB_DATA_RECEIVED'] = 'data_received_IoT-sub'

topic_name = 'projects/{project_id}/topics/{topic}'.format(
    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
    topic=os.getenv('TOPIC_DATA_RECEIVED'),  # Set this to something appropriate.
)

subscription_name = 'projects/{project_id}/subscriptions/{sub}'.format(
    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
    sub=os.getenv('SUB_DATA_RECEIVED'),  # Set this to something appropriate.
)

def callback(message):
    print(message.data)
    print("message received!")
    #메세지를 수신했음을 Pub/Sub에 알림
    message.ack()

project_id = os.getenv('GOOGLE_CLOUD_PROJECT')
subscription_name = os.getenv('SUB_DATA_RECEIVED')
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_name)

# Subscribe to the topic and wait for messages
future = subscriber.subscribe(subscription_path, callback)


print("Listening for messages on {}...".format(subscription_path))
try:
    # Keeps the main thread active and prevents it from exiting
    future.result()
except KeyboardInterrupt:
    print("Stopped by user.")
    future.cancel()  # Gracefully stop the subscription if interrupted by the user