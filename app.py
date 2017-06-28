import argparse
import csv
import os
from ex_gdax import ex_gdax

parser = argparse.ArgumentParser()
parser.add_argument("--exchange")
args = parser.parse_args()

if not os.path.exists('files/{}.csv'.format(args.exchange)):
    f = open('{}.csv'.format(args.exchange), 'w')
    writer = csv.writer(f)
    writer.writerow(['Time', 'Best price', 'Volume', 'Asks', 'Bids'])
# else:


if args.exchange == 'gdax':
    print(ex_gdax.get_order_book('BTC-USD'))
    print(ex_gdax.get_product_ticker_by_id('BTC-USD'))