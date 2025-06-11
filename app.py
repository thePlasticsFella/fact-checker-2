import streamlit as st
from agent import fact_check

st.title("🧠 MedFact: Peer-Reviewed Fact Checker")
text = st.text_area("Paste your article or paragraph:")

if st.button("Fact Check"):
    with st.spinner("Checking..."):
        results = fact_check(text)
        for claim, result in results:
            st.markdown(f"**🔍 Claim:** {claim.strip()}\n**✅ Evidence:** {result.strip()}")
            st.markdown("---")