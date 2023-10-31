import type { Metadata } from "next/types"
import "../styles/globals.scss"
import Navbar from "@/components/navbar"
import Footer from "@/components/footer"

export const metadata: Metadata = {
  title: 'Some cool name here',
  description: 'Something here',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        <Navbar />
        <div id="content">{children}</div>
        <Footer />
      </body>
    </html>
  )
}
