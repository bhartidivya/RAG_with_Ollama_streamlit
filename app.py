import streamlit as st
from rag_ollama import RAG

rag_system = RAG()


def main():
    st.title("Query document wth Ollama!")
    question = st.text_input("Ask your question:")
    if st.button("Query document"):
        response = rag_system.answer_query(question)
        st.write(response)

if __name__ == "__main__":
    main()
