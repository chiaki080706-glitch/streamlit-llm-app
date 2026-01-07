from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI

from langchain_core.messages import SystemMessage, HumanMessage 


def call_llm(user_input: str, expert_type: str) -> str:
    """
    入力テキストと専門家タイプを受け取り、
    LLMからの回答テキストを返す関数
    """         

    # 専門家タイプごとのシステムメッセージ
    if expert_type == "A":
        system_prompt = "あなたは経験豊富なITアーキテクトです。専門的かつ実務的に回答してください。"
    else:
        system_prompt = "あなたはファッションアドバイザーです。初心者にも分かりやすく丁寧に説明してください。"

    llm = ChatOpenAI(
        model_name="gpt-4o-mini",
        temperature=0
    )

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input)
    ]

    result = llm(messages)
    return result.content


st.title("サンプルアプリ: Webアプリ")

st.write("##### 動作モード1: ITアーキテクトへの相談")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことでITアーキテクトへの相談ができます。")
st.write("##### 動作モード2: ファッションアドバイス")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことでファッションアドバイスが受けられます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["ITアーキテクトへの相談", "ファッションアドバイス"]
)

st.divider()

if selected_item == "ITアーキテクトへの相談":
    input_message = st.text_area(label="ITアーキテクトへの相談内容を入力してください。", height=150,
    placeholder="ここにテキストを入力してください")

else:
    input_message = st.text_area(label="ファッションについての相談内容を入力してください。", height=150,
    placeholder="ここにテキストを入力してください")

if st.button("送信"):
    expert_type = "A" if selected_item == "ITアーキテクトへの相談" else "B" 
    user_input = input_message
    
    if user_input.strip() == "":
        st.warning("テキストを入力してください。")
    else:
        with st.spinner("LLMが回答を生成しています..."):
            answer = call_llm(user_input, expert_type)

        st.subheader("回答結果")
        st.write(answer)
