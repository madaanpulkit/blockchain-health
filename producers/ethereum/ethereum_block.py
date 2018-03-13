from pykafka import KafkaClient

from config import TEST_KAFKA_BROKER
from config import ETHEREUM_ACCOUNT_GROUP, ETHEREUM_ACCOUNT_TOPIC


class KafkaEthereumBlockProducer(object):
    def __init__(self):
        self.client = KafkaClient(hosts=TEST_KAFKA_BROKER)
        self.group = ETHEREUM_ACCOUNT_GROUP
        self.topic = self.client.topics[ETHEREUM_ACCOUNT_TOPIC]
        self.producer = self.topic.get_sync_producer()
    
    def produce(self, data):
        data_in_bytes = bytes(data, 'utf-8')
        with self.producer as producer:
            producer.produce(data_in_bytes)

    def start(self):
        self.send("test")
