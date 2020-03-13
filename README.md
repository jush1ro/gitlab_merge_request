# Gitlab 发起并执行 分支合并请求 脚本

1. 在 gitlab 代码仓库中创建 private token
![gitlab_private_token](gitlab_private_token.png)

2. 修改 `config.py` 配置

3. 安装 `python-gitlab` 依赖
  
sudo pip install --upgrade python-gitlab

3. 执行 `main.py` 方法，按提示操作

```shell script
#!/bin/bash

mdir=$(dirname $0)
echo `alias mr="python3 $mdir/main.py"` > ~/.bashrc
```