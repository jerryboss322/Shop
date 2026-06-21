import React from 'react';
import { Link } from 'react-router-dom';

const categories = [
  {
    name: "Electronics",
    image: "/images/categories/electronics.jpg",
    slug: "electronics",
    description: "Phones, laptops & gadgets"
  },
  {
    name: "Fashion",
    image: "/images/categories/fashion.jpg", 
    slug: "fashion",
    description: "Clothing & accessories"
  },
  {
    name: "Home",
    image: "/images/categories/home.jpg",
    slug: "home", 
    description: "Furniture & decor"
  },
  {
    name: "Beauty",
    image: "/images/categories/beauty.jpg",
    slug: "beauty",
    description: "Skincare & makeup"
  }
];

export default function HomePage() {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header - keep your existing header */}
      <header className="bg-white border-b">
        <div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 bg-emerald-600 rounded-lg flex items-center justify-center text-white font-bold">
              L
            </div>
            <span className="text-xl font-semibold">Lagos Store</span>
          </div>
          <div className="flex gap-4">
            <Link to="/login" className="px-4 py-2 text-gray-700 hover:text-gray-900">
              Login
            </Link>
            <Link to="/signup" className="px-4 py-2 bg-emerald-600 text-white rounded-lg hover:bg-emerald-700">
              Sign Up
            </Link>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-8">
        {/* Categories */}
        <section className="mb-12">
          <h2 className="text-2xl font-bold text-gray-900 mb-6">Shop by Category</h2>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            {categories.map((category) => (
              <Link
                key={category.slug}
                to={`/category/${category.slug}`}
                className="group bg-white rounded-2xl p-6 shadow-sm hover:shadow-md transition-all duration-200 border border-gray-100"
              >
                <div className="relative w-24 h-24 mx-auto mb-4">
                  <div className="w-full h-full rounded-full overflow-hidden ring-4 ring-emerald-50 group-hover:ring-emerald-100 transition-all">
                    <img
                      src={category.image}
                      alt={category.name}
                      className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-300"
                    />
                  </div>
                </div>
                <h3 className="text-center font-semibold text-gray-900 group-hover:text-emerald-600 transition-colors">
                  {category.name}
                </h3>
                <p className="text-center text-xs text-gray-500 mt-1">
                  {category.description}
                </p>
              </Link>
            ))}
          </div>
        </section>

        {/* Featured Products */}
        <section>
          <div className="flex justify-between items-center mb-6">
            <h2 className="text-2xl font-bold text-gray-900">Featured Products</h2>
            <Link to="/products" className="text-emerald-600 hover:text-emerald-700 font-medium flex items-center gap-1">
              View all
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
              </svg>
            </Link>
          </div>
          
          <div className="bg-white rounded-2xl p-12 text-center border border-gray-100">
            <div className="max-w-md mx-auto">
              <div className="w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg className="w-8 h-8 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
                </svg>
              </div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2">No products yet</h3>
              <p className="text-gray-500 mb-1">Add some in your admin panel.</p>
              <p className="text-xs text-gray-400 mt-4">
                API: http://fexcwzutmesq3mpm53zonhtk.145.241.100.20.sslip.io
              </p>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}