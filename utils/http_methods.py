import requests


class Http_methods:
    headers = {"Content-Type": "application/json"}
    cookies = ""

    @staticmethod
    def get(url):
        request = requests.get(url=url, headers=Http_methods.headers, cookies=Http_methods.cookies)
        return request

    @staticmethod
    def post(url, json):
        request = requests.post(url=url, headers=Http_methods.headers, cookies=Http_methods.cookies, json=json)
        return request


    @staticmethod
    def put(url, json):
        request = requests.put(url=url, headers=Http_methods.headers, cookies=Http_methods.cookies, json=json)
        return request


    @staticmethod
    def delete(url, json):
        request = requests.delete(url=url, headers=Http_methods.headers, cookies=Http_methods.cookies, json=json)
        return request