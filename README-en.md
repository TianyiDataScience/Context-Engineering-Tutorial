<h1 align="center">
  <br>
  <img src="./assets/icon.png" alt="Markdownify" width="300"></a>
  <br>
  Context-Engineering-Tutorial
  <br>
</h1>

<h4 align="center">A theorical and practical context engineering tutorial based on <a href="[http://[electron.atom.io](https://github.com/langchain-ai/langchain)](https://github.com/langchain-ai/langchain)" target="_blank">LangChain and LangGraph </a>.</h4>


<p align="center">
  English · <a href="./README.md">简体中文</a>
</p>


<p align="center">
  <a href="#main-features">Main Features</a> •
  <a href="#contents">Contents</a> •
  <a href="#how-to-use">How to Use</a> •
  <a href="#guide-for-non-programmers">Guide for Non-programmers</a> •
  <a href="#license">License</a>
</p>

## Key Feature

* Slides for theorical explanation + Python code for realization.
  
## How To Use
```bash
# Clone this repository
$ git clone https://github.com/TianyiDataScience/Context-Engineering-Tutorial.git

# Go into the repository
$ cd Context-Engineering-Tutorial
```

## Guide for no-coders

1. **Download and set up VS code：**
    1. https://code.visualstudio.com/
    2. Install and open VS Code
    3. Create a new folder locally and open it in VS Code
       
       <img src="./assets/vscode_init.png" alt="Markdownify" width="450">
2. **Install uv：**
    1. Linux/MacOS：
        
        ```bash
        curl -LsSf https://astral.sh/uv/install.sh | sh
        ```
        
        Then restart the terminal.
       
       <img src="./assets/uv_install_linuxmac.png" alt="Markdownify" width="450">
        
    3. Windows:
        
        ```powershell
        powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
        ```
        
        Then restart PowerShell.
       
        <img src="./assets/uv_install_windows.png" alt="Markdownify" width="450">
    
    ? What is uv?

    uv is an extremely fast Python package installer and resolver.
    
    uv primarily does two core things, and does them extremely fast:
    
    Package management: A complete and extremely fast replacement for pip and pip-tools.
    
    Virtual environment management: A fast replacement for venv or virtualenv.
    ```
   
3.**Clone the project**
  1. Install git: Go to the page https://git-scm.com/book/en/v2/ and follow the installation instructions in section 1.5.
  2. In your terminal: ：git clone https://github.com/TianyiDataScience/Context-Engineering-Tutorial.git
     
     <img src="./assets/git_clone.png" alt="Markdownify" width="450">

    
4. **Enter the project directory**
    
    ```
    cd Context-Engineering-Tutorial
    ```
    
5. **Create and activate the virtual environment:** uv will automatically create an environment in a folder named .venv.
    1. Linux/MacOS：
        
        ```bash
        # Create the virtual environment
        uv venv
        # Activate the virtual environment
        source .venv/bin/activate 
        ```
         <img src="./assets/venv.png" alt="Markdownify" width="450">

    2. Windows
        
        ```powershell
        # Create the virtual environment 
        uv venv
        #  Activate the virtual environment
        .\.venv\Scripts\Activate.ps
        ```
        
    
5. **Install all project dependencies:**：
    
    ```
    uv sync
    ```
    Why use uv sync? It reads the uv.lock file to ensure that every library installed is the exact same version used by the project author.
    
6. **Configure environment variables:**：
   
   Copy .env.example to a new .env file.
    ```bash
    # linux/mac
    cp .env.example .env
    # windows
    copy .env.example .env
    ```
    Then open this new .env file and fill in your own API keys.
    
7. **Run a script:**：
    
    ```
    # For example, to run the window memory chatbot
    python window_memory_v1.py
    <img src="./assets/launch_script.png" alt="Markdownify" width="450">

    ```


## License

MIT



