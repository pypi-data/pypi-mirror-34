alice_scripts
=============

Простой способ создавать сложные сценарии для [Яндекс.Алисы](https://dialogs.yandex.ru/)

> Библиотека разработана сообществом и не является продуктом Яндекса

## 🚀 Быстрый старт

Эта библиотека позволяет писать многоэтапные сценарии без callback-ов и ручного хранения информации о состоянии диалога. Достаточно использовать условия и циклы:

> ```
> from alice_scripts import Skill, request, say, suggest
> skill = Skill(__name__)
> ```

```python
@skill.script
def run_script():
    yield say('Загадайте число от 1 до 100, а я его отгадаю. Готовы?')

    lo, hi = 1, 100
    while lo < hi:
        middle = (lo + hi) // 2
        yield say(f'Ваше число больше {middle}?',
                  f'Правда ли, что число больше {middle}?',
                  suggest('Да', 'Нет'))

        while not request.has_lemmas('да', 'ага', 'нет', 'не'):
            yield say('Я вас не поняла. Скажите "да" или "нет"')

        if request.has_lemmas('нет', 'не'):
            hi = middle
        else:
            lo = middle + 1

    yield say(f'Думаю, вы загадали число {lo}!', end_session=True)
```

Запустить сценарий можно как обычное [Flask](http://flask.pocoo.org/)-приложение:

    pip install alice_scripts
    FLASK_APP=hello.py flask run --with-threads
    
## Примеры

* [Примеры из документации](examples)
* [Навык &laquo;Приложение для знакомств&raquo;](https://github.com/FuryThrue/WhoIsAlice/blob/master/app.py)

## 📖 Интерфейс

### alice_scripts.Skill

Этот класс реализует WSGI-приложение и является наследником класса [flask.Flask](http://flask.pocoo.org/docs/1.0/api/#flask.Flask). Сценарий, соответствующий приложению, регистрируется с помощью декоратора `@skill.script` (см. пример выше).

Сценарий запускается отдельно для каждого уникального значения `session_id`.

### alice_scripts.say(...)

Конструкция `yield say(...)` служит для выдачи ответа на запрос и принимает три типа параметров:

- Неименованные строковые аргументы задают варианты фразы, которую нужно показать и сказать пользователю. При выполнении случайно выбирается один из вариантов:

    ```python
    yield say('Как дела?', 'Как вы?', 'Как поживаете?')
    ```

- Модификаторы (см. ниже) позволяют указать дополнительные свойства ответа. Например, модификатор `suggest` создаёт кнопки с подсказками для ответа:

    ```python
    yield say('Как дела?', suggest('Хорошо', 'Нормально', 'Не очень'))
    ```

- Именованные аргументы позволяют использовать те возможности [протокола](https://tech.yandex.ru/dialogs/alice/doc/protocol-docpage/#response), для которых нет модификаторов:

    ```python
    yield say('Здравствуйте! Это мы, хороводоведы.',
              tts='Здравствуйте! Это мы, хоров+одо в+еды.')
    ```
  
  Переданные пары &laquo;ключ-значение&raquo; будут записаны в словарь `response` в ответе навыка.

### Модификаторы

Модификаторы &mdash; это функции, возвращающие [замыкания](https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%BC%D1%8B%D0%BA%D0%B0%D0%BD%D0%B8%D0%B5_(%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5)). При этом каждое замыкание должно принимать словарь `response` из [ответа](https://tech.yandex.ru/dialogs/alice/doc/protocol-docpage/#response) навыка и добавлять туда нужные ключи.

- `alice_scripts.suggest(...)`

    Создаёт кнопки с подсказками для ответа:
    
    ```python
    yield say('Как дела?', suggest('Хорошо', 'Нормально'))
    ```
    
> Так как библиотека находится в стадии proof of concept, других модификаторов пока не реализовано. Используйте именованные параметры в конструкции `yield say(...)`.

### alice_scripts.request

Объект `request` представляет собой thread-local хранилище, содержащее информацию о последнем действии пользователя в сессии.

- С объектом `request` можно работать как со словарём, полученным из [запроса](https://tech.yandex.ru/dialogs/alice/doc/protocol-docpage/#request) к навыку:

    ```python
    original_utterance = request['request']['original_utterance'] 
    ```

- `request.command` &mdash; свойство, содержащее значение поля [command](https://tech.yandex.ru/dialogs/alice/doc/protocol-docpage/#request), из которого убраны завершающие точки.

- `request.words` &mdash; свойство, содержащее все слова (и числа), найденные в поле [command](https://tech.yandex.ru/dialogs/alice/doc/protocol-docpage/#request).

- `request.lemmas` &mdash; свойство, содержащее начальные формы слов из свойства `request.words` (полученные с помощью библиотеки [pymorphy2](http://pymorphy2.readthedocs.io/en/latest/)).

- `request.has_lemmas(...)` &mdash; метод, позволяющий проверить, были ли в запросе слова, чьи начальные формы совпадают с начальными формами указанных слов:

    ```python
    if request.has_lemmas('нет', 'не'):
        answer = 'no'
    elif request.has_lemmas('да', 'ага'):
        answer = 'yes'
    ``` 

> Так как библиотека находится в стадии proof of concept, встроенных методов проверки фразы с помощью нечёткого поиска или регулярных выражений пока не реализовано.

## Разбиение на подпрограммы

Сценарий можно (и нужно) разбивать на подпрограммы. Каждая подпрограмма *должна* вызываться с помощью оператора `yield from` и может возвращать значение с помощью оператора `return`. См. [пример](examples/guess_number_subgens.py).

## Ограничения

Хранение состояния диалога в виде состояния Python-генератора накладывает несколько ограничений:

- Навык не может быть запущен на serverless-платформе.
- При перезапуске приложения все сессии будут разорваны.
- Развёрнутое веб-приложение может работать в нескольких потоках (опция [threads](http://docs.gunicorn.org/en/stable/settings.html#threads) в gunicorn), но не может работать в нескольких процессах (опция [workers](http://docs.gunicorn.org/en/stable/settings.html#workers)).

## Автор

Copyright &copy; Александр Борзунов, 2018

The MIT License (MIT)
