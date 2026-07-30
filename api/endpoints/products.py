class ProductsAPI:
    def __init__(self, client):
        self.client = client

    def get_products(self, params=None):
        return self.client.get("/products", params=params)

    def get_product_by_id(self, product_id, params=None):
        return self.client.get(f"/products/{product_id}", params=params)

    def search_products(self, query):
        return self.client.get("/products/search", params={"q": query})
