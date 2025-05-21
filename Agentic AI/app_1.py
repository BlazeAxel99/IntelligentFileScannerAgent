import streamlit as st
import pandas as pd
import io

def process_text_file(file_content):
    """
    Processes the content of a text file to count lines and characters.

    Args:
        file_content (str): The content of the uploaded text file.

    Returns:
        tuple: A tuple containing (num_lines, num_chars).
    """
    lines = file_content.splitlines()
    num_lines = len(lines)
    num_chars = len(file_content)
    return num_lines, num_chars

def main():
    st.set_page_config(page_title="Intelligent File Scanner", layout="centered")

    st.title("📄 Intelligent File Scanner")
    st.markdown(
        """
        Upload your `.txt` files here to get a quick scan of the number of lines and characters!
        """
    )

    uploaded_files = st.file_uploader(
        "Choose .txt files", type="txt", accept_multiple_files=True
    )

    if uploaded_files:
        results = []
        for uploaded_file in uploaded_files:
            # Read the file content as a string
            string_io = io.StringIO(uploaded_file.getvalue().decode("utf-8"))
            file_content = string_io.read()

            num_lines, num_chars = process_text_file(file_content)
            results.append({
                "File Name": uploaded_file.name,
                "Number of Lines": num_lines,
                "Number of Characters": num_chars
            })

        if results:
            df = pd.DataFrame(results)
            st.subheader("Scan Results:")
            st.table(df)

if __name__ == "__main__":
    main()