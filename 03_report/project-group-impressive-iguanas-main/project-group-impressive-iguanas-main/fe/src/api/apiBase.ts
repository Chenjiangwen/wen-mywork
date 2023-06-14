import axios from 'axios'
import config from '../config'

axios.interceptors.response.use(
    function (response) {
        // Any status code that lie within the range of 2xx cause this function to trigger
        // Do something with response data
        return response.data
    },
    function (error) {
        // Any status codes that falls outside the range of 2xx cause this function to trigger
        // Do something with response error
        return Promise.reject(error)
    }
)

const instance = axios.create({
    baseURL: config.gateway_endpoint,
    // TODO
    // timeout: 1000,
})

export default instance
