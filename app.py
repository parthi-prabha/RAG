import streamlit as st

from src.rag_pipeline import RAGPipeline


st.set_page_config(
    page_title="RAG Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 RAG Assistant")
st.write("Ask questions about your indexed documents.")

# Load pipeline once
@st.cache_resource
def load_pipeline():
    return RAGPipeline()

rag = load_pipeline()

question = st.text_input(
    "Enter your question:"
)

if st.button("Ask"):

    if question.strip():

        with st.spinner("Searching documents..."):

            result = rag.ask(question)

        st.subheader("Answer")

        st.write(result["answer"])

        st.subheader("Sources")

        for source in result["sources"]:
            st.write(f"📄 {source}")

    else:
        st.warning("Please enter a question.")