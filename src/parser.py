import datetime
from collections.abc import Iterator
from bs4 import BeautifulSoup


def parse_file(path_name: str):
    print(f"Start parsing {path_name}")
    for url_parsed in _FileParser().get_urls(path_name):
        print(url_parsed)


class _Url:
    def __init__(
        self,
        creation_date_epoch_str: str,
        href: str,
        name: str,
    ):
        self._creation_date_epoch_str = creation_date_epoch_str
        self._href = href
        self._name = name

    def __repr__(self) -> str:
        return f"[{self._creation_date_str} {self._name}]({self._href})"

    @property
    def _creation_date_str(self) -> str:
        creation_date_epoch = int(self._creation_date_epoch_str)
        creation_date = self._get_datetime_from_epoch_str(creation_date_epoch)
        return creation_date.strftime("%Y%m%d")

    def _get_datetime_from_epoch_str(self, epoch: int) -> datetime.date:
        return datetime.datetime.fromtimestamp(epoch)


class _FileParser:
    def get_urls(self, path_name: str) -> Iterator[_Url]:
        with open(path_name, "r") as f:
            soup = BeautifulSoup(f, "html.parser")
        urls = soup.find_all("a")
        for url in urls:
            yield _Url(
                url["add_date"],
                url["href"],
                url.text,
            )
