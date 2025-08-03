


export const SERVER_BASE_URL = process.env.NEXT_PUBLIC_SERVER_API_URL;

export enum HttpMethod {
    GET = 'GET',
    POST = 'POST',
    PUT = 'PUT',
    DELETE = 'DELETE'
}

export interface ApiRequest {
    method: string;
    path: string;
    body?: any;
}

export interface ApiResponse {
    status: number;
    data?: any;
    error?: string;
}

export const api = ({ method, path, body }: ApiRequest): Promise<ApiResponse> => {

    return fetch(SERVER_BASE_URL + path, {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        },
        body: body ? JSON.stringify(body) : undefined,
    }).then(response => {
        if (!response.ok) {
            return {
                status: response.status,
                error: `HTTP error! status: ${response.status}`
            }
        }
        return {
            status: response.status,
            data: response.json() // Handle no content response
        }
    }).catch(error => {
        console.error('API request failed:', error);
        throw error;
    });
}