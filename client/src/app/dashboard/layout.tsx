import styles from "./styles.module.scss"

export default function DashboardLayout({ children }: { children: React.ReactNode }) {
    return (
        <div className={styles.layout}>
            <div className={styles.subnavbar}>
                <a>Dashboard</a>
            </div>
            <main>
                {children}
            </main>
        </div>
    )
}