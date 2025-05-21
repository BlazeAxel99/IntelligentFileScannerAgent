import streamlit as st
import io
from agents.file_processing_agent import FileProcessingAgent
from utils.ui_utils import display_scan_results
from core.data_models import FileScanResult, AgentExecutionResult

def main():
    st.set_page_config(page_title="Intelligent File Scanner Agent", layout="centered")

    st.title("🤖 Intelligent File Scanner Agent")
    st.markdown(
        """
        Upload your `.txt` files here. Our agent will use its specialized tools
        to scan them for lines and characters!
        """
    )

    # Initialize the agent
    agent = FileProcessingAgent()

    uploaded_files = st.file_uploader(
        "Choose .txt files", type="txt", accept_multiple_files=True
    )

    if uploaded_files:
        # Prepare data for the agent
        file_contents_bytes = [file.getvalue() for file in uploaded_files]
        file_names = [file.name for file in uploaded_files]

        # Agent executes its task
        with st.spinner("Agent is processing files..."):
            agent_response: AgentExecutionResult = agent.process_files(file_contents_bytes, file_names)

        if agent_response.success:
            st.success(agent_response.message)
            display_scan_results(agent_response.data)
        else:
            st.error(f"Agent encountered an issue: {agent_response.message}")
            if agent_response.data:
                st.warning("Partial results are available:")
                display_scan_results(agent_response.data)

if __name__ == "__main__":
    main()
    