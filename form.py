import requests
from email_validate import validate

class Form:
    def __init__(self, log, passw, email=None, url=None):
        self.log = log
        self.passw = passw
        if email:
            self.email = email
        if url:
            self.url = url

    def __setattr__(self, key, value):
        # будем проверять корректность url и на этапе создания объекта
        if key == 'url' and not self.set_web_url(value):
            return None
        # Проверяем корректность email
        elif key == 'email' and not validate(email_address=value, check_smtp=False, smtp_debug=False,
                           check_format=True, check_blacklist=True, check_dns=True,
                           dns_timeout=10):   # проверки SMPT осуществлять не будем, т.к. может выдаваться неоднозначный результат
            return None
        return object.__setattr__(self, key, value)

    def set_web_url(self, url):
        headers = {
            'accept': '*/*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }
        try:
            session = requests.Session()
            return session.get(url, headers=headers).status_code == 200
        except:
            return False

# Функция для проверки и установки url
def set_url(form, url):
    form.url = url
    if not form.__dict__.get('url'):
        print('Недействительная ссылка.')

# Функция для проверки и установки email
def set_email(form, adress):
    form.email = adress
    if not form.__dict__.get('email'):
        print('Некорректная почта.')


form = Form('log', 'pass')
form2 = Form('log', 'pass', 'ovchinnikov_2@mail.ru', 'https://itproger.com/')
#print(form.set_web_url('https://itproger.com/'))  # мешается при запуске main.py, можно раскоментить - все работает






