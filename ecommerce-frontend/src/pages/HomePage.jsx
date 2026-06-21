import { useEffect, useState } from 'react'
import api from '../api/client'

export default function HomePage() {
  const [products, setProducts] = useState([])
  
  useEffect(() => {
    api.get('/products').then(res => setProducts(res.data))
  }, [])
  
  return (
    <div className="max-w-7xl mx-auto px-4 py-12">
      <div className="text-center mb-12">
        <h1 className="text-5xl font-bold mb-4">Shop <span className="text-green-600">Nigeria's</span> Best</h1>
        <p className="text-gray-600">Authentic products, secure payments, nationwide delivery</p>
      </div>
      
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {products.map(p => (
          <div key={p.id} className="bg-white rounded-2xl p-4 border">
            <img src={p.image_url} alt={p.name} className="w-full aspect-square object-cover rounded-xl mb-3" />
            <h3 className="font-medium">{p.name}</h3>
            <p className="text-green-600 font-bold">₦{p.price.toLocaleString()}</p>
          </div>
        ))}
      </div>
    </div>
  )
}