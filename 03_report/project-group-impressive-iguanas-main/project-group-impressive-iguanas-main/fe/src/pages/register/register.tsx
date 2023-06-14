import { Button, Form, Input } from 'antd'
import config from '../../config'
import api from '../../api/apiBase'
import styles from './register.module.scss'
import React from 'react'
import { message } from 'antd'
import type { RegisterRequest } from './types'
import { selectEmail, selectToken } from '../../app/slices/user/userSlice'
import { store } from '../../app/store'
import { useNavigate } from 'react-router-dom'

const App: React.FC = () => {
    const [form] = Form.useForm()
    const [messageApi, contextHolder] = message.useMessage()
    const navigate = useNavigate()
    const onFinish = async (values: RegisterRequest) => {
        try{
            const result: any = await api.post(
                `${config.gateway_endpoint!}/v1/users/register`,
                {
                    name: values.project,
                    email: selectEmail(store.getState())
                },
                {
                    headers: { authorization: selectToken(store.getState()) },
                }
            )
            return navigate(`/home/${result.data.projects[0].id}/production`, {state:{props: result.data}})   
        }catch(e: any){
            messageApi.open({
                type: 'error',
                content: e.toString()
            })
        }
    }

    return (
        <div className={styles.container}>
            {contextHolder}
            <Form form={form} name="register" onFinish={onFinish}>
                <Form.Item
                    name="project"
                    label="Project"
                    rules={[{ required: true }]}
                >
                    <Input />
                </Form.Item>

                <Form.Item className={styles.button}>
                    <Button type="primary" htmlType="submit">
                        Submit
                    </Button>
                </Form.Item>
            </Form>
        </div>
    )
}

export default App
