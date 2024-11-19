import os
from google.cloud import pubsub_v1
from setenv import setEnv

setEnv()
sub_id_IoT = 'SUB_DATA_RECEIVED_DBM'
sub_id_local = 'SUB_DATA_CALCULATED_DBM'

def callback_1(message):
    print(message.data)
    print("message received from IoT!")
    #메세지를 수신했음을 Pub/Sub에 알림 - 저장된 메세지가 지워짐
    message.ack()

def callback_2(message):
    print(message.data)
    print("message received from Local!")
    #메세지를 수신했음을 Pub/Sub에 알림 - 저장된 메세지가 지워짐
    message.ack()

project_id = os.getenv('GOOGLE_CLOUD_PROJECT')

subscription_name_IoT = os.getenv(sub_id_IoT)
subscription_name_local = os.getenv(sub_id_local)
subscriber = pubsub_v1.SubscriberClient()

subscription_path_IoT = subscriber.subscription_path(project_id, subscription_name_IoT)
subscription_path_local = subscriber.subscription_path(project_id, subscription_name_local)
# Subscribe to the topic and wait for messages
future = subscriber.subscribe(subscription_path_IoT, callback_1)
future = subscriber.subscribe(subscription_path_local, callback_2)

print("Listening..")
try:
    # Keeps the main thread active and prevents it from exiting
    future.result()
except KeyboardInterrupt:
    print("Stopped by user.")
    future.cancel()  # Gracefully stop the subscription if interrupted by the user