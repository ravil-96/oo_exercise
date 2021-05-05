import requests
from .repo import Repo

URL = 'https://api.github.com/users/ravil-96/repos'

def fetch_repos():
    ''' Call to API of GitHub'''
    req = requests.get(URL)
    for data in req.json():
        Repo(data)
    return data