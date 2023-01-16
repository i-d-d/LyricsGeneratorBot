<h1 align=center>
    90sRockSongsGenerator
</h1>

<h4 align=center>
    <a href=https://t.me/rock90generator_bot>Telegram-бот</a>, генерирующий (порой очень смешные) тексты песен в стиле <i>Metallica</i>, <i>Nirvana</i> и т.д.
    <br>
    <br>
</h4>

## Описание:

Бот, помимо простого поддержания разговора (ответа на приветствие, рассказа о себе), по запросу пользователя может отправлять сообщение сервису, который сгенерирует текст и отправит обратно запросившему. Сервис представляет собой обученную на текстах исполнителей нейросеть. За основу была взята нейросеть [🤗 Transformers](https://github.com/huggingface/transformers), а именно модель [GPT-2](https://huggingface.co/gpt2).

## Сервисы, входящие в проект:

 * **tgbot** - Логика самого бота, передача запросов сервису с нейросетью. Исходный код содержится в директории ``bot``.
 * **neural** - Приём запросов (полученных от бота) на генерацию, сама обученная модель и создание сессии бота для отправки сгенерированного результата. Код можно найти в директории ``network-responder``.
 * **rabbitmq** - Очередь сообщений между **tgbot** и **neural**, все данные о настройке содержатся в файле ``docker-compose.yaml`` в описании соответствующего сервиса.

## Как развернуть приложение:

Для запуска необходимо наличие *Python*, *docker* и *docker compose*.

1. **Клонировать этот репозиторий** 
```bash
$ git clone https://github.com/i-d-d/LyricsGeneratorBot
```
2. **Обучить нейросеть**. Для этого нужно в директории ``prep`` загрузить датасет текстов с помощью ``dataset_collector.py`` (список артистов можно изменить в ``artist_names.txt``, пробелы в названии заменить на дефис "-"). В результате будет создан ``song_dataset.txt`` (если уже существует, загруженные песни допишутся в конец). После этого нужно последовательно запустить ячейки в ``train.ipynb`` (процесс обучения занимает несколько часов). Полученную после обучения папку ``result`` перенести в директорию ``network-responder``.
3. **Добавить токен бота**. В ``bot`` и ``network-responer`` создать файлы ``config.py`` вида 
```python
BOT_API_TOKEN = 'your_bot_token'
```  
Создать своего бота и получить его токен можно у специального бота [*BotFather*](https://t.me/BotFather).

4. **Развернуть приложение**. Для этого нужно находясь в директории ``LyricsGeneratorBot`` выполнить в терминале следующие команды (возможно понадобится в начало добавить ``sudo``):
```bash
# Building app (can take some time)
$ docker compose build
# Starting rabbitmq service. Wait about 10 seconds after this line so RabbitMQ can start properly
$ docker compose up -d rabbitmq
# Starting neural service
$ docker compose up -d neural
# Starting tgbot service
$ docker compose up -d tgbot
# Use
# $ docker compose down
# to stop the app
```
5. **Начать диалог с ботом**

## Архитектура проекта

*Визуальное представление архитектуры нашего проекта:*
![Arch](./arch.jpg)

## Над проектом работали:

 - Сеимов М.С. (``docker`` и ``docker compose``, выбор и обучение нейросети)
 - Злобина В.В. (логика бота, настройка RabbitMQ, сбор датасета)

 <h4 align=center>
    <br>
    <i>Выполнено в рамках курсового проекта по ООП
    <br>
    МАИ, 2023</i>
</h4>