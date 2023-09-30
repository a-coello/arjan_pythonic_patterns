from bitcoin import BitcoinTradingBot
from ethereum import EthereumTradingBot
from trading_bot_copy import trade


def main():
    bitcoin_trader = BitcoinTradingBot()
    trade(bitcoin_trader)

    ethereum_trader = EthereumTradingBot()
    trade(ethereum_trader)


if __name__ == "__main__":
    main()
