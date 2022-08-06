import time
import jwt

SECRET_KEY = 'scorhl*98f*8fr*vf8vf5'
 
 
def get_token(id, username, auth):
    ADMIN_TOKEN_EXPIRE = 14 * 24 * 60 * 60
    now = int(time.time())
    token = jwt.encode(
        headers={
            'typ': 'POI',
            'alg': 'HS256'
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
        algorithm='HS256'
    )
    return token
 
print('GetToken: \n', get_token(12, 'scorhl', 1))

def get_name(token):
    data = jwt.decode(
        jwt=token, 
        key=SECRET_KEY, 
        algorithm='HS256')
    return data
 
print('GetName: \n', get_name(get_token(12, 'scorhl', 1)))

	# public static Token create(String username) {
	# 	HashMap<String, Object> map = new HashMap<String, Object>();
	# 	map.put("username", username);
	# 	Date expire_date = new Date(System.currentTimeMillis() + 60L * 1000L * 60L * 2L); //2h
	# 	String expire_time = ToolsUtil.getDateTimeStr(expire_date, "yyyy-MM-dd HH:mm:ss");
	# 	String jwt = Jwts.builder().setClaims(map).setExpiration(expire_date).signWith(SignatureAlgorithm.HS512, SECRET)
	# 			.compact();
	# 	return new Token("Bearer%20" + jwt, username, expire_time); // jwt前面一般都会加Bearer
	# }