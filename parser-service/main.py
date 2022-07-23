from src.app.app import App


def main():
    app = App('1vuCZvE1GzgPkxYAf_c1P_51jwUcWn5WBLS6j8BFb0k0', ['https://www.googleapis.com/auth/spreadsheets'])
    app.run('Test', "R01235", "https://www.cbr.ru/scripts/XML_daily.asp?", 'http://data-microservice:8002/api/v1/')


if __name__ == '__main__':
    main()
