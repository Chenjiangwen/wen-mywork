import { useEffect } from 'react'
import config from '../../config'

import styles from './login.module.scss'
import { useDispatch } from 'react-redux'
import { setToken } from '../../app/slices/user/userSlice'
import { message } from 'antd'
import { useNavigate } from 'react-router-dom'
import logo from '../../assets/logo.png'
import { userLoginApi } from './api'

const GOOGLE_LOGIN_BUTTON_ID = 'g_id_onload'
const GOOGLE_BUTTON_PROPERTIES = {
    className: 'g_id_signin',
    'data-type': 'standard',
    'data-shape': 'rectangular',
    'data-theme': 'outline',
    'data-text': 'signin_with',
    'data-size': 'large',
    'data-logo_alignment': 'left',
}

export default function Login() {
    const [messageApi, contextHolder] = message.useMessage()
    const dispatch = useDispatch()
    const navigate = useNavigate()
    useEffect(() => {
        window.google.accounts.id.initialize({
            client_id: config.client_id!,
            callback: handleCallback,
        })
        window.google.accounts.id.prompt()

        window.google.accounts.id.renderButton(
            document.getElementById(GOOGLE_LOGIN_BUTTON_ID) as HTMLElement,
            {
                type: 'standard',
                theme: 'outline',
                size: 'large',
                click_listener: onClickHandler,
            }
        )
    })

    const handleCallback = async (
        resp: google.accounts.id.CredentialResponse
    ) => {
        const result = await userLoginApi(resp)
        if (result.status === 200) {
            dispatch(
                setToken({
                    token: result.data.token,
                    tokenType: result.data.tokenType,
                    email: result.data.email
                })
            )
            if (result.data.projects && result.data.projects.length !== 0) {
                const project = result.data.projects[0]
                navigate(`/home/${project.id}/${project.envs[0]}`, {
                    state: {
                        props: result.data
                    },
                })
            } else {
                navigate('/register')
            }
        } else {
            messageApi.open({
                type: 'error',
                content: 'Something goes wrong, please try again later',
            })
        }
    }

    function onClickHandler() {}
    return (
        <div className={styles.container}>
            {contextHolder}
            <div className={styles.logo}>
                <img src={logo} alt="logo" />
            </div>
            <div className={styles.title}>Sign in with Google</div>
            <div className={styles.button}>
                <div
                    id={GOOGLE_LOGIN_BUTTON_ID}
                    data-client_id={config.client_id!}
                    data-context="signin"
                    data-ux_mode="popup"
                    data-itp_support="true"
                ></div>

                <div {...GOOGLE_BUTTON_PROPERTIES}></div>
            </div>
        </div>
    )
}
