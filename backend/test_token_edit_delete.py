import http.cookiejar, urllib.request, urllib.parse, re, sqlite3, time
BASE='http://127.0.0.1:5000'
cj=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

def get_csrf(path):
    r=opener.open(BASE+path)
    html=r.read().decode()
    m=re.search(r'name=["\']csrf_token["\'][^>]*value=["\']([^"\']+)["\']', html)
    if not m:
        print('no csrf on',path)
        return None
    return m.group(1), html

# create paste
csrf, _ = get_csrf('/new')
data={'title':'token-test','content':'hello token','public':'1','csrf_token':csrf}
req=opener.open(BASE+'/new', data=urllib.parse.urlencode(data).encode())
print('create status', req.getcode(), 'url', req.geturl())
# try to find slug from Location or from HTML
html=req.read().decode()
# sometimes redirect happened: check final URL
slug_match = re.search(r'/(\w{6,})$', req.geturl())
if slug_match:
    slug=slug_match.group(1)
else:
    m=re.search(r'href=["\']http://[^"\']+/(\w+)["\']', html)
    slug = m.group(1) if m else None
print('slug=',slug)
# open DB to read edit_token
conn=sqlite3.connect('instance/rentry.sqlite')
c=conn.cursor()
c.execute("select slug, edit_token from paste order by id desc limit 1")
row=c.fetchone()
print('db row',row)
if row:
    slug_db, token = row
    print('slug_db',slug_db,'token',token)
    slug = slug or slug_db
else:
    raise SystemExit('no paste in db')

# view with token
r=opener.open(BASE+f'/{slug}?token={token}')
html=r.read().decode()
print('view with token status', r.getcode())
print('has Edit link?', 'edit?token' in html.lower())

# delete via token link
r=opener.open(BASE+f'/{slug}/delete?token={token}')
print('delete link status', r.getcode(), 'url', r.geturl())
# check gone
try:
    r=opener.open(BASE+f'/{slug}')
    print('after delete, status', r.getcode())
    print('content length', len(r.read()))
except Exception as e:
    print('after delete, exception', e)

conn.close()
print('done')
