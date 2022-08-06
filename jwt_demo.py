import time
import jwt

SECRET_KEY = 'scorhl*98f*8fr*vf8vf5'
 
 
def get_token(id, username, auth):
    ADMIN_TOKEN_EXPIRE = 14 * 24 * 60 * 60
    now = int(time.time())
    token = jwt.encode(
        headers={
            'typ': 'POI',
            'alg': 'HS512'
        },
        payload={
            'exp': now + ADMIN_TOKEN_EXPIRE,
            'iat': now,
            'data': {
                'id': id,
                'username': username,
                'auth': auth,
            }
        },
        key=SECRET_KEY,
        algorithm='HS512'
    )
    return token
 
print('GetToken: \n', get_token(12, 'scorhl', 1))

def get_name(token):
    data = jwt.decode(
        jwt=token, 
        key=SECRET_KEY, 
        algorithms='HS512')
    return data
 
print('GetName: \n', get_name(get_token(12, 'scorhl', 1)))