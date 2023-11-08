import { FirestoreAdapter } from "@auth/firebase-adapter"
import NextAuth from "next-auth"

const handler = NextAuth({
    providers: [],
    secret: process.env.SECRET,
    adapter: FirestoreAdapter()
})

export {
    handler as GET,
    handler as POST
}