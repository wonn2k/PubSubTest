import os, datetime, json
from google.cloud import pubsub_v1
from setenv import setEnv
from FBupdater import FBupdater

setEnv()
updater = FBupdater()
sub_id_IoT = 'SUB_DATA_RECEIVED_DBM'
sub_id_local = 'SUB_DATA_CALCULATED_DBM'


def parse_json_IoT(data):
    building_id_value = data['building_id']
    id_value = int(data['store_id'])
    ewt_num = int(data['ewt_num'])
    ewt_cur = int(data['ewt_cur'])
    timestamp = data['timestamp']
    dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
    return building_id_value, id_value, ewt_num, ewt_cur, dt

def callback_from_IoT(message):
    print(message.data)
    print("message received from IoT!")
    message.ack()

    data = json.loads(message.data)
    building_id_value, id_value, ewt_num, ewt_cur, dt = parse_json_IoT(data)

    year = dt.year
    month = dt.month
    day = dt.day
    hour = dt.hour
    minute = dt.minute

    updater.update_from_IoT(building_id_value, id_value, ewt_num, ewt_cur)

    # 메세지를 수신했음을 Pub/Sub에 알림 - 저장된 메세지가 지워짐
    message.ack()

def parse_json_Local(data):
    building_id_value = data['building_id']
    id_value = int(data['store_id'])
    ewt_avg = int(data['ewt_avg'])
    return building_id_value, id_value, ewt_avg

def callback_from_Local(message):

    print(message.data)
    print("message received from IoT!")
    message.ack()
    data = json.loads(message.data)
    building_id_value, id_value, ewt_avg = parse_json_Local(data)
    updater.update_from_local(building_id_value, id_value, ewt_avg)
    #메세지를 수신했음을 Pub/Sub에 알림 - 저장된 메세지가 지워짐


project_id = os.getenv('GOOGLE_CLOUD_PROJECT')

subscription_name_IoT = os.getenv(sub_id_IoT)
subscription_name_local = os.getenv(sub_id_local)
subscriber = pubsub_v1.SubscriberClient()

subscription_path_IoT = subscriber.subscription_path(project_id, subscription_name_IoT)
subscription_path_local = subscriber.subscription_path(project_id, subscription_name_local)

# Subscribe to the topic and wait for messages
future = subscriber.subscribe(subscription_path_IoT, callback_from_IoT)
future = subscriber.subscribe(subscription_path_local, callback_from_Local)

print("Listening..")
try:
    # Keeps the main thread active and prevents it from exiting
    future.result()
except KeyboardInterrupt:
    print("Stopped by user.")
    future.cancel()  # Gracefully stop the subscription if interrupted by the user