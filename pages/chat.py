import streamlit as st

from utils.ai_client import get_ai_response
from utils.state_manager import init_session_state


init_session_state()

if not st.session_state.get("is_processed", False):
    st.warning("Még nincs feldolgozott dokumentum!")
    st.stop()

if "messeages" not in st.session_state:
    st.session_state.messeages = []

for messeage in st.session_state.messeages:
    with st.chat_message(messeage["role"]):
        st.markdown(messeage["content"])

if prompt := st.chat_input("Kérdezz a feltöltött dokumentummal kapcsolatban: "):
    st.session_state.messeages.append(
            {
            "role": "user",
            "content": prompt
            }
        )
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Gondolkodom..."):
            response = get_ai_response(prompt, st.session_state.text_chunks)

    st.session_state.messeages.append(
        {
            "role" : "assistant",
            "content" : response
        }
    )