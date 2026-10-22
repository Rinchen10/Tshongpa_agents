import streamlit as st
import sqlite3
# Import the actual compiled agent engine blueprint directly from your core code layer
from langgraph_agent import tshongpa_engine

st.set_page_config(page_title="Tshongpa-AI Room", page_icon="🦣", layout="wide")
st.title("🦣 Chat with Tshongpa-AI Framework Core")
st.write("---")

col1, col2 = st.columns(2)

with col1:
    st.header("📊 System Operational Analytics")
    conn = sqlite3.connect("tshongpa.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS audit_logs (id INTEGER PRIMARY KEY, merchant_id TEXT, price REAL, verdict TEXT)")
    
    cursor.execute("SELECT COUNT(*) FROM audit_logs WHERE verdict LIKE '%BLOCKED%'")
    blocked_count = cursor.fetchone()[0] or 0
    st.metric(label="🔒 Total Scam Exploits Prevented", value=f"{blocked_count} Attacks")
    conn.close()

with col2:
    st.header("💬 Interactive Agent Core Chat")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Kuzu zangpo la! I am running on my core framework tracks. Send a deal details pitch text to begin."}]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if user_prompt := st.chat_input("Type e-commerce transaction information here..."):
        with st.chat_message("user"):
            st.write(user_prompt)
        st.session_state.messages.append({"role": "user", "content": user_prompt})

        with st.chat_message("assistant"):
            # Trigger the actual agent compiled execution loop
            inputs = {"raw_text": user_prompt}
            final_state = tshongpa_engine.invoke(inputs)
            
            # Pull the ready-made smart reasoning report card right out of the Agent State
            agent_report = final_state["audit_report"]["detailed_reasoning"]
            clean_metrics = final_state["clean_data"]
            
            # Render report on dashboard canvas
            st.markdown(agent_report)
            st.session_state.messages.append({"role": "assistant", "content": agent_report})
            
            # Log data record row securely
            conn = sqlite3.connect("tshongpa.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO audit_logs (merchant_id, price, verdict) VALUES (?, ?, ?)", 
                           (clean_metrics["merchant_id"], clean_metrics["price"], final_state["audit_report"]["verdict"]))
            conn.commit()
            conn.close()
            st.rerun()
