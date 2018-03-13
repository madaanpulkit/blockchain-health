from producers.ethereum.ethereum_block import KafkaEthereumAccount

if __name__ == "__main__":
  ethereum_account = KafkaEthereumAccount()
  ethereum_account.start()
