import os

def get_subscriber_name(topic_id, sub_id):
    topic_name = 'projects/{project_id}/topics/{topic}'.format(
        project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
        topic=os.getenv(topic_id),  # Set this to something appropriate.
    )

    subscription_name = 'projects/{project_id}/subscriptions/{sub}'.format(
        project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
        sub=os.getenv(sub_id),  # Set this to something appropriate.
    )

    return topic_name, subscription_name