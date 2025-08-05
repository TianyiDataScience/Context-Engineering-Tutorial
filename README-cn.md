<h1 align="center">
  <br>
  <img src="./assets/icon.png" alt="Markdownify" width="300"></a>
  <br>
  上下文工程教程 (Context-Engineering-Tutorial)
  <br>
</h1>

<h4 align="center">一个基于 <a href="https://github.com/langchain-ai/langchain" target="_blank">LangChain 和 LangGraph</a> 的上下文工程理论与实践教程。</h4>

<p align="center">
  <a href="./README.md">English</a>・简体中文
</p>

<p align="center">
  <a href="https://badge.fury.io/js/electron-markdownify">
    <img src="https://badge.fury.io/js/electron-markdownify.svg"
         alt="Gitter">
  </a>
  <a href="https://gitter.im/amitmerchant1990/electron-markdownify"><img src="https://badges.gitter.im/amitmerchant1990/electron-markdownify.svg" alt="Gitter聊天"></a>
  <a href="https://saythanks.io/to/bullredeyes@gmail.com">
      <img src="https://img.shields.io/badge/SayThanks.io-%E2%98%BC-1EAEDB.svg" alt="说声谢谢">
  </a>
  <a href="https://www.paypal.me/AmitMerchant">
    <img src="https://img.shields.io/badge/$-赞赏-ff69b4.svg?maxAge=2592000&amp;style=flat" alt="赞赏">
  </a>
</p>

<p align="center">
  <a href="#主要特性">主要特性</a> •
  <a href="#内容">内容</a> •
  <a href="#如何使用">如何使用</a> •
  <a href="#给非程序员的指南">给非程序员的指南</a> •
  <a href="#许可证">许可证</a>
</p>

## 主要特性

* 理论讲解幻灯片 + Python 代码实现。
* 基于Youtube和B站视频教程：木子不写代码
  * Youtube: https://www.youtube.com/channel/UCY3SgqRpZd0GWWk8dRCybdw
  * B站： https://space.bilibili.com/13416784
  * 小红书：木子不写代码
* 视频教程尚在更新中...

## 内容

* 记忆：
  * 窗口记忆：
    * 课件：Context Engineering-WindowMemory-cn.pdf
    * 实现方式1脚本(旧版langchain)：window_memory_v1.py
    * 实现方式2脚本(当前版本langchain)：window_memory_v2.py

## 如何使用
```bash
# 克隆此仓库
$ git clone [https://github.com/TianyiDataScience/Context-Engineering-Tutorial.git](https://github.com/TianyiDataScience/Context-Engineering-Tutorial.git)

# 进入仓库目录
$ cd Context-Engineering-Tutorial
```

## 给非程序员的指南
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

## 许可证

MIT


