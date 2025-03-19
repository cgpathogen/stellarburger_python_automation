import requests


class Http_methods:

    headers = {"Content-Type":"application/json"}
    cookies= ""


    @staticmethod
    def get(url):
        request = requests.get()