import json, hashlib

def hashFile(file: str):
    BUFFER_SIZE = 65536
    sha = hashlib.sha512()
    with open(file, "rb") as f:
        while True:
            data = f.read(BUFFER_SIZE)
            if not data:
                break
            sha.update(data)
    return sha.hexdigest()

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

serverHash = hashFile("./server/config.json")

serverHashFile = open("./server/config.json.hash", mode="w")
serverHashFile.write(serverHash)
serverHashFile.close()

print(serverHash)


print(serverData, dataTemplate)


clientConfig = open("./client/config.json", mode="w")

print(data)



clientConfig.close()