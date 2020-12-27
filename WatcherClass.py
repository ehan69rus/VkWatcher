import time
import datetime
import requests

class Watcher:
    def __init__(self, token, user_id) :
        self.token = token
        self.user_id = user_id

    def __check__(self) :
        response = requests.get("https://api.vk.com/method/users.get?user_id=" + self.user_id + "&fields=online&v=5.52&access_token=" + self.token)
        jsonMap = response.json()
        userInfo = jsonMap['response']
        isOnline = userInfo[0]['online']

        return isOnline

    def watch(self, interval = 60) : 
        minutes = 0

        now = datetime.datetime.now()
        fileTime = now.strftime("%d-%m-%Y %H:%M")

        f = open('log/' + fileTime + '.txt', 'w')

        while True:
            isOnline = self.__check__()

            now = datetime.datetime.now()
            nowText = now.strftime("%H:%M")

            if isOnline == True:
                minutes = minutes + 1
                text = nowText + " user is online " + "summ: " + str(minutes)

                f.write(text + '\n')
                print(text)
            else:
                if minutes != 0:
                    f.write(nowText + '\n')
                    print(nowText + " user has disconnected")
                    print()

                minutes = 0

            time.sleep(interval)


