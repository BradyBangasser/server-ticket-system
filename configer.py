import json, hashlib

# generate meta
buildId = "cat"
buildDate = "the"
builtBy = "hi"

# read in the main config
mainConfig = open("./build-config.json")
data: dict = json.load(mainConfig)
mainConfig.close()

dataTemplate = {
    "buildId": buildId,
    "buildDate": buildDate,
    "builtBy": builtBy,
    "data": {}
}

# configure the server
serverData = dataTemplate.copy()

for key in data.keys():
    serverData[key] = data[key]

serverJson = json.dumps(serverData)

serverConfig = open("./server/config.json", mode="w")
serverConfig.write(serverJson)
serverConfig.close()

serverHash = hashlib.sha512(open("./server/config.json").buffer)

print(serverHash)


print(serverData, dataTemplate)


clientConfig = open("./client/config.json", mode="w")

print(data)



clientConfig.close()