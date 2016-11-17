def wsgi_app (environ, start_response): 

	status = '200 ok'
	headers = [ ('Content-Type', 'text/plain')]
	body = environ['QUERY_STRING'].replace('&','\n')
	start_response (status, headers)
	return [ body ]