import { api, ApiResponse, HttpMethod } from '@/api/basicApi';

export interface HelloWorldResponse {
    message: string;
}

export const helloWorldApi = (): Promise<HelloWorldResponse> => {
    return api({
        method: HttpMethod.GET,
        path: '/hello'
    }).then((response: ApiResponse) => {
        if (response.status >= 200 && response.status < 300) {
            return response.data;
        } else {
            throw new Error(response.error || 'Failed to fetch hello world');
        }
    }).catch((error: Error) => {
        console.error('Error in helloWorld API:', error);
        throw error;
    });
}
