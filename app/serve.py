import gunicorn
from urllib.parse import unquote_plus
import json
import cgi
import sys, traceback
import io

def app(environ, start_response):
    response_code = '200 OK'
    response = json.dumps('Hakuna Matata!').encode('utf-8')

    start_response(response_code, [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(response)))
    ])
    
    return iter([response])
