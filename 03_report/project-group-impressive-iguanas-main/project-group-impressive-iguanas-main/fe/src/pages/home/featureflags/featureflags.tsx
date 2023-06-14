import { useLocation, useNavigate } from 'react-router-dom'
import styles from './featureflags.module.scss'
import { useEffect, useState } from 'react'
import { Button, Form, Input, Modal, message } from 'antd'
import FeatureflagList from '../featureflagList/featureflagList'
import { createAFeatureflag, queryAProjectsEnvFeatureflag } from '../api'
import logo from '../../../assets/logo.png'
import { selectToken } from '../../../app/slices/user/userSlice'
import { store } from '../../../app/store'

interface Featureflag {
    name: string
    status: boolean
}

export default function Featureflags() {
    const location = useLocation()
    const navigate = useNavigate()
    const [currentProject, currentEnv] = location.pathname
        .split('/')
        .slice(2, 4)
    const email = location.state.props.email
    const [featureflag, setFeatureflag] = useState<string>('')
    const [messageApi, contextHolder] = message.useMessage()
    const [showCreateModal, setShowCreateModal] = useState<boolean>(false)
    const [isListLoading, setIsListLoading] = useState<boolean>(false)
    const [featureflagList, setFeatureflagList] = useState<Featureflag[]>([])
    useEffect(() => {
        setFeatureflagList([])
        setIsListLoading(true)
        const fetchFeatureflags = async () => {
            try {
                const result = await queryAProjectsEnvFeatureflag(
                    currentProject,
                    currentEnv
                )
                setFeatureflagList(result.data.featureflags)
            } catch (e) {
                console.log(e)
            } finally {
                setIsListLoading(false)
            }
        }
        fetchFeatureflags()

        if (!selectToken(store.getState())) {
            navigate('/login')
        }
    }, [currentProject, currentEnv, navigate])

    const renderModalShown = (projectID: string, env: string) => {
        const onFinish = async (value: any) => {
            messageApi.open({
                type: 'success',
                content: 'the request has been sent',
            })
            try {
                const result = await createAFeatureflag(
                    value.featureflagName,
                    projectID,
                    env
                )
                if (result.status >= 200 || result.status < 300) {
                    setTimeout(() => {
                        queryAProjectsEnvFeatureflag(
                            currentProject,
                            currentEnv
                        ).then((result) => {
                            setFeatureflagList(result.data.featureflags)
                        })
                    }, 2000)
                }
            } catch (e) {
                console.error(e)
                messageApi.open({
                    type: 'error',
                    content: 'Something goes wrong, Please try again',
                })
            }
            setShowCreateModal(false)
            setFeatureflag('')
        }
        const formatFeatureflagID = (
            featureflag: string,
            env: string,
            projectID: string
        ) => {
            return `${featureflag}:${env}:${projectID}`
        }

        const renderForm = (projectID: string, env: string) => {
            const renderFeatureflagName = (
                <Form.Item
                    label="Featureflag name"
                    name="featureflagName"
                    help="A human-friendly name for your featureflag."
                    rules={[
                        {
                            required: true,
                            message: 'Please input your featureflag name!',
                        },
                    ]}
                >
                    <Input
                        type="text"
                        placeholder="New featureflag"
                        value={featureflag}
                        onChange={(
                            event: React.ChangeEvent<HTMLInputElement>
                        ) => {
                            setFeatureflag(event.target.value)
                        }}
                    />
                </Form.Item>
            )
            const renderFeatureflagID = (
                <div className={styles.id}>
                    <span>ID</span>
                    <Input
                        type="text"
                        value={formatFeatureflagID(featureflag, env, projectID)}
                        disabled={true}
                    />
                </div>
            )
            const renderSubmitButton = (
                <div>
                    <Button
                        className={styles.saveButton}
                        size="large"
                        htmlType="submit"
                    >
                        Submit
                    </Button>

                    <Button className={styles.cancelButton} size="large">
                        Cancel
                    </Button>
                </div>
            )
            return (
                <Form layout="vertical" className="" onFinish={onFinish}>
                    {renderFeatureflagName}
                    {renderFeatureflagID}
                    {renderSubmitButton}
                </Form>
            )
        }

        return (
            <Modal
                title="Create a feature"
                open={showCreateModal}
                footer={false}
                afterClose={() => {
                    setFeatureflag('')
                }}
                onCancel={() => {
                    setShowCreateModal(!showCreateModal)
                }}
            >
                {renderForm(currentProject, currentEnv)}
            </Modal>
        )
    }

    const renderTopSection = (
        <>
            <div className={styles.logo}>
                <img src={logo} alt="logo" />
            </div>
            <div className={styles.briefAndButton}>
                <div className={styles.brief}>
                    View and manage feature flags and remote config for your
                    selected environment.
                </div>
                <div className={styles.ButtonDiv}>
                    <Button
                        className={styles.button}
                        size="large"
                        onClick={() => setShowCreateModal(true)}
                    >
                        Create Feature
                    </Button>
                    <Button
                        type="primary"
                        size="large"
                        onChange={async () => {
                            const result = await queryAProjectsEnvFeatureflag(
                                currentProject,
                                currentEnv
                            )
                            setFeatureflagList(result.data.featureflags)
                        }}
                    >
                        Refresh
                    </Button>
                </div>
            </div>
            {renderModalShown(currentProject, currentEnv)}
        </>
    )

    const renderFeatureflagList = (
        <FeatureflagList
            featureflags={featureflagList ? featureflagList : []}
            projectId={currentProject}
            env={currentEnv}
            email={email}
            isListLoading={isListLoading}
        />
    )
    return (
        <div className={styles.container}>
            {contextHolder}
            <div className={styles.topSection}>{renderTopSection}</div>
            <div className={styles.FeatureflagList}>
                {renderFeatureflagList}
            </div>
        </div>
    )
}

export type { Featureflag }
