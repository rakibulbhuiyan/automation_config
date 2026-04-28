
import requests

class HttpClient:
    def post(self, url, data=None, headers=None):
        try:
            r = requests.post(url, json=data, headers=headers)
            return r.status_code, r.json()
        except Exception as e:
            return 0, {"error": str(e)}