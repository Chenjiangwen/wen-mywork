// import React from 'react'
// import logo from './logo.svg'
// import { Counter } from './features/counter/Counter'

import { useEffect } from 'react'
import './App.css'
import { selectToken } from './app/slices/user/userSlice'
import { store } from './app/store'
import { useNavigate } from 'react-router-dom'

function App() {
    const navigate = useNavigate()

    useEffect(() => {
        if (selectToken(store.getState()) === '') {
            navigate('/login')
        }
    })

    return <></>
}

export default App
