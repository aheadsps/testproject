from src.news import get_news


def main():
    """Главная функция для работы приложения"""
    articles = get_news('tesla', ['Twitter'])
    print(articles)

if __name__ == '__main__':
    main()