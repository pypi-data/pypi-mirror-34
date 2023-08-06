import google

from rgpubsub import Publisher
from google.cloud import pubsub


class GoogleClientPublisher(Publisher):

    def __init__(self):
        self._publisher = pubsub.PublisherClient()

    def _create_topic(self, topic_name):
        try:
            self._publisher.create_topic(topic_name)
            return True
        except google.api_core.exceptions.GoogleAPICallError as err:
            if err.code.value != 409:
                raise err
            return False

    def _send(self, topic_name, payload, arguments):
        future = self._publisher.publish(topic_name, payload, **arguments)
        future.result()
