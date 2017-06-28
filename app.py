import argparse
import csv
import os
import time
from ex_gdax import ex_gdax

parser = argparse.ArgumentParser()
parser.add_argument("--exchange")
args = parser.parse_args()


def run_exchange():
    if not os.path.exists('files/{}.csv'.format(args.exchange)):
        f = open('files/{}.csv'.format(args.exchange), 'w')
        writer = csv.writer(f)
        writer.writerow(['Time', 'Best price', 'Volume', 'Ask', 'Bid', 'Asks', 'Bids'])
    with open('files/{}.csv'.format(args.exchange), 'a') as f:
        writer = csv.writer(f)
        order_book = ex_gdax.get_order_book_by_id('BTC-USD')
        ticker_data = ex_gdax.get_product_ticker_by_id('BTC-USD')
        writer.writerow([ticker_data['time'], ticker_data['price'], ticker_data['volume'],
                        ticker_data['ask'], ticker_data['bid'], order_book['asks'], order_book['bids']])


while(True):
    print("CSV written")
    run_exchange()
    time.sleep(60)
