from consumers.ethereum.ethereum_block import KafkaEthereumBlockConsumer


class TestKafkaEthereumAccount:
    def test__init(self):
        test_ethereum_block = KafkaEthereumBlockConsumer()

        assert True
