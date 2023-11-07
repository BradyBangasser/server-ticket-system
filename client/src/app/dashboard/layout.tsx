import styles from "./styles.module.scss"
import { join } from "path"
import { SubRoute } from "./types"
import LayoutRoute from "./layout-route"

const subNavRoutes: SubRoute[] = [{
    name: "Dashboard",
    route: "/dashboard"
},
{
    name: "invoices",
    route: "/dashboard/invoices/view"
}, {
    name: "Work Orders",
    route: [{
        name: "Create",
        route: "/dashboard/work-orders/new",
    }, {
        name: "View",
        route: "/dashboard/work-orders/"
    }]
}].sort((a, b) => a.name.localeCompare(b.name))

export default function DashboardLayout({ children }: { children: React.ReactNode }) {
    return (
        <div className={styles.layout}>
            <div className={styles.subnavbar}>
                {subNavRoutes.map((val, index) => <LayoutRoute key={index} name={val.name} route={val.route} />)}   
            </div>
            <main>
                {children}
            </main>
        </div>
    )
}