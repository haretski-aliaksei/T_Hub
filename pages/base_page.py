class BasePage:
    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url

    def open(self, path=""):
        self.page.goto(f"{self.base_url}{path}")
