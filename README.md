<h1 align="center">
  <br>
  <img src="./assets/icon.png" alt="Markdownify" width="300"></a>
  <br>
  Context-Engineering-Tutorial
  <br>
</h1>

<h4 align="center">A theorical and practical context engineering tutorial based on <a href="[http://[electron.atom.io](https://github.com/langchain-ai/langchain)](https://github.com/langchain-ai/langchain)" target="_blank">LangChain and LangGraph </a>.</h4>


<p align="center">
  English · <a href="./README-cn.md">简体中文</a>
</p>

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
  <a href="#key-features">Key Feature</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#Guide for no-coders">Guide for no-coders
</a> •
  <a href="#license">License</a>
</p>

## Key Feature

* Slides for theorical explanation + Python code for realization.

## How To Use
```bash
# Clone this repository
$ git clone https://github.com/TianyiDataScience/Context-Engineering-Tutorial.git)

# Go into the repository
$ cd Context-Engineering-Tutorial
```

## Guide for no-coders

1. **Download VS code：**
    1. https://code.visualstudio.com/
2. **Install uv：**
    1. Linux/MacOS：
        
        ```bash
        curl -LsSf https://astral.sh/uv/install.sh | sh
        ```
        
        then restart terminal
        
    2. Windows:
        
        ```powershell
        irm https://astral.sh/uv/install.ps1 | iex
        ```
        
        then restart powershell
        
    
    ?What is uv?

    uv is an extremely fast package installer and resolver for Python.

    uv primarily does two core things, and it does them extremely fast:

    Package management: As a complete and extremely fast replacement for pip and pip-tools.

    Virtual environment management: As a fast replacement for venv or virtualenv.
    ```
    
3. **Create a folder**
    
    ```
    mkdir my-ai-agent
    cd my-ai-agent
    ```
    
4. **Create and activate the virtual environment**：uv will automatically create an environment in a folder named .venv.。
    1. Linux/MacOS：
        
        ```bash
        # Create the virtual environment
        uv venv
        # Activate the virtual environment
        source .venv/bin/activate 
        ```
        
    2. Windows
        
        ```powershell
        # Create the virtual environment
        uv venv
        # Activate the virtual environment
        .\.venv\Scripts\Activate.ps
        ```
    
5. **Initialize the project:**：This command will create a pyproject.toml file.
    
    ```bash
    	uv init
    ```
    
6. **Install dependencies**：
    
    ```
    uv add langchain langchain_community python-dotenv
    ```
    
7. **Create the Python script file**：
    
    ```bash
    # linux/mac
    touch chat_agent.py
    # windows
    ni chat_agent.py
    ```
    
8. **Create the .env file in the project**
    
    ```bash
    # 确保你在 my-ai-agent 文件夹内
    # linux/mac
    touch .env
    # windows
    ni .env
    ```
    
    Open the .env file and write your key like below (Note: no export, the format is KEY=VALUE):

    GOOGLE_API_KEY='your_api_key'
    
    
9. **Paste the code**：Paste your AI agent code into the open editor and save.
11. **Run the script**：
    
    ```
    python chat_agent.py

    ```



## License

MIT


