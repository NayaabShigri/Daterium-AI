import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Configuration
st.set_page_config(page_title="Daterium AI", page_icon="📊", layout="wide")

# Custom CSS for the "Daterium" look
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("Daterium Pulse")
    st.subheader("📰 Economic News Digest")
    st.info("**IMF Update:** Pakistan's growth forecast revised to 3.5% for 2026.")
    st.divider()
    st.subheader("🧪 Formula Lab")
    st.latex(r"GDP = C + I + G + (X - M)")

# Main Content
st.title("Welcome back, Hussain. 🚀")
col1, col2, col3 = st.columns(3)
with col1: st.metric(label="USD/PKR", value="280.50", delta="-0.20")
with col2: st.metric(label="Inflation (CPI)", value="12.4%", delta="-1.1%")
with col3: st.metric(label="KSE-100 Index", value="78,450", delta="+450")

st.divider()
st.subheader("🤖 Ask Daterium")
prompt = st.chat_input("Ex: Explain the Misery Index...")
if prompt:
    st.write(f"Daterium is analyzing: {prompt}")
