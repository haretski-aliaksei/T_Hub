class BasePage:
    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url

    def get_url(self, path=""):
        return f"{self.base_url}{path}"

    def open(self, path=""):
        self.page.goto(self.get_url(path))
