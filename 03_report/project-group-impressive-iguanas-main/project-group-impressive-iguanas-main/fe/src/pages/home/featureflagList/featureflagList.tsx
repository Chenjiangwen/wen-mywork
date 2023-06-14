import { useEffect, useState } from 'react'
import { List, Switch, Button, message, Input } from 'antd'
import { ReloadOutlined, DeleteOutlined } from '@ant-design/icons'
import { CheckOutlined, CloseOutlined, RocketOutlined } from '@ant-design/icons'
import {
    changeStatusOfAFeatureflag,
    deleteAFeatureflag,
    queryAFeatureflagStatus,
} from '../api'
import type { Featureflag } from '../featureflags/featureflags'
import styles from './featureflagList.module.scss'

interface Props {
    featureflags: Featureflag[]
    projectId: string
    env: string
    email: string
    isListLoading: boolean
}

interface PopulateFeatureflag {
    id: string
    name: string
    status: boolean
    isLoading: boolean
}

type PaginationPosition = 'top' | 'bottom' | 'both'

type PaginationAlign = 'start' | 'center' | 'end'

const calculatePopulateFeatureflags = (featureflags: Featureflag[], env: string, projectId: string) => {
    const result = featureflags.reduce((map, item) => {
        map.set(item.name, { id: `${item.name}:${env}:${projectId}`, ...item, isLoading: false })
        return map
    }, new Map<string, PopulateFeatureflag>())
    return result
}

const App = (props: Props) => {
    const { featureflags, isListLoading } = props
    const position: PaginationPosition = 'bottom'
    const align: PaginationAlign = 'center'
    const pageSize = 10

    const [searchText, setSearchText] = useState<string>('')
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    const [messageApi, contextHolder] = message.useMessage()
    const [populateFeatureflags, setPopulatedFeatureflags] = useState<
        Map<string, PopulateFeatureflag>
    >(new Map())

    useEffect(() => {
        setPopulatedFeatureflags(calculatePopulateFeatureflags(featureflags, props.env, props.projectId))
    }, [featureflags, props.env, props.projectId])

    const filterFeatureFlags = (
        featureFlags: Map<string, PopulateFeatureflag>,
        searchText: string
    ) => {
        if (searchText === '') {
            return Array.from(featureFlags.values())
        }
        const result: PopulateFeatureflag[] = []
        featureFlags.forEach((featureflag, key) => {
            if (featureflag.name.indexOf(searchText) >= 0) {
                result.push(featureflag)
            }
        });
        return result
    }

    const renderSearchSection = (
        <div className={styles.searchContainer}>
            <div className={styles.title}>
                <RocketOutlined className={styles.icon} />
                Features
            </div>
            <Input.Search
                className={styles.searchInput}
                placeholder="Search a feature flag"
                allowClear
                onChange={(e) => setSearchText(e.target.value)}
            />
        </div>
    )

    const reSetPopulatedFeatureflagsLoading = ({
        p,
        name,
    }: {
        p: Map<string, PopulateFeatureflag>
        name: string
    }) => {
        p.get(name)!.isLoading = !p.get(name)!.isLoading;
        setPopulatedFeatureflags(new Map(p));
    }

    const reSetPopulatedFeatureflagsCheckedAndLoading = ({
        p,
        name,
        checked,
    }: {
        p: Map<string, PopulateFeatureflag>
        name: string
        checked: boolean
    }) => {
        const featureflag = p.get(name)!;
        featureflag.status = checked;
        featureflag.isLoading = !featureflag.isLoading;
        setPopulatedFeatureflags(new Map(p));
    };

    const reSetPopulatedFeatureflagsChecked = ({
        p,
        name,
        checked,
    }: {
        p: Map<string, PopulateFeatureflag>
        name: string
        checked: boolean
    }) => {
        p.get(name)!.status = checked
        setPopulatedFeatureflags(new Map(p));
    };

    const removeAFeatureflagFromPopulatedFeatureflags = (name: string) => {
        populateFeatureflags.delete(name);
        setPopulatedFeatureflags(new Map(populateFeatureflags));
    }

    const renderListItem = (item: PopulateFeatureflag) => {
        const renderSwitch = (
            <Switch
                key="toggle"
                checkedChildren={<CheckOutlined />}
                unCheckedChildren={<CloseOutlined />}
                loading={item.isLoading}
                checked={item.status}
                onChange={async (checked: boolean) => {
                    reSetPopulatedFeatureflagsCheckedAndLoading({
                        p: populateFeatureflags,
                        name: item.id.split(":")[0],
                        checked,
                    })
                    try {

                        await changeStatusOfAFeatureflag(
                            `${props.projectId}`,
                            `${props.env}`,
                            item.name,
                            `${props.email}`,
                            item.status)
                        reSetPopulatedFeatureflagsLoading({
                            p: populateFeatureflags,
                            name: item.id.split(":")[0],
                        })
                    } catch (e) {
                        messageApi.open({
                            type: 'error',
                            content: 'Something goes wrong, please try again 3',
                        })
                        reSetPopulatedFeatureflagsCheckedAndLoading({
                            p: populateFeatureflags,
                            name: item.id.split(":")[0],
                            checked: !checked,
                        })
                    }
                }}
            />
        )
        const renderRefresh = (
            <Button
                key="refresh"
                icon={<ReloadOutlined />}
                loading={item.isLoading}
                onClick={async () => {
                    reSetPopulatedFeatureflagsLoading({
                        p: populateFeatureflags,
                        name: item.id.split(":")[0],
                    })
                    try {
                        const result = await queryAFeatureflagStatus(item.id)
                        reSetPopulatedFeatureflagsChecked({
                            p: populateFeatureflags,
                            name: item.id.split(":")[0],
                            checked: result.data.status,
                        })
                    } catch (e) {
                        console.error(e)
                        messageApi.open({
                            type: 'error',
                            content: 'Something goes wrong, please try again 2 ',
                        })

                    } finally {
                        reSetPopulatedFeatureflagsLoading({
                            p: populateFeatureflags,
                            name: item.id.split(":")[0],
                        })
                    }
                }}
            />
        )
        const renderDelete = (
            <Button
                key="delete"
                icon={<DeleteOutlined />}
                loading={item.isLoading}
                onClick={async () => {
                    reSetPopulatedFeatureflagsLoading({
                        p: populateFeatureflags,
                        name: item.id.split(":")[0],
                    })
                    try {
                        await deleteAFeatureflag(item.id)
                        removeAFeatureflagFromPopulatedFeatureflags(item.id.split(":")[0])
                    } catch (e) {
                        messageApi.open({
                            type: 'error',
                            content: 'Something goes wrong, please try again 1',
                        })
                        reSetPopulatedFeatureflagsLoading({
                            p: populateFeatureflags,
                            name: item.id.split(":")[0],
                        })
                    }
                }}
            />
        )
        return (
            <List.Item className={styles.lists}>
                <div>
                    <div className={styles.featureName}>
                        {item.name}
                    </div>
                    <div className={styles.featureId}>
                        {`${item.name}:${props.env}:${props.projectId}`}
                    </div>
                </div>
                <div className={styles.buttons}>
                    {renderSwitch}
                    {renderRefresh}
                    {renderDelete}
                </div>
            </List.Item>
        )
    }

    return (
        <>
            {contextHolder}
            <List
                header={renderSearchSection}
                bordered
                pagination={{ position, align, pageSize }}
                dataSource={filterFeatureFlags(
                    populateFeatureflags,
                    searchText
                )}
                renderItem={renderListItem}
                loading={isListLoading}
            />
        </>
    )
}

export default App
