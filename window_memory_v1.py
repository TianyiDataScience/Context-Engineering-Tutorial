import os 
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate

load_dotenv()
os.getenv("GOOGLE_API_KEY")

# 定义一个多行字符串作为模板。
# {history} 和 {input} 是特殊占位符，不可更改。
# ConversationChain 会自动将记忆和用户输入填充到这里。
template = """
请你回答用户的问题，但不要总结对话历史

当前的对话历史:
{history}

用户: {input}
AI:
"""

# 使用模板字符串和指定的输入变量来创建一个PromptTemplate实例。
prompt = PromptTemplate(
    input_variables=["history", "input"], 
    template=template
)

# --- 1. 初始化模型 ---
llm= init_chat_model(model="gemini-2.5-flash",model_provider="google_genai")

# --- 2. 创建一个封装好的、带滑动窗口的记忆对象 ---
# 这是关键：一行代码就创建了一个功能完备的窗口记忆。
# 所有窗口管理的逻辑（pop、add等）都封装在它内部。
memory = ConversationBufferWindowMemory(k=2) # k=2 表示记住最近2轮对话

# --- 3. 创建一个封装好的对话链 ---
# ConversationChain 是一个高度封装的“黑盒子”。
# 它自动处理了提示模板、从记忆中读取历史、将新消息存入记忆等所有事情。
# 设置 verbose=True 可以让它在运行时打印出完整的内部提示，便于教学。
conversation = ConversationChain(
    llm=llm, 
    memory=memory, 
    prompt=prompt, # <--- 将自定义prompt传入
    verbose=True # 强烈建议在教学时开启
)

# --- 4. 启动对话 ---
# 调用方式也更简单，直接使用 .predict() 方法
print("--- 旧版封装组件AI代理已启动 (k=2) ---")
print("输入 'quit' 退出。")

while True:
    user_input = input("你: ")
    if user_input.lower() == 'quit':
        print("AI: 再见！")
        break
    
    # 直接调用 predict，传入用户输入即可。
    # 所有与记忆相关的操作都在后台自动完成了。
    response = conversation.predict(input=user_input)
    print(f"AI: {response}")