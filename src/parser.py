from bs4 import BeautifulSoup


def parse_file(path_name: str):
    print(f"Start parsing {path_name}")
    _Parser().run(path_name)


class _Parser:
    def run(self, path_name: str):
        with open(path_name, "r") as f:
            soup = BeautifulSoup(f, "html.parser")
            self._process_beautiful_soup(soup)

    def _process_beautiful_soup(self, soup: BeautifulSoup):
        print(soup.prettify())
        print(type(soup))


# TODO rm
def foo() -> int:
    return 1
