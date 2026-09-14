from src.web.app import app

def main():
    """
    Запуск локального веб-сервера на порту 5000
    """
    app.run(host="127.0.0.1", port=5000, debug=True)

if __name__ == "__main__":
    main()