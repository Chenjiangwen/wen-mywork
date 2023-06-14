import React, { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { LogoutOutlined , UserOutlined} from '@ant-design/icons'
import { Menu, Button } from 'antd'
import type { MenuProps } from 'antd/es/menu'
import styles from './Sidebar.module.scss'

import { LoginApiResponse, Project } from '../types'
import { ItemType } from 'antd/es/menu/hooks/useItems'

type MenuItem = Required<MenuProps>['items'][number]

const VERTICAL = 'vertical'
const INLINE = 'inline'
const DEFAULT_ROOT_MENU_KEY = ['']

const LogoutButton: React.FC = () => {
    const navigate = useNavigate()

    const handleLogout = async () => {
        //dispatch(tokenClean)
        // localStorage.removeItem('access_token');
        navigate('/login')
    }

    return (
        <div className={styles.logoutButton}>
            <Button icon={<LogoutOutlined />} onClick={handleLogout}>
                Log out
            </Button>
        </div>
    )
}

function getItem(
    label: React.ReactNode,
    key?: React.Key | null,
    icon?: React.ReactNode,
    children?: MenuItem[],
    onClick?: () => void
): MenuItem {
    return {
        key,
        icon,
        children,
        label,
        onClick,
    } as MenuItem
}

const getDefaultRootMenuItemAndSubMenuItem = (projects: Project[]) => {
    const getDefaultRootMenuItem = (projects: Project[]) => {
        return projects.length > 0 ? [projects[0].id] : DEFAULT_ROOT_MENU_KEY
    }
    return {
        rootMenuItem: getDefaultRootMenuItem(projects),
        subMenuItem: [`${projects[0].id}:${projects[0].envs[0]}`],
    }
}

const Sidebar: React.FC<{
    response: LoginApiResponse
}> = ({ response }) => {
    // eslint-disable-next-line
    const [loginApiResponse, setLoginApiResponse] =
        useState<LoginApiResponse>(response)

    const [mode] = useState<typeof VERTICAL | typeof INLINE>(INLINE)
    const { rootMenuItem, subMenuItem } = getDefaultRootMenuItemAndSubMenuItem(
        loginApiResponse.projects
    )
    const getMenuItems: (loginApiResponse: LoginApiResponse) => ItemType[] = (
        loginApiResponse
    ) => {
        return createMenuItems(loginApiResponse)
    }
    const createMenuItems = (loginApiResponse: LoginApiResponse) => {
        const menuItems = loginApiResponse.projects.map((project: Project) => {
            // TODO onclick
            return getItem(
                project.name,
                project.id,
                null,
                project.envs.map((env: string, key: number) => {
                    return getItem(
                        <Link
                            to={`${project.id}/${env}`}
                            state={{
                                props: response,
                            }}
                        >
                            {env}
                        </Link>,
                        `${project.id}:${env}`
                    )
                })
            )
        })
        return menuItems
    }

    const renderLeftMenu = (
        <Menu
            className={styles.menu}
            defaultOpenKeys={rootMenuItem}
            defaultSelectedKeys={subMenuItem}
            mode={mode}
            items={getMenuItems(loginApiResponse)}
        />
    )

    const renderUserInfo = (
        <div className={styles.user}>
            <div>
            <UserOutlined className={styles.icon}/>
            {loginApiResponse.email.split('@')[0]}</div>
        </div>
    )
    return (
        <div className={styles.container}>
            {renderUserInfo}
            {renderLeftMenu}
            <LogoutButton />
        </div>
    )
}

export default Sidebar

