import requests
from timeit import default_timer as timer
from threading import Thread

def rollDice():
    url = "https://roll-dice1.p.rapidapi.com/rollDice"

    headers = {
        "X-RapidAPI-Key": "1fd50227d9msh3fa3b60f2c06f69p1b8e26jsn201fdee07872",
        "X-RapidAPI-Host": "roll-dice1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    print(response.json().get('data').get('Dice'))
    print("\n")

n = 1000

start = timer()

threads = []
for i in range(n):
    t = Thread(target=rollDice)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end = timer()
print(end - start)
f = open("resultados.txt", "a")
f.write(str(end - start))
f.write("\n")
f.close()