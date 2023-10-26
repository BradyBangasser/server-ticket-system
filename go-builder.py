import os
from os import path

CWD = path.dirname(os.path.realpath(__file__))
ROUTES_PATH = "server/routes"
BUILD_FILE_NAME = "build"

def getFiles(file: str = "", basepath = ROUTES_PATH):
    if file.endswith(".go"):
        return file.lower().replace(".go", "")
    
    folderPath = path.join(CWD, basepath, file)
    files = [getFiles(f, folderPath) for f in os.listdir(folderPath)]

    if len(file) > 0:
        return { file: files }
    else:
        return files
    
def getImports(groups, cpath = ROUTES_PATH):
    imports = []

    pathAdded = False

    if type(groups) == dict:
        for key in groups.keys():
            imports = [*imports, *getImports(groups[key], path.join(cpath, key).replace("\\", "/"))]

    for group in groups:
        if type(group) == str and not pathAdded:
            imports.append(path.join(cpath, group).replace("\\", "/"))
            pathAdded = True
        elif type(group) == dict:
            for key in group.keys():
                imports = [*imports, *getImports(groups[key], path.join(cpath, key).replace("\\", "/"))]
    
    return imports

goFiles: list = getFiles()
goFiles.remove(BUILD_FILE_NAME)

buildImports = getImports(goFiles)

print(buildImports)

buildFileContent = [f"package {path.basename(ROUTES_PATH)}"]

# buildFile = open(path.join(CWD, ROUTES_PATH, BUILD_FILE_NAME + ".go"), "w")