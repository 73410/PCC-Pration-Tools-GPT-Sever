# 一.说明
调用openai官方的付费api，国内用户必须**翻墙**才能用。
如遇到bug或问题请上传issues
# 二.搭建方法
## 1.下载库内文件
## 2.配置config.env
```env
MEMORY_DIR="./memory"
PORT=65017
API_KEY=""
PROXY=""
```
### 1.MEMORY_DIR
保存记忆文件的目录
### 2.PORT
服务器的端口
### 3.API_KEY
填入你的api key
[获取api key](https://platform.openai.com/account/api-keys)
### 4.PROXY
填入代理服务器ip（若没有空着）
## 3.安装python库和python
### python下载
[python下载地址](https://www.python.org/downloads/)
### python库下载
打开cmd，输入以下命令
```cmd
pip install fastapi
pip install revChatGPT
pip install uvicorn
pip install python-dotenv
```
## 4.运行服务器
先打开cmd，输入
```cmd
cd <文件所在目录>
python main.py
```
# 三、服务器内配置及使用
## 1.配置
打开服务牌的插件配置文件夹（Pcc_limbo_system）,打开config.yml找到以下项
'''yml
#ChatGPT的后端服务器ip
ip: http://htyuty.top
'''
将ip更改为你前面搭建的chatgpt服务器的ip
## 2.使用
输入指令/chat 问题 即可
