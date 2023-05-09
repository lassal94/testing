'''Написал для демонстрации использования класса Form'''

from form import Form, set_url, set_email

dec1 = input('Желаете указать почту и адрес эл. почты? (да/нет): ')
while dec1 not in ('да', 'нет'):
    dec1 = input('Повторите: ')

if dec1 == 'нет':
    form = Form('lassal', 'pass')
else:
    dec2 = input('Укажем до создания объекта, или позже? (1 - сразу, 2 - позже) ')
    while dec2 not in ('1', '2'):
        dec2 = input('Повторите: ')
    # Проверяем и устанавливаем на этапе создания объекта
    if dec2 == '1':
        url, email = input('Введите url: '), input('Введите email: ')
        form2 = Form('lassal', 'pass', email, url)
        while not form2.__dict__.get('url') or not form2.__dict__.get('email'):
            print('Указанные url или email некорректны!')
            url, email = input('Введите url: '), input('Введите email: ')
            form2 = Form('lassal', 'pass', email, url)
        print(f'\nУстановленный email {form2.email} корректен')
        print(f'Установленный url {form2.url} корректен')
    # Проверяем и устанавливаем после создания объекта
    else:
        form3 = Form('lassal', 'pass')
        while not form3.__dict__.get('email'):
            email = input('Введите адрес эл. почты: ')
            set_email(form3, email)   # вывел установку атрибутов email и url в отдельные функции вне класса Form
        while not form3.__dict__.get('url'):
            url = input('Введите url: ')
            set_url(form3, url)   # вывел установку атрибутов email и url в отдельные функции вне класса Form
        print(f'\nУстановленный email {form3.email} корректен')
        print(f'Установленный url {form3.url} корректен')