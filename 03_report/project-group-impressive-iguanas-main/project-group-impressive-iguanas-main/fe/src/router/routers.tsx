import { createBrowserRouter } from 'react-router-dom'

import App from '../App'
import Register from '../pages/register/register'
import Login from '../pages/login/login'
import Home from '../pages/home/home'
import Featureflags from '../pages/home/featureflags/featureflags'
const router = createBrowserRouter([
    {
        path: '/',
        element: <App />,
    },
    {
        path: '/register',
        element: <Register />,
    },
    {
        path: '/login',
        element: <Login />,
    },
    {
        path: '/home',
        element: <Home />,
        errorElement: <Login />,
        children: [
            {
                path: ":project/:env",
                element: <Featureflags />,
            }
        ],
    },

])

export default router;
