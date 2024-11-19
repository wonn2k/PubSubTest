import os
from google.cloud import pubsub_v1
from setenv import setEnv

setEnv()

publisher = pubsub_v1.PublisherClient()
topic_name = 'projects/{project_id}/topics/{topic}'.format(
    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
    topic=os.getenv('TOPIC_DATA_RECEIVED'),  # Set this to something appropriate.
)


#publisher.create_topic(name=topic_name)
future = publisher.publish(topic_name, b'My first message!', spam='eggs')
future.result()