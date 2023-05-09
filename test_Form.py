'''Отчет сохранен в html-файле'''
import pytest
import form

# для начала протестируем создание объекта с 2-мя параметрами
@pytest.mark.parametrize('log, passw', [
    ('dima', '123'),
    ('vasya', 'igor'),
    ('pasha', 789)
])
@pytest.mark.add
def test_create_2params(log, passw):
    obj = form.Form(log, passw)  # создаю объект здесь, потому что хочу прогнать несколько тестов.
                                 # способ использовать оба готовых объекта в тестах я продемонстрировал дальше
                                 # (стр.43 и 57)
    assert obj.log == log and obj.passw == passw

# тестируем создание объекта с 4-мя параметрами
@pytest.mark.parametrize('log, passw, email, url, res', [
    ('dima', '123', 'ovchd1@mail.ru', 'https://itproger.com/user/', True),
    ('vasya', 'igor', 'igor@gmail.com', 'https://docs-python.ru/packages/frejmvork-pytest/', True),
    ('pasha', 789, '123', 'https://docs-python.ru/packages/modul-validate-email-python/', False) # 123 - некорректный email
])
@pytest.mark.slow  # проверка адреса и email достаточно долгая, поэтому логичнее указать другой тег slow
def test_create_4params(log, passw, email, url, res):
    obj = form.Form(log, passw, email, url)  # здесь тем более объект пришлось создавать непосредственно в функции проверки,
                                             # т.к. в моем варианте программы проверяется корректность
                                             # адреса и email в том числе при создании объекта, хотелось показать
                                             # тест с некорректными данными
    # сначала проверяем все ли атрибуты установились, затем проверяем значения атрибутов
    # для читабельности можно было бы и разделить на 2 обхода, но решил не плодить циклы,
    # а уместить в 1 генератор - и так проверка долгая из-за bs4 и email_validate
    assert all(obj.__dict__.get(i[0]) == i[1] for i in
               zip(('log', 'passw', 'email', 'url'), (log, passw, email, url))) == res

# тестируем set_web_url
@pytest.mark.parametrize('url, res', [
    ('https://itproger.com/user/', True),
    ('https://docs-python.ru/packages/frejmvork-pytest/', True),
    ('https://123', False) # некорректный url
])
@pytest.mark.slow
def test_set_web_url(url, res):
    assert form.form.set_web_url(url) == res # а вот здесь можно воспользоваться готовым объектом

# Смысла в тестировании set_url и set_email по большому счету нет, поскольку обе обращаются к __setattr__,
# а его мы уже тестировали выше. Но т.к. по идее нужно тестировать все функции, использующиеся в программе
# пропишем несколько тестов
@pytest.mark.parametrize('url, email, res', [
    ('https://itproger.com/', 'bg2@gmail.com', True),
    ('https://123', 'error', False), # некорректная эл. почта
    ('https://docs-python.ru/packages/frejmvork-pytest/', 'coder@mail.ru', True)
])
# Сделаем тест обеих функций с одним набором данных
@pytest.mark.slow
def test_set_url(url, email, res):
    form.set_url(form.form2, url)   # используем готовый объект с уже установленными атрибутами url и email
    form.set_email(form.form2, email)
    assert bool(form.form2.url == url) == res
    assert bool(form.form2.email == email) == res





