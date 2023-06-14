interface LoginResponse {
    email: string
    projects: Project[]
    token: string
    tokenType: string
}

interface Project {
    envs: string[]
    id: string
    name: string
}

export type {LoginResponse, Project}