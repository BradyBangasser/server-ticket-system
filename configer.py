import json

# generate meta
buildId = ""
buildDate = ""
builtBy = ""

# read in the main config
mainConfig = open("./build-config.json")
data = json.load(mainConfig)
mainConfig.close()

# configure the server
serverData = {
    "meta": {

    }
}


serverConfig = open("./server/config.json", mode="w")
clientConfig = open("./client/config.json", mode="w")

print(data)


serverConfig.close()
clientConfig.close()