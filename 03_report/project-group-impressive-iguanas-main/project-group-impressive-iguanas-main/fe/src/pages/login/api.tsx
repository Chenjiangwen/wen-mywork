import api from '../../api/apiBase'
import { LoginResponse } from './types'
import config from '../../config'



const userLoginApi = async (resp: google.accounts.id.CredentialResponse) => await api.post<LoginResponse,any>(`${config.gateway_endpoint}/v1/users/login`, {
    idToken: resp.credential,
})

export {userLoginApi}