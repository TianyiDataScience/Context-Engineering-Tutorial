<h1 align="center">
  <br>
  <img src="./assets/icon.png" alt="Markdownify" width="200"></a>
    <img src="./assets/screenshot.jpg" alt="App Screenshot" width="500"/>
  <br>
  Context-Engineering-Tutorial
  <br>
</h1>

<h4 align="center">A theorical and practical context engineering tutorial based on <a href="[http://[electron.atom.io](https://github.com/langchain-ai/langchain)](https://github.com/langchain-ai/langchain)" target="_blank">LangChain and LangGraph </a>.</h4>

<p align="center">
  <a href="https://badge.fury.io/js/electron-markdownify">
    <img src="https://badge.fury.io/js/electron-markdownify.svg"
         alt="Gitter">
  </a>
  <a href="https://gitter.im/amitmerchant1990/electron-markdownify"><img src="https://badges.gitter.im/amitmerchant1990/electron-markdownify.svg"></a>
  <a href="https://saythanks.io/to/bullredeyes@gmail.com">
      <img src="https://img.shields.io/badge/SayThanks.io-%E2%98%BC-1EAEDB.svg">
  </a>
  <a href="https://www.paypal.me/AmitMerchant">
    <img src="https://img.shields.io/badge/$-donate-ff69b4.svg?maxAge=2592000&amp;style=flat">
  </a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download">Download</a> •
  <a href="#credits">Credits</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>

1. **下载VS code：**
    1. https://code.visualstudio.com/
2. **安装uv：**
    1. Linux/MacOS：
        
        ```bash
        curl -LsSf https://astral.sh/uv/install.sh | sh
        ```
        
        后重启终端
        
    2. Windows:
        
        ```powershell
        irm https://astral.sh/uv/install.ps1 | iex
        ```
        
        后重启powershell
        
    
    ?什么是uv?
    
    uv是用于 Python 的一个非常快速的包安装器和解析器
    
    uv 主要能做到两件核心事情，并将它们做得极快：
    1. 包管理：作为 pip 和 pip-tools 的一个完整且极速的替代品。
    2. 虚拟环境管理：作为 venv 或 virtualenv 的一个快速替代品。
    ```
    
3. **设置项目并运行 AI 代理**
    
    ```
    mkdir my-ai-agent
    cd my-ai-agent
    ```
    
4. **创建并激活虚拟环境**：`uv` 会自动在名为 `.venv` 的文件夹中创建环境。
    1. Linux/MacOS：
        
        ```bash
        # 创建虚拟环境
        uv venv
        # 激活虚拟环境
        source .venv/bin/activate 
        ```
        
    2. Windows
        
        ```powershell
        # 创建虚拟环境
        uv venv
        # 激活虚拟环境
        .\.venv\Scripts\Activate.ps
        ```
    
5. **初始化项目**：此命令会创建一个 `pyproject.toml` 文件。
    
    ```bash
    	uv init
    ```
    
6. **安装依赖库**：
    
    ```
    uv add langchain langchain_community python-dotenv
    ```
    
7. **创建 Python 脚本文件**：
    
    ```bash
    # linux/mac
    touch chat_agent.py
    # windows
    ni chat_agent.py
    ```
    
8. 在项目中创建 `.env` 文件
    
    ```bash
    # 确保你在 my-ai-agent 文件夹内
    # linux/mac
    touch .env
    # windows
    ni .env
    ```
    
    打开 `.env` 文件，然后像下面这样写入您的密钥（注意：没有 `export`，格式是 `KEY=VALUE`）：
    
    `GOOGLE_API_KEY='你的密钥'`
    
9. **确保向 Python 程序传递中文字符时，使用的编码格式是 Python 和 LangChain 所期望的 UTF-8**。
    
    ```bash
    # WSL/Linux
    echo 'export PYTHONUTF8=1' >> ~/.bashrc
    ```
    
    然后启动新的终端
    
10. **粘贴代码**：将您的 AI 代理代码粘贴到打开的编辑器中， 保存。
11. **运行脚本**：
    
    ```
    python chat_agent.py

    ```
