class ProductsAPI:
    def __init__(self, client):
        self.client = client

    def get_product_by_id(self, product_id):
        return self.client.get(f"/products/{product_id}")
