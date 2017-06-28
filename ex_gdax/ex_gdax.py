import gdax
public_client = gdax.PublicClient()

def get_order_book(product_id):
    return public_client.get_product_order_book(product_id, level=1)

def get_product_ticker_by_id(product_id):
    data = public_client.get_product_ticker(product_id=product_id)
    return data['price']

# def get_