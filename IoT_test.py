import os
from google.cloud import pubsub_v1
from setenv import setEnv

setEnv()



project_id = 'GOOGLE_CLOUD_PROJECT'
topic_id = 'TOPIC_DATA_RECEIVED'
topic_name = os.getenv(topic_id)
project_name=os.getenv(project_id)


publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_name, topic_name)
future = publisher.publish(topic_path, b'Event from IoT!', spam='eggs')
future.result()