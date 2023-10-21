import type { Metadata } from "next/types"
import "../styles/globals.scss"

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
      <body>{children}</body>
    </html>
  )
}
