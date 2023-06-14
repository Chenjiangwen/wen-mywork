import { PayloadAction, createSlice } from '@reduxjs/toolkit'
import { RootState } from '../../store'
import type { User } from './types'

const initialState: User = {
    token: '',
    tokenType: '',
    email: '',
}

const userSlice = createSlice({
    name: 'user',
    initialState,
    reducers: {
        setToken: (state: User, action: PayloadAction<User>) => {
            state.token = action.payload.token
            state.tokenType = action.payload.tokenType
            state.email = action.payload.email
        },
        cleanToken: (state: User) => {
            state.token = ''
        },
    },
})

const { setToken, cleanToken } = userSlice.actions
const selectToken = (state: RootState) => state.user.token
const selectEmail = (state: RootState) => state.user.email

export { setToken, cleanToken, selectToken, selectEmail }
export default userSlice.reducer
