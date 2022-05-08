import requests
import json


class NsoRestconf:

    def __init__(self, protocol='http', ip='127.0.0.1', port=8080, user='admin', password='admin'):
        self.auth = (user, password)
        self.url = f'{protocol}://{ip}:{port}/restconf/data/'

    def get(self, path):
        headers = {'Accept': 'application/yang-data+json'}
        url = self.url + path
        resp = requests.get(url=url, headers=headers,
                            auth=self.auth, verify=False)
        return resp

    def post(self, path, payload):
        headers = {'Accept': 'application/yang-data+json',
                   'Content-Type': 'application/yang-data+json'}
        url = self.url + path
        with open(payload) as f:
            data = json.load(f)
        resp = requests.post(url=url, headers=headers, data=json.dumps(
            data), auth=self.auth, verify=False)
        return resp

    def put(self, path, payload):
        headers = {'Accept': 'application/yang-data+json',
                   'Content-Type': 'application/yang-data+json'}
        url = self.url + path
        with open(payload) as f:
            data = json.load(f)
        resp = requests.put(url=url, headers=headers, data=json.dumps(
            data), auth=self.auth, verify=False)
        return resp

    def patch(self, path, payload):
        headers = {'Accept': 'application/yang-data+json',
                   'Content-Type': 'application/yang-data+json'}
        url = self.url + path
        with open(payload) as f:
            data = json.load(f)
        resp = requests.patch(url=url, headers=headers, data=json.dumps(
            data), auth=self.auth, verify=False)
        return resp

    def delete(self, path):
        headers = {'Accept': 'application/yang-data+json'}
        url = self.url + path
        resp = requests.delete(url=url, headers=headers,
                               auth=self.auth, verify=False)
        return resp
