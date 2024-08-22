import datetime
from bs4 import BeautifulSoup


def parse_file(path_name: str):
    print(f"Start parsing {path_name}")
    _Parser().run(path_name)


class _Parser:
    def run(self, path_name: str):
        with open(path_name, "r") as f:
            soup = BeautifulSoup(f, "html.parser")
        urls = soup.find_all("a")
        for url in urls:
            return _Url(
                url["add_date"],
                url["href"],
                url.text,
            )


class _Url:
    def __init__(
        self,
        creation_date_epoch_str: str,
        href: str,
        name: str,
    ):
        self._creation_date_epoch_str = creation_date_epoch_str
        self.href = href
        self.name = name

    @property
    def creation_date_str(self) -> str:
        creation_date_epoch = int(self._creation_date_epoch_str)
        creation_date = self._get_datetime_from_epoch_str(creation_date_epoch)
        return creation_date.strftime("%Y%m%d")

    def _get_datetime_from_epoch_str(self, epoch: int) -> datetime.date:
        return datetime.datetime.fromtimestamp(epoch)
