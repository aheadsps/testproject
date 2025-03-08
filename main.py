import datetime
import logging
from src.save_to_file import save_to_file
from src.news import get_news


logger = logging.getLogger("main")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/main.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def main():
    """Главная функция для работы приложения"""
    try:
        logger.info('Запрос у пользователя ключевых слов')
        query = input('Введите ключевые слова: ')
        exclude_words = input('Введите слова для фильтрации (через запятую): ').split(',')

        today = datetime.datetime.today()
        today_string = today.strftime("%Y-%m-%d")

        logger.info('Получение новостей')
        articles_list = get_news(query, exclude_words)

        logger.info('Запись новостей в файл')
        file_name = f'{today_string}_{query.replace(" ", "_")}.json'
        file_path = f'news/{file_name}'
        save_to_file(articles_list, file_path)

    except Exception as ex:
        logger.error(f'Произошла ошибка: {ex}')


if __name__ == '__main__':
    main()
