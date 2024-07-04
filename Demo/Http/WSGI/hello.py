def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    print(environ)
    return ['<h1>Hello, web!</h1>'.encode('utf-8'), 'hello'.encode('utf-8')]