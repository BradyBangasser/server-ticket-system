import os, re
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
    
def getImports(groups, cpath = ROUTES_PATH, r = False):
    imports = []

    pathAdded = False

    if type(groups) == dict:
        for key in groups.keys():
            imports = [*imports, *getImports(groups[key], path.join(cpath, key).replace("\\", "/"), True)]

    for group in groups:
        if type(group) == str and not pathAdded:
            importPath = path.join(cpath).replace("\\", "/")
            imports.append(f'{importPath.replace("/", "_")} "{importPath}"')
            pathAdded = True
        elif type(group) == dict:
            for key in group.keys():
                imports = [*imports, *getImports(group[key], path.join(cpath, key).replace("\\", "/"), True)]
    
    if not r:
        imports.append('"github.com/gin-gonic/gin"')

    return imports

def joiner(fc: list):
    indent = 0
    string = ""

    for line in fc:
        if re.match(r"^[\])}].*", line):
            indent -= 1
        string = string + ("\t" * indent) + line + "\n"
        if re.match(r".*[({[]$", line):
            indent += 1

    return string

def createRouter(routeList: list, initalPath = "/", parentVariable = "r", n = False):
    routerLines = []

    if not n:
        routerLines = [
            "func CreateRouter(r *gin.Engine) {"
        ]
    
    for route in routeList:
        if type(route) == dict:
           for subroute in route.keys():
                spv = f"{parentVariable}_{subroute}" # sub path parent variable
                sp = "/" + path.basename(subroute) # sub path path
                routerLines.append(f'{spv} := {parentVariable}.Group("{sp}"); ' + "{")
                routerLines += createRouter(route[subroute], sp, spv, True)
                routerLines.append("}")
        elif type(route) == str:
            importVar = f"{ROUTES_PATH}{initalPath}".replace("/", "_")
            routeMethod = route.replace('.go', '').upper()

            routerLines.append(f'{parentVariable}.{routeMethod}("/", {importVar}.{routeMethod})')
        else: print("Help")

    if not n:
        routerLines.append("}")
    
    return routerLines
           
        

goFiles: list = getFiles()
goFiles.remove(BUILD_FILE_NAME)

buildImports = getImports(goFiles)
buildRouter = createRouter(goFiles)
buildFileContent = [f"package {path.basename(ROUTES_PATH)}", "", "import (", *buildImports, ")", "", *buildRouter]

buildFile = open(path.join(CWD, ROUTES_PATH, BUILD_FILE_NAME + ".go"), "w")
buildFile.write(joiner(buildFileContent))
buildFile.close()