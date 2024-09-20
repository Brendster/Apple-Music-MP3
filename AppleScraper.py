from urllib.request import urlopen


class AppleScraper:

    def __init__(self, url):
        self.url = url 
        self.page = urlopen(url)


    def printHTML(self):
        html_bytes = self.page.read()
        html = html_bytes.decode("utf-8")
        self.html = html
        print(html)

    def printSongNames(self):
        self.html