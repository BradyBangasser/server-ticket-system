"use client";

import { SubRoute } from "./types";
import styles from "./styles.module.scss"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faChevronRight } from "@fortawesome/free-solid-svg-icons";
import React, { useState } from "react"

export default function LayoutRoute({ name, route }: {
    name: string
    route: string | SubRoute[]
}): JSX.Element {
    const [selected, setSelected] = useState(false)
    if (Array.isArray(route)) {
        return (
            <div className={`${styles.nestedNavlink} ${selected ? styles.selectedDropdown : ""}`} onClick={() => setSelected(!selected)}>
                <div className={styles.nestedRouteTitle}>
                    <div className={styles.dropsign}>
                        <FontAwesomeIcon icon={faChevronRight} rotate={90} />
                    </div>
                    <div className={`${styles.droptitle} ${styles.routeLink}`}>{name}</div>
                </div>
                <div className={styles.dropdown}>
                    {route.map((subroute, index) => <RouteLink key={index} href={subroute.route.toString()}>{subroute.name}</RouteLink>)}
                </div>
            </div>
        )
    } else {
        return (
            <div className={styles.navlink}>
                <RouteLink href={route}>{name}</RouteLink>
            </div>
        )
    }
}

function RouteLink({
    href,
    children
}: {
    href: string
    children: any
}) {
    return <div className={styles.routeLink}><a href={href}>{children}</a></div>
}