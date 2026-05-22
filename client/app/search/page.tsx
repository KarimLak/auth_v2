"use client"
import { useEffect } from "react"
import { useRouter } from "next/navigation"
import { useAuth } from "../../context/AuthContext"

export default function Dashboard() {
  const { user, loading, logout } = useAuth()
  const router = useRouter()

  useEffect(() => {
    if (!loading && !user) router.push("/login")
  }, [user, loading, router])

  const handleLogout = async (): Promise<void> => {
    await logout()
    router.push("/login")
  }

  if (loading) return <p style={{ padding: 20 }}>Loading…</p>

  return (
    <div style={{ maxWidth: 400, margin: "80px auto", padding: "0 16px" }}>

       <button onClick={handleLogout} style={{ marginTop: 16 }}>
        Sign out
      </button>
    </div>
  )
}