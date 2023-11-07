import streamlit as st
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

from apikey import apikey

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

def submit():
    st.session_state.user_input = st.session_state.widget
    st.session_state.widget = ""

st.title("Порфирий")
st.image('Porphyrius.jpg', caption=None, width=200, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
user_input = st.text_input("Пользователь: ", key="widget", on_change=submit)

user_input = st.session_state.user_input

chat = GigaChat(credentials=apikey, 
                verify_ssl_certs=False, temperature=0.9)

messages = [
    SystemMessage(
        content="Ты мужчина, великий римский император Порфирий. Твоя задача разговаривать на философские темы."
    )
]

if user_input:
    messages.append(HumanMessage(content=user_input))
    res = chat(messages)
    messages.append(res)
    st.write("Порфирий: ", res.content)