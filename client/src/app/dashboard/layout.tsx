import styles from "./styles.module.scss"
import { join } from "path"

interface SubRoute {
    name: string
    route: string | SubRoute[]
}

const subNavRoutes: SubRoute[] = [{
    name: "Dashboard",
    route: "/"
},
{
    name: "invoices",
    route: [
        {
            name: "list",
            route: "/hello"
        }
    ]
}]

function createNavRoutes(initalPath: string, routes: SubRoute[]): React.ReactNode {
    return routes.map((route, index) => {
        if (Array.isArray(route.route)) {
            return (
                <div key={index} className={styles.nestedNavlink}>
                    <div className={styles.nestedRouteTitle}>
                        {route.name}
                    </div>
                    <div>
                        {createNavRoutes(join(initalPath, route.name), route.route)}
                    </div>
                </div>
            )
        } else {
            return (
                <div key={index + initalPath} className={styles.navlink}>
                    <a href={`${initalPath}${route.route}`}>{route.name}</a>
                </div>
            )
        }
    })
}

export default function DashboardLayout({ children }: { children: React.ReactNode }) {
    return (
        <div className={styles.layout}>
            <div className={styles.subnavbar}>
                {createNavRoutes("./dashboard", subNavRoutes)}   
            </div>
            <main>
                {children}
            </main>
        </div>
    )
}