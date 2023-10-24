import json, hashlib, os

# constants
MAIN_CONFIG_PATH = "./build-config.json"
CONFIG_HASH_LOCATION = "./server"

# generate meta
buildId = "cat"
buildDate = "the"
builtBy = "hi"

dataTemplate = {
    "buildId": buildId,
    "buildDate": buildDate,
    "builtBy": builtBy,
    "data": {}
}

# read in the main config
mainConfig = open(MAIN_CONFIG_PATH, "r")
mainData: dict = json.load(mainConfig)
mainConfig.close()

# Hashes file without taking too much memory
def hashFile(file: str):
    BUFFER_SIZE = 65536
    sha = hashlib.sha512()
    with open(file, "rb") as f:
        while True:
            data = f.read(BUFFER_SIZE)
            if not data:
                break
            sha.update(data)
        f.close()
    return sha.hexdigest()

# creates a config file
def createConfigFile(path: str, data: dict = {}, ignorePaths: list = [], createHash = True):
    configuration = dataTemplate.copy()
    configData: dict = {}

    for key in mainData.keys():
        if not ignorePaths.count(key):
            configData[key] = mainData[key]
    
    for key in data.keys():
        if not ignorePaths.count(key):
            configData[key] = data[key]

    configuration["data"] = configData

    configJson = json.dumps(configuration)

    configFile = open(path, mode="w")
    configFile.write(configJson)
    configFile.close()

    if createHash:
        hashPath = os.path.join(CONFIG_HASH_LOCATION, os.path.basename(path) + ".hash").replace("\\", "/")
        sha = hashFile(path)
        hFile = open(hashPath, "w")
        hFile.write(sha)
        hFile.close()

createConfigFile("./server/config.json")