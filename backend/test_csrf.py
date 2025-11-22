import http.cookiejar, urllib.request, urllib.parse, re, uuid

BASE = 'http://127.0.0.1:5000'

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

def get_csrf(path):
    r = opener.open(BASE + path)
    html = r.read().decode('utf-8')
    m = re.search(r'name=["\']csrf_token["\'][^>]*value=["\']([^"\']+)["\']', html)
    if not m:
        print('No csrf token found on', path)
        return None
    return m.group(1)

# Register
username = 'testuser_' + uuid.uuid4().hex[:6]
print('Trying register with', username)
csrf = get_csrf('/register')
if not csrf:
    raise SystemExit('CSRF not found on register')
post_data = {
    'username': username,
    'password': 'password123',
    'csrf_token': csrf
}
req = opener.open(BASE + '/register', data=urllib.parse.urlencode(post_data).encode())
print('Register response:', req.getcode())
text = req.read().decode('utf-8')
if 'Akun dibuat' in text or req.geturl().endswith('/login'):
    print('Register seems ok')
else:
    print('Register response page length', len(text))

# Login
csrf = get_csrf('/login')
post_data = {'username': username, 'password': 'password123', 'csrf_token': csrf}
req = opener.open(BASE + '/login', data=urllib.parse.urlencode(post_data).encode())
print('Login response:', req.getcode(), '->', req.geturl())

# Create new paste
csrf = get_csrf('/new')
post_data = {'title': 'script test', 'content': 'hello', 'public': '1', 'csrf_token': csrf}
req = opener.open(BASE + '/new', data=urllib.parse.urlencode(post_data).encode())
print('New paste response:', req.getcode(), '->', req.geturl())
print('Done')
