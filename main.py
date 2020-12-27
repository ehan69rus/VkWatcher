#!/usr/bin/python3

from WatcherClass import Watcher

# Твой токен ВК
token = ""
# id пользователя
user_id = ""
# Интервал проверки (в секундах)
interval = 60

watcher = Watcher(token, user_id)
watcher.watch(interval)
