import streamlit as st
import openai

# OpenAI API 키 설정 (환경 변수나 직접 입력 가능)
openai.api_key = "YOUR_OPENAI_API_KEY"

# Streamlit 페이지 설정
st.set_page_config(
    page_title="ChatGPT 웹 챗봇",
    page_icon="🤖",
    layout="centered",
)

# 앱 헤더
st.title("🎙️ ChatGPT 챗봇")
st.markdown(
    """
    이 앱은 OpenAI GPT API를 활용하여 사용자의 질문에 답변합니다.  
    아래 입력창에 질문을 입력하고, "보내기" 버튼을 눌러주세요.
    """
)

# 사용자 입력
user_input = st.text_input("질문을 입력하세요", placeholder="여기에 질문을 입력...")

# GPT 응답
if st.button("보내기"):
    if user_input:
        try:
            with st.spinner("응답 생성 중..."):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": user_input}],
                )
                bot_reply = response["choices"][0]["message"]["content"]
                st.markdown("### 🤖 ChatGPT 응답")
                st.write(bot_reply)
        except Exception as e:
            st.error(f"에러가 발생했습니다: {str(e)}")
    else:
        st.warning("질문을 입력해주세요!")

# 페이지 푸터
st.markdown("---")
st.markdown("Powered by [OpenAI](https://openai.com) | Created with 💻 Streamlit")
