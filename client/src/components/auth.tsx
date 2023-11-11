"use client"

import { useSession } from "next-auth/react"
import DefaultLoadingComponent from "./defaultLoading"
import { useRouter } from "next/router"

/**
 * Creates auth barrier
 * @param enabled boolean or minimum user role
 * @warning This Component and it's children will be rendered on the client side
*/
function Auth({ children, enabled = true, redirect = "/auth/login", loadingComponent = <DefaultLoadingComponent /> } : { children: React.ReactElement, enabled?: boolean | string, redirect?: string, loadingComponent?: JSX.Element }) {

    if (loadingComponent === <DefaultLoadingComponent />) console.warn("Default loading component not implmented yet")
    
    const router = useRouter()
    const { data: session, status } = useSession({
        required: !!enabled,
        onUnauthenticated() {
            const url = new URL(router.query.redirect?.toString() ?? redirect)
            url.searchParams.set("redirect", router.asPath)
            router.replace(url)
        },
    })

    if (status === "loading") return loadingComponent
    if (status === "unauthenticated" && !enabled) return children

    // TODO: CHECK ROLES
    console.warn("role checking not implemented")
    return children
}

export default Auth