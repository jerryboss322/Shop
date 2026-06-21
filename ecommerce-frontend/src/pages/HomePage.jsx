import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'

export default function Home() {
  const [products, setProducts] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_URL}/api/v1/products`)
      .then(res => res.json())
      .then(data => {
        setProducts(data.items || data || [])
        setLoading(false)
      })
      .catch(() => setLoading(false))
  }, [])

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm sticky top-0 z-10">
        <div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 bg-primary rounded-lg flex items-center justify-center text-white font-bold">L</div>
            <span className="font-bold text-xl">Lagos Store</span>
          </div>
          <div className="flex gap-4">
            <Link to="/login" className="px-4 py-2 text-gray-700 hover:text-primary">Login</Link>
            <Link to="/register" className="px-4 py-2 bg-primary text-white rounded-lg hover:bg-green-700">Sign Up</Link>
          </div>
        </div>
      </header>

      {/* Hero */}
      <div className="bg-gradient-to-r from-primary to-green-600 text-white py-20">
        <div className="max-w-7xl mx-auto px-4 text-center">
          <h1 className="text-5xl md:text-6xl font-bold mb-4">
            Shop <span className="text-green-200">Nigeria's</span> Best
          </h1>
          <p className="text-xl opacity-90 mb-8">Authentic products, secure payments, nationwide delivery</p>
          <button className="bg-white text-primary px-8 py-3 rounded-lg font-semibold hover:bg-gray-100">
            Shop Now
          </button>
        </div>
      </div>

      {/* Categories */}
      <div className="max-w-7xl mx-auto px-4 py-12">
        <h2 className="text-2xl font-bold mb-6">Shop by Category</h2>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {['Electronics', 'Fashion', 'Home', 'Beauty'].map(cat => (
            <div key={cat} className="bg-white p-6 rounded-xl shadow-sm hover:shadow-md cursor-pointer text-center">
              <div className="w-12 h-12 bg-green-100 rounded-full mx-auto mb-3 flex items-center justify-center">
                <span className="text-primary text-xl">📦</span>
              </div>
              <p className="font-semibold">{cat}</p>
            </div>
          ))}
        </div>
      </div>

      {/* Products */}
      <div className="max-w-7xl mx-auto px-4 pb-16">
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-2xl font-bold">Featured Products</h2>
          <Link to="/products" className="text-primary font-semibold">View all →</Link>
        </div>
        
        {loading ? (
          <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-6">
            {[1,2,3,4,5,6,7,8].map(i => (
              <div key={i} className="bg-white rounded-xl shadow-sm p-4 animate-pulse">
                <div className="bg-gray-200 h-48 rounded-lg mb-4"></div>
                <div className="h-4 bg-gray-200 rounded w-3/4 mb-2"></div>
                <div className="h-4 bg-gray-200 rounded w-1/2"></div>
              </div>
            ))}
          </div>
        ) : products.length === 0 ? (
          <div className="bg-white rounded-xl p-12 text-center">
            <p className="text-gray-500 mb-4">No products yet. Add some in your admin panel.</p>
            <p className="text-sm text-gray-400">API: {import.meta.env.VITE_API_URL}</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-6">
            {products.slice(0, 8).map(product => (
              <div key={product.id} className="bg-white rounded-xl shadow-sm hover:shadow-lg transition p-4 cursor-pointer">
                <div className="bg-gray-100 h-48 rounded-lg mb-4 flex items-center justify-center">
                  {product.image_url ? (
                    <img src={product.image_url} alt={product.name} className="h-full object-cover rounded-lg" />
                  ) : (
                    <span className="text-4xl">📱</span>
                  )}
                </div>
                <h3 className="font-semibold mb-1 truncate">{product.name}</h3>
                <p className="text-gray-500 text-sm mb-2 truncate">{product.description}</p>
                <p className="text-primary font-bold text-lg">₦{product.price?.toLocaleString()}</p>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-12">
        <div className="max-w-7xl mx-auto px-4 text-center">
          <p className="mb-2">© 2025 Lagos Store. Built in Nigeria 🇳🇬</p>
          <p className="text-gray-400 text-sm">Secure payments via Paystack • Nationwide delivery</p>
        </div>
      </footer>
    </div>
  )
}