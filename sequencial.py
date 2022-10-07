import requests
from timeit import default_timer as timer

def rollDice():
    url = "https://roll-dice1.p.rapidapi.com/rollDice"

    headers = {
        "X-RapidAPI-Key": "1647a78bb7mshd3d0c82dcbcd838p1b6f35jsn95ddc2ae7677",
        "X-RapidAPI-Host": "roll-dice1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    print(response.json().get('data').get('Dice'))
    print("\n")

n = 1000

start = timer()
for x in range(n):
    rollDice()

end = timer()
print(end - start)
f = open("resultados.txt", "a")
f.write(str(end - start))
f.write("\n")
f.close()