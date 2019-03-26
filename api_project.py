import requests as r

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


while True:
    if json_data["total_jokes"] == 0:
        print("Enter another search query.")
        break
    else:
        print("There are " + str(json_data["total_jokes"]) + " jokes")
        print("Here is one: \n" +json_data["results"][0]['joke'])
        another = input("Would you like to search another?(y/n)")
        if another == "n":
            break
#print(json_data)