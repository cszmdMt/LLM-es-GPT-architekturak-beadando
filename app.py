"""
Main entry point for the Streamlit Intelligent Document Analysis and Knowledge Base System.
"""
import streamlit as st

def main():
    st.set_page_config(page_title="Intelligent Doc Analysis", layout="wide")
    st.title("Intelligent Document Analysis & Knowledge Base")
    st.write("Welcome to the system. Use the sidebar to navigate between pages.")

if __name__ == "__main__":
    main()
