import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.messages import BaseMessage

# --- 1. 自定义带窗口功能的 ChatMessageHistory 子类 ---
# 将窗口管理的逻辑封装在这个类中，让主代码更整洁。
# ChatMessageHistory -> 在内存中（RAM）以列表的形式存储和管理对话消息
class WindowChatMessageHistory(ChatMessageHistory):
    """一个自动修剪消息以符合指定窗口大小的 ChatMessageHistory。"""

    k: int #对话轮数
    window_size: int #窗口大小

    # 调用父类的 __init__ 构造函数: 为新创建的对象设置其初始状态（属性）
    # 1.从外部接收最核心的参数 k。
    # 2.在内部根据 k 计算出父类需要的衍生参数 window_size。（window_size = k * 2）
    # 3.将所有必需的参数（原始的 k 和衍生的 window_size）一起打包，提交给父类的构造函数 super().__init__(...)，以满足其内部规定。
    def __init__(self, k: int):
        super().__init__(k=k, window_size=k * 2) 
        
    # 通过继承 ChatMessageHistory 并重写 (override) add_message 方法。
    # 默认会一直存储用户添加的所有消息，没有任何大小限制、截断或摘要功能。
    def add_message(self, message: BaseMessage) -> None:
        """添加一条消息，并在需要时修剪旧消息"""
        super().add_message(message)
        # 如果消息列表超过了窗口大小，就从列表开头移除最旧的消息
        if len(self.messages) > self.window_size:
            self.messages.pop(0)

# --- 2. 设置会话历史的管理函数 ---
# 这个函数为每个会话ID创建一个独立的、带窗口的记忆实例。
# 让一个AI同时和多个人聊天，并且能记住每个人最近说了什么。
# 通过 session_id 作为钥匙（key），为每一个独立的用户或会话创建一个专属的聊天记录存储区。
# store 这个字典就是用来存放所有这些存储区的。
store = {}
def get_session_history(session_id: str) -> WindowChatMessageHistory:
    if session_id not in store:
        # k=2 表示只记住最近2轮对话
        store[session_id] = WindowChatMessageHistory(k=2)
    return store[session_id]

# --- 3. 主函数 ---
def main():
    """主执行函数"""
    load_dotenv()
    os.getenv("GOOGLE_API_KEY")

    # 初始化LLM
    model = init_chat_model(
        model="gemini-2.5-flash",
        model_provider="google_genai"
    )

    # 定义提示模板，history部分会自动由RunnableWithMessageHistory填充
    prompt = ChatPromptTemplate.from_messages([
        ("system", "请你回答用户的问题，但不要总结对话历史。"), 
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ])
    
    # 创建核心的对话链
    runnable = prompt | model

    # 使用RunnableWithMessageHistory包装核心链，为其添加记忆功能
    chat_agent = RunnableWithMessageHistory(
        runnable,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history",
    )

    print("--- 滑动窗口记忆AI代理已启动 (只会记住最近2轮对话) ---")
    print("输入 'quit' 退出。")
    
    session_id = "window_chat_1"

    # 开始对话循环
    while True:
        user_input = input("🚀 你: ")
        if user_input.lower() == 'quit':
            print("🤖 AI: 再见！")
            break

        # 调用对话代理
        response = chat_agent.invoke(
            {'input': user_input},
            config={'configurable': {'session_id': session_id}}
        )
        print(f"🤖 AI: {response.content}")
        

if __name__ == "__main__":
    main()