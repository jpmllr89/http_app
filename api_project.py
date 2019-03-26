import requests as r
import random as rand


def run_query():
    url = "https://icanhazdadjoke.com/search"

    term = input("What topic would you like to search?  ")

    res = r.get(
        url, 
        headers={
            "Accept":"application/json",
            },
        params = {"term": term}
        )

    json_data = res.json()
    return json_data

while True:
    json_data = run_query()
    if json_data["total_jokes"] == 0:
        print("Enter another search query.")
    else:
        print("There are " + str(json_data["total_jokes"]) + " jokes")
        result_num = rand.choice(range(0, json_data["total_jokes"]))
        print("Here is one: \n" +json_data["results"][result_num]['joke'])
        another = input("Would you like to search another?(y/n)")
        if another == "n":
            break