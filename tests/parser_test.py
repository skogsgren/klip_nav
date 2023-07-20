import json
from klip_nav.utils import SortedClippings


clippings = SortedClippings("tests/resources/clipping_sample.txt")

with open("tests/resources/correctly_parsed_sample.json", "r") as f:
    answers = json.load(f)


def test_titles():
    assert answers["titles"] == [x for x in clippings.books.keys()]


def test_notes():
    for title in clippings.books:
        for note in clippings.books[title].notes:
            assert note.content in answers["notes"]


def test_location():
    print(clippings.books)
    for title in clippings.books:
        for note in clippings.books[title].notes:
            assert note.location in answers["loc"]


def test_time():
    for title in clippings.books:
        for note in clippings.books[title].notes:
            assert note.time in answers["time"]
