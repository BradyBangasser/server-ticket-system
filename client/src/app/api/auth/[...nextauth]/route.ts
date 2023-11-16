import { firestoreInstance } from "@/lib/firestore"
import { FirestoreAdapter } from "@auth/firebase-adapter"
import NextAuth, { User } from "next-auth"
import GoogleProvider from "next-auth/providers/google"
import config from "../../../../../config.json"

const handler = NextAuth({
    providers: [
        GoogleProvider({
            clientId: process.env.GOOGLE_AUTH_CLIENT_ID as string,
            clientSecret: process.env.GOOGLE_AUTH_CLIENT_SECRET as string,
            // async profile(profile, tokens) {
            //     console.log(profile, tokens)
            //     return {
            //         role: config.data.roles.user,
            //         id: profile.id ?? "7"
            //     } as User
            // }
        })
    ],
    secret: process.env.SECRET,
    adapter: FirestoreAdapter(firestoreInstance),
    callbacks: {
        jwt({ token }) {
            return token
        }
    }
})

export {
    handler as GET,
    handler as POST
}