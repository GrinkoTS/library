from model_book import books

def library():
    def print_menu():
        print('Выберите действие: ')
        print('1. Добавление книги')
        print('2. Удаление книги')
        print('3. Поиск книги')
        print('4. Отображение всех книг')
        print('5. Изменение статуса книги')
        print('6. Выход')



    def insert_book(books):
        """Функция добавления книги в библиотеку"""
        try:
            title = str(input('Введите название книги: '))
            author = str(input('Введите автора книги: '))
            year = str(input('Введите год выпуска книги: '))
            if len(title) != 0 and len(author) != 0 and len(year) != 0:
                books.add_book(title=title, author=author, year=year)
                print('Книга успешно добавлени в библиотеку!')
            else:
                print('Неккоректные данные, попробуйте еще раз')
        except:
            pass

    def delete_book(books):
        book_id = str(input('Введите номер книги из списка для удаления: '))
        try:
            if len(book_id) != 0:
                books.remove_book(book_id=book_id)
                print('Книга успешно удалена')
            else:
                raise Exception
        except:
            print('Неккоректные данные, попробуйте еще раз')
            # print_menu()

    def search_book(books):
        """Поиск книги"""
        word = str(input('Введите название/ автора / год издания: '))
        books.get_book(word=word)

    def list_of_all_books(books):
        """Функция вывода списка книг"""
        books.get_books()

    def change_status_book(books):
        """Изменение статуса книги"""
        book_id = str(input('Введите номер книги: '))
        try:
            books.check_book(book_id)
            status = str(input('Введите статус книги в формтате (В наличии / Выдана): ')).lower()

            if len(book_id) != 0 and len(status) != 0:
                books.change_status(book_id=book_id, status=status)
                print('Статус книги успешно изменен!')
            else:
                raise Exception
        except:
            print('Неккоректные данные, попробуйте еще раз')


    print('Привет! Введите пункт меню, который хотите совершить: ')
    while True:
        print_menu()
        try:
            result = int(input())
        except:
            print('Попробуй еще раз')
            result = 0
        if (result==1):
            insert_book(books)
            print('-' * 100)
        elif (result==2):
            delete_book(books)
            print('-' * 100)
        elif (result == 3):
            search_book(books)
            print('-' * 100)
        elif (result == 4):
            list_of_all_books(books)
            print('-' * 100)
        elif (result == 5):
            change_status_book(books)
            print('-' * 100)
        elif (result == 6):
            print('Спасибо! До скорых встреч)')
            break


if __name__ == "__main__":
    library()







