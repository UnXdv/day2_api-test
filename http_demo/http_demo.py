import requests

# BASE = "https://httpbin.org"

# def login():
#     r = requests.post(f"{BASE}/post", json={"username": "alice", "password": "123"},timeout = 5)
#     r.raise_for_status
#     return r.json()

# def get_profile(token):
#     header = {"Authotization":f"Bearer {token}"}
#     r = requests.get(f"{BASE}/get", headers = header, timeout = 5)
#     r.raise_for_status
#     return r.json

# token = "demo-token"
# print(get_profile(token))
# print(login())

# r = requests.get(
#     "https://httpbin.org/get",
#     params={"q":"python", "page":1},
#     headers={"User-Agent":"my-app/1.0"},
#     timeout= 5 
# )
# print(r.status_code)
# print(r.url)
# print(r.json())

# r = requests.post(
#     "https://httpbin.org/post",
#     json={"name": "Alice", "age": 18},
#     headers={"Authorization": "Bearer xxx"},
#     timeout= 5
# )
# data = r.json()
# print(r.status_code)
# print(r.json()['headers']['Content-Type'])
# print(data.get('headers', {}).get('Content-Type'))

# url = "https://httpbin.org"
# headers = {
#     "User-Agent": "my-aapp/1.0",
#     "Authorization": "Bearer <token>",
#     "Accept": "application/json",
# }
# r = requests.get(f"{url}/get", headers= headers, timeout=(3,10))
# print(r.status_code)
# print(r.headers)
# print(r.text)
# print(r.content)
# print(r.json())
# # print(r.headers.get("Content-Type"))
# # print(r.text[:500])

# r = requests.get("https://httpbin.org/get", params={"a":1}, timeout=10)
# print(r.status_code,r.json()["origin"],r.url,r.json(),sep='\n')

# r = requests.post("https://httpbin.org/post", json={"name": "tom"}, timeout=10)
# print(r.text, r.content, r.json(), sep='\n')

# r = requests.get("https://httpbin.org/headers",
#                  headers={"token": "abc"}, timeout=10)
# print(r.json()["headers"]["Token"])
# print(r.text)

# r = requests.get("https://httpbin.org/basic-auth/user/pass",
#                  auth=("user", "pass"), timeout=10)
# print(r.status_code)
# print(r.text)

# BASE = "https://jsonplaceholder.typicode.com"
# r1 = requests.post(f"{BASE}/posts",
#                        json={"title": "t", "body": "b", "userId": 1},
#                        timeout= 10)
# new_id = r1.json()["id"]
# print(new_id)

# r1 = requests.post("https://httpbin.org/post",
#                        json={"username": "u", "password": "p"}, timeout= 10)
# print("状态码:", r1.status_code)
# print("Content-Type:", r1.headers.get("Content-Type"))
# print("响应体前 500 字符:", r1.text[:500])
# #token = r1.json()["token"]
r1 = requests.get("http://localhost:3000/login",
                       json={"username": "u", "password": "p"}, timeout= 10)
print("响应 JSON:", r1.json()[0]["token"])
