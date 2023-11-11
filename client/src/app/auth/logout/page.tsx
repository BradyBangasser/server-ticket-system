import { signOut, useSession } from "next-auth/react"

export default async function Logout() {
    return (
        <div>
            <button onClick={async () => await signOut()}>Sign Out</button>
        </div>
    )
}