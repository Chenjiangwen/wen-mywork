interface LoginApiResponse {
    email: string
    projects: Project[]
}

interface Project {
    id: string
    name: string
    envs: string[]
}

export type { LoginApiResponse, Project }
