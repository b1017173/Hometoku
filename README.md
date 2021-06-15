# Hometoku
Slack app Hometokuの開発

## 利用パッケージの共有方法
### 準備
1. `$ git pull origin main`
2. `$ python3 -m venv .venv`
3. `$ source .venv/bin/active`

### パッケージのインストールした時
1. `(.venv)$ pip install xxx(インストールするパッケージ)`
2. `(.venv)$ pip freexe > requirements.txt`
3. `(.venv)$ git add .`からいつものpushまで

### 他の人のものを引っ張ってくる時
1. `(.venv)$ git pull`
2. `(.venv)$ pip install -r requirements.txt`
