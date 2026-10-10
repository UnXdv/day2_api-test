import requests
from utils.logger import logger

class RequestsUtil:
    def __init__(self, base_url="", timeout = 10, headers = None):
        self.base_url = base_url.rstrip("/")  ##去掉末尾的“/”
        self.timeout = timeout
        self.session = requests.Session() ##创建对象
        ##如果传入了请求头则更新到session中
        if headers:
            self.session.headers.update(headers)

    def _url(self, path):
        if path.startswith("http"):
            return path
        return f"{self.base_url}{path}"

    def requests(self, method, path, **kwargs):
        url = self._url(path)
        kwargs.setdefault("timeout", self.timeout)
        logger.info(f"请求{method}{url} | params={kwargs.get('params')} | json={kwargs.get('json')}")
        resp = self.session.request(method, url, **kwargs)
        logger.info(f"响应{resp.status_code} | body={resp.text[:500]}")
        return resp

    def get(self, path, **kwargs):
        return self.requests("GET", path, **kwargs)

    def post(self, path, **kwargs):
        return self.requests("POST", path, **kwargs)

    def put(self, path, **kwargs):
        return self.requests("PUT", path, **kwargs)

    def patch(self, path, **kwargs):
        return self.requests("PATCH", path, ** kwargs)

    def delete(self, path, **kwargs):
        return self.requests("DELETE", path, **kwargs)

    def set_token(self, token):
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def close(self):
        self.session.close()