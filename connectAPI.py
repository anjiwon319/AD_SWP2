from urllib.request import Request, urlopen
from urllib.parse import quote
import json

class ConnectAPI:
    def __init__(self):
        self.CLIENT_ID = 'dF_3eZeMCXBNFaphvayQ'

        self.CLIENT_SECRET = 'WN5BpepWkT'

    def search_book(self, query):
        request = Request('https://openapi.naver.com/v1/search/book_adv?d_isbn=' + quote(query))
        request.add_header('X-Naver-Client-Id', self.CLIENT_ID)
        request.add_header('X-Naver-Client-Secret', self.CLIENT_SECRET)
        response = urlopen(request).read().decode('utf-8')
        search_result = json.loads(response)
        return search_result

if __name__ == "__main__":
    isbn = input("barcode: ")
    ISBN = ConnectAPI()
    books = ISBN.search_book(isbn)['items']
    print(books[0]['title'], books[0]['author'], books[0]['publisher'])

