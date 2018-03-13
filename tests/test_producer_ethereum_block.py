from producers.ethereum.ethereum_block import KafkaEthereumBlockProducer


class TestKafkaEthereumAccount:
    def test__init(self):
        test_ethereum_block = KafkaEthereumBlockProducer()

        assert True

    def test_produce(self):
        data = "this is a test"
        test_ethereum_block = KafkaEthereumBlockProducer()

        test_ethereum_block.produce(data)

        assert True
