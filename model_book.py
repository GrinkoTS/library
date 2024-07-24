# -*- coding: utf-8 -*-
from json import load, dump
class Book():
    """Общий класс для работы с книгами в формате JSON"""
    def __init__(self, filename='books.json'):
        self.filename = filename
        self.load()
        self.titles = [i['title'] for i in self.books.values()]
        self.last_id = int(list(self.books.keys())[-1])

    def load(self):
        """Загрузить файл с книгами"""
        try:
            with open(self.filename) as f:
                self.books = load(f)
        except FileNotFoundError:
            self.books = {}

    def save(self):
        """Сохраняет файл с книгами"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            dump(self.books, f, ensure_ascii=False, indent=4)

    def add_book(self, title, author, year):
        """Добавляет книгу в json"""
        if title not in self.titles:
            book_id = str(self.last_id + 1)
            self.books[book_id] = {'title': title, 'author': author, 'year': year, 'status': 'В наличии'}
            self.save()
        else:
            print(f'Книга с названием {title} уже существует')
            raise Exception

    def remove_book(self, book_id):
        """Удаляет книгу"""
        book_id_list = [str(id) for id in list(self.books.keys())]
        if book_id in book_id_list:
            del self.books[book_id]
            self.save()
        else:
            raise Exception

    def get_books(self):
        """Получить список всех книг"""
        for book in self.books:
            info_book = self.books.get(book)
            print(f'{book}. Книга *{info_book["title"]}*, автор - {info_book["author"]}, год издания - {info_book["year"]}, статус - {info_book["status"]}')

    def get_book(self, word):
        """Поиск книги"""
        word = str(word)
        word.strip()
        book_list = []
        for book in self.books.values():
            if word.lower() == book['title'].lower() or word.lower() == book['author'] or word.lower() == book['year']:
                book_list.append(book)
        if len(book_list) != 0:
            for book in book_list:
                print(f'Книга - {book["title"]}, автор - {book["author"]}, год издания - {book["year"]}, статус - {book["status"]}')
        else:
            print('Книга не найдена')

    def check_book(self, book_id):
        book_id_list = [str(id) for id in list(self.books.keys())]
        if book_id not in book_id_list:
            print('Книга не найдена.')
            raise Exception


    def change_status(self, book_id, status):
        if status not in ['в наличии', 'выдана']:
            print('Неверный формат статуса.')
            raise Exception

        book = self.books[book_id]
        book['status'] = status.capitalize()
        self.save()

books = Book()


