import textwrap
import requests

def log_requests(response, *args, **kwargs):
    def format_headers(d):
        return '\n'.join(f'{k}: {v}' for k, v in d.items())
    res = textwrap.dedent('''
        ---------------- request ----------------
        method: {req.method}
        url: {req.url}
        headers: {request_headers}
        body: {req.body}
        ---------------- response ----------------
        method: {res.status_code}
        reason: {res.reason}
        url: {res.url}
        headers: {response_headers}
    ''').format(
        req=response.request,
        res=response,
        request_headers=format_headers(response.request.headers),
        response_headers=format_headers(response.headers),
    )
    print(res)


requests.post('https://httpbin.org/',
            data={'tes': 'test'}, hooks={'response': log_requests})
