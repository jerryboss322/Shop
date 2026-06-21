import { Link } from 'react-router-dom'
import { useAuth } from '../store/authStore'

export default function Navbar() {
  const { user, logout } = useAuth()
  
  return (
    <nav className="bg-white shadow-sm border-b">
      <div className="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between">
        <Link to="/" className="flex items-center gap-2">
          <div className="w-9 h-9 bg-green-600 rounded-xl grid place-items-center text-white font-bold">L</div>
          <span className="font-bold text-lg">Lagos Store</span>
        </Link>
        <div className="flex items-center gap-4">
          {user ? (
            <>
              <span className="text-sm">Hi, {user.first_name}</span>
              <button onClick={logout} className="text-sm px-4 h-9 rounded-lg border">Logout</button>
            </>
          ) : (
            <Link to="/login" className="text-sm px-4 h-9 grid place-items-center rounded-lg bg-gray-900 text-white">Login</Link>
          )}
        </div>
      </div>
    </nav>
  )
}