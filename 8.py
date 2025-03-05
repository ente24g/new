numbers = [1, 2, 3, 4, 5]
result = all(num > 0 for num in numbers)  # Перевіряє, чи всі числа більше 0
print(result)translations = {
    "hello": {"uk": "привіт", "ru": "привет", "ch": "問候"},
    "world": {"uk": "світ", "ru": "свет", "ch": "世界"},
    "cat": {"uk": "кіт", "ru": "кот", "ch": "貓"},
    "dog": {"uk": "собака", "ru": "сабака", "ch": "狗"},
}
def translate(word, lang):
    word = word.lower()
    if word in translations and lang in translations[word]:
        return translations[word][lang]
    else:
        return "Переклад не знайдено"

# Приклад використання
word = input("Введіть слово для перекладу: ")
language = input("Введіть код мови (uk, ru, ch): ")
print("Переклад:", translate(word, language))
