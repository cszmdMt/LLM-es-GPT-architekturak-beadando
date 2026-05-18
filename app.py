import streamlit as st

st.set_page_config(
    page_title="Intelligens-Dokumentum-Elemző",
    page_icon="🐕",
    layout="wide"
)

dashboard_page = st.Page(
    "pages/dashboard.py",
    title="Vezérlőpult",
    icon="⚙️"
)

analysis_page = st.Page(
    "pages/analysis.py",
    title="Elemzés és Eredmények",
    icon="📉"
)

chat_page = st.Page(
    "pages/chat.py",
    title="Dobby",
    icon="🧝"
)

pg = st.navigation([dashboard_page, analysis_page, chat_page])

pg.run()
