'''def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']'''

def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
	return [body.encode('utf-8')]

str = b'123'
print(str)

print(str.decode('ascii'))
print(len(str))

str2 = "abc"
print(len(str2))