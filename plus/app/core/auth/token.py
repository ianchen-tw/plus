import json
from datetime import datetime, timedelta

from jwcrypto import jwk, jwt


class Token:
    def __init__(self, key, sign_alg, encrypt_key_alg, encrypt_alg):
        self.key = jwk.JWK(k=key, kty="oct")
        self.sign_header = {"alg": sign_alg}
        self.enc_header = {"alg": encrypt_key_alg, "enc": encrypt_alg}

    def create(self, to_encode: dict) -> str:
        # create the token and sign it
        expire = datetime.utcnow() + timedelta(minutes=15)
        expire = int(expire.timestamp())
        to_encode.update({"exp": expire})
        token = jwt.JWT(header=self.sign_header, claims=to_encode)
        token.make_signed_token(self.key)
        # further encrypt it
        token = jwt.JWT(header=self.enc_header, claims=token.serialize())
        token.make_encrypted_token(self.key)
        return token.serialize()

    def verify(self, to_verify):
        to_verify = jwt.JWT(key=self.key, jwt=to_verify)
        to_verify = jwt.JWT(key=self.key, jwt=to_verify.claims)
        claim = json.loads(to_verify.claims)
        print(claim.get("username"))
        return claim.get("username")
