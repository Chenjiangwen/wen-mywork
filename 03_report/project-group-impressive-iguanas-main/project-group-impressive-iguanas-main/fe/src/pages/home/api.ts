import api from '../../api/apiBase'
import { selectToken } from '../../app/slices/user/userSlice'
import { store } from '../../app/store'
import config from '../../config'

const changeStatusOfAFeatureflag = async (
    projectId: string, 
    env: string,
    featureflagName: string,
    email: string,
    status: boolean) => {
    const result = await api.patch(
        `${config.gateway_endpoint!}/v1/featureflags/featureflag`,
        {
            projectId: projectId,
            env: env,
            featureflagName: featureflagName,
            email: email,
            status: status,
        },
        {
            headers: { authorization: selectToken(store.getState()) },
        }
    )
    return result
}

const queryAFeatureflagStatus = async (id: string) => {
    const result = await api.get(
        `${config.gateway_endpoint!}/v1/featureflags/${id}`,{
            headers: { authorization: selectToken(store.getState()) },
        }
    )
    return result
}

const queryAProjectsEnvFeatureflag = async (projectId: string, env: string) => {
    const result = await api.post(
        `${config.gateway_endpoint!}/v1/featureflags/query/${projectId}/${env}`,{},
        {
            headers: { authorization: selectToken(store.getState()) },
        }
    )
    return result
}

const deleteAFeatureflag = async (id: string) => {
    const result = await api.delete(
        `${config.gateway_endpoint!}/v1/featureflags/${id}`,{
            headers: { authorization: selectToken(store.getState()) },
        }
    )
    return result
}

const createAFeatureflag = async (name: string, projectId: string, env: string) => {
    const result = await api.post(
        `${config.gateway_endpoint!}/v1/featureflags/featureflag`,
        {
            featureflagName: name,
            projectId,
            env,
        },
        {
            headers: { authorization: selectToken(store.getState()) },
        }
    )
    return result
}

export { changeStatusOfAFeatureflag, queryAFeatureflagStatus, deleteAFeatureflag, createAFeatureflag, queryAProjectsEnvFeatureflag }
