import requests

BASE = "https://jsonplaceholder.typicode.com"

##接口关联，上一个接口的出参作为下一个接口的入参
def test_get_user_then_posts():
    #1.查用户
    r1 = requests.get(f"{BASE}/users/1", timeout= 10)
    assert r1.status_code == 200
    user_id = r1.json()['id']

    #2.用user_id查帖子
    r2 = requests.get(f"{BASE}/posts", params={"userId": user_id}, timeout= 10)
    assert r2.status_code == 200
    posts = r2.json()
    assert len(posts) > 0
    assert all(p["userId"] == user_id for p in posts)

def test_create_then_get():
    #创建成功返回201
    r1 = requests.post(f"{BASE}/posts",
                       json={"title": "t", "body": "b", "userId": 1},
                       timeout= 10)
    assert r1.status_code == 201
    new_id = r1.json()["id"]

    #查询刚创建的
    r2 = requests.get(f"{BASE}/posts/1", timeout= 10) ##posts/{new_id}->1,new_id实际为101，网站不存储数据，故返回的状态码实际会为404
    assert r2.status_code == 200
    assert r2.json()["id"] == 1

##token关联
def test_token_flow():
    ##登录拿token
    r1 = requests.get("http://localhost:3000/login",
                       json={"username": "u", "password": "p"}, timeout= 10)
    print("响应 JSON:", r1.json())
    token = r1.json()[0]["token"]
    
    ##带token请求
    r2 = requests.get("http://localhost:3000/profile",
                      headers={"Authorization": f"Bearer {token}"}, timeout= 10)
    assert r2.status_code == 200