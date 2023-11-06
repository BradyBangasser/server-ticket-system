import styles from "./styles.module.scss"
import { join } from "path"
import { SubRoute } from "./types"
import LayoutRoute from "./layout-route"

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
        }, {
            name: "test",
            route: "/hello"
        }
    ]
}, {
    name: "Work Orders",
    route: "/work-orders"
}]

export default function DashboardLayout({ children }: { children: React.ReactNode }) {
    return (
        <div className={styles.layout}>
            <div className={styles.subnavbar}>
                {subNavRoutes.map((val, index) => <div key={index}>{<LayoutRoute name={val.name} route={val.route} />}</div>)}   
            </div>
            <main>
                {children}
            </main>
        </div>
    )
}