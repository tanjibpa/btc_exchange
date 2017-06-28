import gdax
public_client = gdax.PublicClient()

def get_order_book(currency, level=3):
    return public_client.get_product_order_book(currency, level=level)
