import requests
from fastapi.responses import RedirectResponse

class OAuth2():
    def __init__(self, client_id, client_secret, auth_url, token_url, data_url, redirect_url, scope=''):
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_url = auth_url
        self.token_url = token_url
        self.data_url = data_url
        self.redirect_url = redirect_url
        self.scope = scope

    def user_auth(self):
        '''Redirect the user to third party auth page
        '''
        return RedirectResponse(self.auth_url)

    def user_data(self, code):
        '''redirect_url catch code and use it to redeem the token
        '''
        post_data = {
            'grant_type': 'authorization_code',
            'code': code,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_url
        }
        res = requests.post(self.token_url, data=post_data).json()
        print('res', res)
        self.access_token = res.get('access_token')
        return self.acquire_data()


    def acquire_data(self):
        header = {
            'Authorization': 'Bearer ' + self.access_token
        }
        res = requests.get(self.data_url, headers=header).json()
        return res
