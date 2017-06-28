import argparse
from ex_gdax import ex_gdax

parser = argparse.ArgumentParser()
parser.add_argument("--exchange")
args = parser.parse_args()

if args.exchange == 'gdax':
    print(ex_gdax.get_order_book('BTC-USD'))