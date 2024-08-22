import bs4
from bs4 import BeautifulSoup


def parse_file(path_name: str):
    print(f"Start parsing {path_name}")
    _Parser().run(path_name)


class _Parser:
    def run(self, path_name: str):
        with open(path_name, "r") as f:
            soup = BeautifulSoup(f, "html.parser")
        urls = soup.find_all('a')
        for url in urls:
            print(url)
