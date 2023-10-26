import json, hashlib, os, subprocess, datetime

# constants
MAIN_CONFIG_PATH = "./build-config.json"
CONFIG_HASH_LOCATION = "./server/public"

# generate meta
buildDate = datetime.datetime.now().isoformat()
builtBy = {
    "name": subprocess.run(["git", "config", "user.name"], stdout=subprocess.PIPE)
    .stdout.strip()
    .decode(),
    "email": subprocess.run(["git", "config", "user.email"], stdout=subprocess.PIPE)
    .stdout.strip()
    .decode(),
}
buildId = hashlib.sha1((builtBy["email"] + buildDate).encode()).hexdigest()

dataTemplate = {
    "buildId": buildId,
    "buildDate": buildDate,
    "builtBy": builtBy,
    "data": {},
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
def createConfigFile(
    path: str,
    data: dict = {},
    ignorePaths: list = [],
    createHash=True,
    hashFileExtention=".hash",
    removeMeta: list = [],
):
    print(f"Gathering config data for '{path}'")
    configuration = dataTemplate.copy()
    configData: dict = {}

    for key in removeMeta:
        try:
            configuration.pop(key)
        except:
            print(f"The key '{key}' was not found in the meta data")

    for key in mainData.keys():
        if not ignorePaths.count(key):
            configData[key] = mainData[key]

    for key in data.keys():
        if not ignorePaths.count(key):
            configData[key] = data[key]

    configuration["data"] = configData

    configJson = json.dumps(configuration)

    print(f"Writing config to '{path}'")
    configFile = open(path, mode="w")
    configFile.write(configJson)
    configFile.close()

    if createHash:
        hashPath = os.path.join(
            CONFIG_HASH_LOCATION, os.path.basename(path) + hashFileExtention
        ).replace("\\", "/")
        print(f"Creating hash of '{path}' at '{hashPath}'")
        sha = hashFile(path)
        hFile = open(hashPath, "w")
        hFile.write(sha)
        hFile.close()


createConfigFile("./server/config.json")
createConfigFile(
    "./client/config.json",
    ignorePaths=["server", "builtBy"],
    hashFileExtention=".client.hash",
    removeMeta=["builtBy"],
)
