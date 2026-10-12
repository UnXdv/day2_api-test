# day2_api-test

基于 Python + pytest + requests 的接口自动化测试项目，覆盖 httpbin、JSONPlaceholder 公开接口，封装统一请求工具，支持日志记录和接口关联测试。

## 技术栈

- Python 3.12
- pytest 9.x
- requests
- pytest-cov（覆盖率统计）

## 目录结构


```text
day2_api-test/
├── http_demo/            # httpbin 接口练习
├── mock/                 # 本地 mock 服务
├── tests/                # 测试用例
│   ├── conftest.py       # fixture：封装后的 client
│   ├── test_httpbin.py
│   ├── test_jsonplaceholder.py
│   └── test_chain.py     # 接口关联用例
├── utils/
│   ├── logger.py         # 日志封装
│   └── request_util.py   # 统一请求封装（session + 日志 + 超时）
├── logs/                 # 运行日志（不提交 Git）
├── pytest.ini
├── requirements.txt
└── README.md
```

## 环境要求

python 3.10+
pip

## 安装

```bash
git clone https://github.com/UnXdv/day2_api-test.git
cd day2_api-test
python -m venv day2.venv
day2.venv\Scripts\Activate
pip install -r requirements.txt
```

## 运行测试

```bash
#全量
pytest
#指定文件
pytest tests/test_jsonplaceholder.py
#详细输出
pytest -v
#覆盖率
pip install pytest -cov
pytest --cov=utils tests/
```

## 测试覆盖场景
 - httpbin：GET/POST、params、json、headers、Basic Auth、状态码、延迟
 - jsonplaceholder：帖子的增删改查、按用户过滤、404场景
 - chain：先查用户->再查用户帖子；先创建->再查询

 ## 日志
 运行后日志会写入
 ```text
 时间 【等级】 内容
 2026-10-XX 13:46:28,671 [INFO] 请求POSThttps:// | params= | json={}
 2026-10-XX 13:46:28,944 [INFO] 响应XXX | body={}
 ```
## 设计说明

 - RequestsUtil 基于 requests.Session 封装，统一管理 base_url、超时、请求头
 - 通过 conftest.py 的 fixture 注入 client，用例不直接调用 requests
 - 日志记录请求和响应，便于定位问题
 - 覆盖率当前 85%

 ## 后续计划

 - 接入 Allure 报告
 - 增加数据驱动（YAML）
 - 增加失败重试、并发执行
 - 接入 GitHub Actions CI

