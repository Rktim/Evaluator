import streamlit as st
st.title("Evaluator !! 🧮")

exp=st.text_input("Enter your your expression:")

if st.button("Evaluate"):
    try:
        value=eval(exp)
        st.success(f"Result 😊: {value}")
    except Exception as e:
        st.error(f"ERROR ❌ : {e}")
        
        