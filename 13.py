class MovieList:     #Цей клас створює список фільмів і надає методи для роботи з ним
    def __init__(self):
        self.movies = [] #це посилання на поточний об'єкт класу

    def add_movie(self, movie): #це метод функція всередині класу у класі MovieList. Він відповідає за додавання нового фільму до списку
        if movie not in self.movies:
            self.movies.append(movie)
            print(f'Фільм "{movie}" додано до списку.')
        else:
            print(f'Фільм "{movie}" вже є в списку.')

    def show_movies(self): #це метод в классі MovieList
        if self.movies:
            print("Список фільмів:")
            for index, movie in enumerate(self.movies, start=1):
                print(f'{index}. {movie}')
        else:
            print("Список фільмів порожній.")

    def remove_movie(self, movie):
        if movie in self.movies:
            self.movies.remove(movie)
            print(f'Фільм "{movie}" видалено зі списку.')
        else:
            print(f'Фільм "{movie}" не знайдено у списку.')


def main():
    movie_list = MovieList()

    while True:
        print("\nМеню:")
        print("1. Додати фільм")
        print("2. Показати всі фільми")
        print("3. Видалити фільм")
        print("4. Вийти")

        choice = input("Виберіть опцію (1-4): ")

        if choice == "1":
            movie = input("Введіть назву фільму: ")
            movie_list.add_movie(movie)
        elif choice == "2":
            movie_list.show_movies()
        elif choice == "3":
            movie = input("Введіть назву фільму для видалення: ")
            movie_list.remove_movie(movie)
        elif choice == "4":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()


