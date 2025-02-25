import json
from typing import Optional, List

import pydantic

class Book(pydantic.BaseModel):
    title: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]
    author2: Optional[str]


def main() -> None:
    with open("/home/urthilak/ws/idea/py-play/data/data.json") as file:
        print("test")
        data = json.load(file)
        books: List[Book] = [Book(**item) for item in data]
        print(books[0])
        print(books[0].author)


if __name__ == "__main__":
    main()
