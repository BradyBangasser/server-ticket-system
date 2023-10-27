import path from "path"
import config from "../../config.json"

function serverURI(endPoint: string): string {
    const defaultBaseServerURL = `http://localhost:${}`
    return path.join(defaultBaseServerURL, endPoint)
}