#sorry, but I was too lazy to do it properly with a json ^^'
FILE = "shower_data.txt"
users = []

def loadFile(file):
    print("not implemented yet")

def saveFile(file):
    content = ""
    for user in users:
        content += user["user"] + ":" + str(user["timesShowered"]) + "|"
    file.write(content)

def hasUser(seekedUser: str) -> dict:
    i = 0
    for user in users:
        if user["user"] == seekedUser:
            return {"boolean": True, "number": i}
        i += 1
    return {"boolean": False,"number": -1}


def showered(user) -> str:
    file = open(FILE, "w")

    if users == {}:
        loadFile(file)
    
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