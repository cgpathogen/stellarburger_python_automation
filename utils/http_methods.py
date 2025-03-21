import requests


class Http_methods:
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "PostmanRuntime/7.43.2",
    }
    cookies = ""

    @staticmethod
    def get(url, token=None):
        headers = Http_methods.headers.copy()
        if token:
            headers['Authorization'] = f"{token}"
        request = requests.get(url=url, headers=headers, cookies=Http_methods.cookies)
        return request


    @staticmethod
    def post(url, json):
        request = requests.post(url=url, json=json, headers=Http_methods.headers, cookies=Http_methods.cookies)
        return request


    @staticmethod
    def put(url, json):
        request = requests.put(url=url, headers=Http_methods.headers, cookies=Http_methods.cookies, json=json)
        return request


    @staticmethod
    def delete(url, json):
        request = requests.delete(url=url, headers=Http_methods.headers, cookies=Http_methods.cookies, json=json)
        return request