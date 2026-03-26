import requests
from config import BASE_URL, DEFAULT_HEADERS, REQUEST_TIMEOUT, POSTS_ENDPOINT
from exceptions import NetworkError, APIResponseError, UnauthorizedError, NotFoundError, ServerError

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = DEFAULT_HEADERS
        self.timeout = REQUEST_TIMEOUT
        self.post_endpoint = POSTS_ENDPOINT

    def _send_request(self, method, endpoint, payload=None):
        url=f"{self.base_url}/{endpoint}"

        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                json=payload,
                timeout=self.timeout
            )
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Request failed! {str(e)}")

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 201:
            return response.json()
        elif response.status_code == 401:
            raise UnauthorizedError("Unauthorized Error", response.status_code)
        elif response.status_code == 400:
            raise APIResponseError("API Client Error", response.status_code)
        elif response.status_code == 404:
            raise NotFoundError("Not found Error", response.status_code)
        elif response.status_code == 500:
            raise ServerError("Server Error", response.status_code)
        else:
            raise APIResponseError("Client Error", response.status_code)

    def get_all_posts(self):
        return self._send_request("GET", self.post_endpoint)

    def get_post_by_id(self,post_id):
        return self._send_request("GET", f"{self.post_endpoint}/{post_id}")

    def create_post(self,payload):
        return self._send_request("POST", self.post_endpoint, payload)

    def update_post(self,post_id,payload):
        return self._send_request("PUT", f"{self.post_endpoint}/{post_id}",payload)