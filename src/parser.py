import bs4
from bs4 import BeautifulSoup


def parse_file(path_name: str):
    print(f"Start parsing {path_name}")
    _Parser().run(path_name)


class _Parser:
    def run(self, path_name: str):
        with open(path_name, "r") as f:
            soup = BeautifulSoup(f, "html.parser")
        bookmarks_toolbar_dt: bs4.element.Tag = soup.dl.p.dt
        #print(bookmarks_toolbar_dt)
        #print(type(bookmarks_toolbar_dt))
        inmediate_folders = bookmarks_toolbar_dt.dl.p.find_all('dt', recursive=False)
        for folder in inmediate_folders:
            print('----------------')
            print(folder)
            # TODO why only 1 folder is detected and not 2?
