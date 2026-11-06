import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import ChatWindow from './components/ChatWindow.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <ChatWindow />
  </StrictMode>,
)
