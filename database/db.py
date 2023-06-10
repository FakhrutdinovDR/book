from dataclasses import dataclass
import os

@dataclass()
class User:
    userid: int
    bookmarks: set
    lastpage: int = 1

def writeupdateusers(usersdict: dict): # Обновление инфы о юзерах
    with open('baseusers.pkl', 'wb') as file:
        pickle.dump(usersdict, file)

def loadusersindict(): # Загрузка базы юзеров
    usersdict = {}
    if os.path.exists('baseusers.pkl'):
        with open('baseusers.pkl', 'rb') as file:
            data = pickle.load(file)
            for key, value in data.items():
                usersdict.setdefault(key, value)
    return usersdict
