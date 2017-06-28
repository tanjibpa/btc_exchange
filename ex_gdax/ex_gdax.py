import gdax
public_client = gdax.PublicClient()


def get_order_book_by_id(product_id):
    data = public_client.get_product_order_book(product_id, level=1)
    return {'asks': data['asks'][0],
            'bids': data['bids'][0]}


def get_product_ticker_by_id(product_id):
    data = public_client.get_product_ticker(product_id=product_id)
    return {'time': data['time'],
            'price': data['price'],
            'volume': data['volume'],
            'ask': data['ask'],
            'bid': data['bid']}
