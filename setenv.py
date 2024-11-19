import os

def setEnv():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\KKW\PycharmProjects\PubSubTest\key.json'
    os.environ['GOOGLE_CLOUD_PROJECT'] = 'aqueous-impact-441809-r5'

    os.environ['TOPIC_DATA_RECEIVED'] = 'data_received_IoT'
    os.environ['SUB_DATA_RECEIVED_LOCAL'] = 'data_received_IoT_local'
    os.environ['SUB_DATA_RECEIVED_DBM'] = 'data_received_IoT_dbm'

    os.environ['TOPIC_DATA_CALCULATED'] = 'data_calculated_local'
    os.environ['SUB_DATA_CALCULATED_DBM'] = 'data_calculated_local_dbm'

