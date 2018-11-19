import urllib3
from bs4 import BeautifulSoup


class Data:
    def __init__(self, url='https://multiplex.ua/cinema/kherson/fabrika'):
        self.url = url
        self.page = ''
        self.title_array = []

    def get_page(self):
        http = urllib3.PoolManager()
        response = http.request('Get', self.url)
        self.page = BeautifulSoup(response.data, features='lxml')

    def get_movie_titles(self):
        title_array = []
        for movieTitle in self.page.find_all('a', attrs={'class': 'title'}):
            title_array.append(movieTitle.text)
        self.title_array = set(title_array)
        return self.print_movies()

    def print_movies(self):
        titles_string = ''
        for movie in self.title_array:
            titles_string = ', \n'.join(self.title_array)
        return titles_string
