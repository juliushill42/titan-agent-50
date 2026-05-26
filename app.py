import streamlit as st
from agent import agent, runner

st.set_page_config(page_title="agent-{Num}", layout="wide")
st.title("agent-{Num} ({Track})")
st.caption("Production Ready - All Green")

if prompt := st.chat_input("Enter your message"):
    with st.spinner("Agent processing..."):
        response = runner.run_sync(agent, input=prompt)
        st.write(response)
