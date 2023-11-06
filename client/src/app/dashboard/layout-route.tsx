"use client";

import { SubRoute } from "./types";
import styles from "./styles.module.scss"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faChevronRight } from "@fortawesome/free-solid-svg-icons";

export default function LayoutRoute({ name, route }: {
    name: string
    route: string | SubRoute[]
}): JSX.Element {
    if (Array.isArray(route)) {
        return (
            <div className={styles.nestedNavlink}>
                <div className={styles.nestedRouteTitle}>
                    <div className={styles.dropsign}>
                        <FontAwesomeIcon icon={faChevronRight} rotate={90} />
                    </div>
                    {name}
                </div>
                <div className={styles.dropdown}>
                </div>
            </div>
        )
    } else {
        return (
            <div className={styles.navlink}>
                <a href={route as string}>{name}</a>
            </div>
        )
    }
}