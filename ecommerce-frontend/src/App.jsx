import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Login from './pages/LoginPage'
import Register from './pages/Register'
import Home from './pages/HomePage'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
