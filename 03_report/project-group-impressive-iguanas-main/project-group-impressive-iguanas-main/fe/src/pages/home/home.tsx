import { useLocation } from 'react-router-dom'
import { Outlet } from 'react-router-dom'
import Sidebar from './sidebar/Sidebar'
import type { LoginApiResponse } from './types'
import styles from './home.module.scss'
import { useState } from 'react'

interface LocationState {
    props: LoginApiResponse
}

const Home: React.FC = () => {
    const location = useLocation()

    const { props: p } = location.state as LocationState
    // eslint-disable-next-line
    const [props, setProps] = useState<LoginApiResponse>(p)
    // TODO move the showCreateModel into the featureflag component
    // const [showCreateModal, setShowCreateModal] = useState(false);
    // TODO: useContext()
    return (
        <div className={styles.container}>
            <Sidebar response={props} />
            <div className={styles.outletContainer}>
                <Outlet />
            </div>
        </div>
    )
}

export default Home
