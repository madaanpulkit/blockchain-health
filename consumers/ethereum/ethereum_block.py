from pykafka import KafkaClient

from config import TEST_KAFKA_BROKER
from config import ETHEREUM_ACCOUNT_GROUP, ETHEREUM_ACCOUNT_TOPIC


class KafkaEthereumBlockConsumer(object):
    def __init__(self):
        self.client = KafkaClient(hosts=TEST_KAFKA_BROKER)
        self.group = ETHEREUM_ACCOUNT_GROUP
        self.topic = self.client.topics[ETHEREUM_ACCOUNT_TOPIC]
        self.consumer = self.topic.get_simple_consumer()

    def consume(self):
        for message in self.consumer:
            if message is not None:
                print(message.offset, message.value)

    def start(self):
        self.consume()
