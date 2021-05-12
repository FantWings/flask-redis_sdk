# Flask 后端 Redis 简易增删改查 SDK

用于给 Flask 后端准备的增删改查 SDK，详情可读代码，已添加注释

## 快速上手

- 下载源码：`git@github.com:FantWings/flask-redis_sdk.git`
- 安装依赖： `pip install -r requirements.txt`
- 运行后端： `flask run -h 0.0.0.0`
- 快速测试：
  - Redis 读 ：http://localhost:5000/read?key=test
  - Redis 写 ：http://localhost:5000/write?key=test&value=xiaozhupeiqi&expire=300
  - Redis 删 ：http://localhost:5000/delete?key=test

## 配置文件

    位于settings.py内，仅作为轻量测试使用，你可以用自己上手的方式从json或ini/env的方式来读取对应的配置。
