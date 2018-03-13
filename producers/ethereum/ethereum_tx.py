from kafka import KafkaProducer
from kafka.errors import KafkaError

from config import TEST_KAFKA_BROKER

producer = KafkaProducer(bootstrap_servers=[TEST_KAFKA_BROKER])

future producer.send()
