import os, time
from google.cloud import pubsub_v1
from setenv import setEnv

setEnv()
sub_id = 'SUB_DATA_RECEIVED_LOCAL'
topic_id = 'TOPIC_DATA_CALCULATED'
project_id = 'GOOGLE_CLOUD_PROJECT'

topic_name = os.getenv(topic_id)
project_name = os.getenv(project_id)

#자신이 보낼 이벤트의 publisher를 준비
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_name, topic_name)


def callback(message):
    print(message.data)
    print("message received!")

    # 메세지를 수신했음을 Pub/Sub에 알림 - 저장된 메세지가 지워짐
    message.ack()

    # 데이터를 계산하던가 하는 행동
    time.sleep(2)

    #이벤트 발생
    future = publisher.publish(topic_path, b'publish!', spam='eggs')
    future.result()


#IoT에서 보내는 이벤트를 구독
subscription_name = os.getenv(sub_id)
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_name, subscription_name)
# Subscribe to the topic and wait for messages
future = subscriber.subscribe(subscription_path, callback)



try:
    # Keeps the main thread active and prevents it from exiting
    future.result()
except KeyboardInterrupt:
    print("Stopped by user.")
    future.cancel()  # Gracefully stop the subscription if interrupted by the user