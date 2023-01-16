import json

FILE = "shower_data.json"
users = []

def loadFile():
    file = open(FILE, "r")
    content = json.loads(file.read())
    file.close()
    global users
    users = content["users"]

def saveFile(file):
    content = {
        "users": users
    }
    
    file.write(json.dumps(content))

def hasUser(seekedUser: str) -> dict:
    i = 0
    for user in users:
        if user["user"] == seekedUser:
            return {"boolean": True, "number": i}
        i += 1
    return {"boolean": False,"number": -1}


def showered(user) -> str:
    if users == []:
        loadFile()
    
    file = open(FILE, "w")
    
    existingUser = hasUser(user.name)
    if existingUser["boolean"]:
        users[existingUser["number"]]["timesShowered"] += 1
        saveFile(file)
        return user.name + " showered, thats the " + str(users[existingUser["number"]]["timesShowered"]) + " time they got wet 😏"

    else:
        users.append({
            "user": user.name,
            "timesShowered": 1
        })
        saveFile(file)
        return (user.name + " has just showered for the first time...finally")

def sortFunc(e):
    return e["timesShowered"]

def countShowerings() -> int:
    n = 0
    for user in users:
        n += user["timesShowered"] 
    return n

def leaderboard() -> str:
    if users == []:
        loadFile()

    lb = users
    lb.sort(key=sortFunc, reverse=True)

    lb.pop(0)
    
    message = """
    People have gotten wet a total of {} times.
    
    1. {} with {} times 
    2. {} with {} times 
    3. {} with {} times 
    """.format(countShowerings(), lb[0]["user"], lb[0]["timesShowered"], lb[1]["user"], lb[1]["timesShowered"], lb[2]["user"], lb[2]["timesShowered"])

    return message

def rank(user) -> str:
    if users == []:
        loadFile()
    
    lb = users
    lb.sort(key=sortFunc, reverse=True)

    lb.pop(0)

    i = 0
    for u in lb:
        i += 1
        if u["user"] == user.name:
            return "{} is current ranked {} with {} times showered.".format(user.name, i, u["timesShowered"])
    return "{} is currently not on the leaderboard".format(user.name)