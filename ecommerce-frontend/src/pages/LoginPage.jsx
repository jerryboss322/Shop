import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuth } from '../store/authStore'

export default function LoginPage() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const { login } = useAuth()
  const nav = useNavigate()
  
  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      await login(email, password)
      nav('/')
    } catch (err) {
      alert('Login failed')
    }
  }
  
  return (
    <div className="max-w-md mx-auto mt-20 px-4">
      <div className="bg-white rounded-2xl p-8 border">
        <h1 className="text-2xl font-bold mb-6">Login</h1>
        <form onSubmit={handleSubmit} className="space-y-4">
          <input type="email" placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} className="w-full h-12 px-4 rounded-xl border bg-gray-50" required />
          <input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} className="w-full h-12 px-4 rounded-xl border bg-gray-50" required />
          <button className="w-full h-12 rounded-xl bg-green-600 text-white font-medium">Login</button>
        </form>
        <p className="text-sm text-gray-600 mt-4">Demo: admin@lagosstore.ng / Admin123!</p>
      </div>
    </div>
  )
}