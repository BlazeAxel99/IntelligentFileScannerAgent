# IntelligentFileScannerAgent

## 📄 Overview

The IntelligentFileScannerAgent is a Streamlit-based application designed to intelligently process and analyze uploaded text files (`.txt`). It leverages a modular, "agentic" architecture to demonstrate how a simple task can be broken down into specialized components (an agent, its tools, and data models) for better organization, maintainability, and future extensibility.

Currently, the agent's primary capability is to scan text files and provide statistics on the number of lines and characters within each file, presented in a clear tabular format.

---

## ✨ Features

- **User-Friendly UI**: Built with Streamlit for an intuitive web interface.
- **Multi-File Upload**: Supports uploading multiple `.txt` files simultaneously.
- **Agentic Architecture**: Demonstrates a basic agent-tool paradigm for structured development.
- **Modular Design**: Clear separation of concerns into agents, tools, data models, and UI utilities.
- **Line & Character Count**: Accurately scans and reports the total number of lines and characters for each uploaded file.
- **Tabular Results**: Displays scan results in an easy-to-read table using Pandas.

---

## 🏗️ Architecture

The project follows a simple agentic design pattern:

- **app.py**: The main Streamlit application. Handles user interaction (file uploads) and acts as the orchestrator, delegating file processing to the FileProcessingAgent.
- **agents/**: Contains the core `FileProcessingAgent`. This agent manages the file processing workflow, decides which tools to use, and coordinates the overall task.
- **tools/**: Houses specialized functions that the agent can "use" to perform specific tasks. Currently includes `TextAnalysisTools` for counting lines and characters. Designed for future expansion.
- **core/**: Defines common data models (e.g., `FileScanResult`, `AgentExecutionResult`) to ensure consistent data structures throughout the application.
- **utils/**: Provides utility functions, such as `ui_utils` for formatting and displaying results in the Streamlit interface.

<details>
<summary>Project Structure</summary>

```
intelligent_scanner_agent/
├── app.py
├── agents/
│   └── file_processing_agent.py
├── tools/
│   └── text_analysis_tools.py
├── core/
│   └── data_models.py
├── utils/
│   └── ui_utils.py
└── requirements.txt
```
</details>

---

## 🚀 How to Run

Follow these steps to get the IntelligentFileScannerAgent up and running on your local machine.

### Prerequisites

- Python 3.8+

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/IntelligentFileScannerAgent.git
    cd IntelligentFileScannerAgent
    ```
    *(Remember to replace `your-username` with your actual GitHub username)*

2. **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    # venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```



### Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

This command will open a new tab in your default web browser (usually at http://localhost:8501).

- **Upload Files:** Use the "Choose .txt files" button to select one or more text files from your computer.
- **View Results:** The agent will process the files, and the scan results (file name, number of lines, number of characters) will be displayed in a table below the uploader.

---

## 💡 Future Enhancements

- **More Text Analysis Tools:**
    - Word count
    - Average word length
    - Keyword extraction
    - Readability scores (e.g., Flesch-Kincaid)
    - Basic sentiment analysis (using a simple lexicon or pre-trained model)
- **Support for Other File Types:** Extend the agent to handle `.csv`, `.docx`, or `.pdf` files (requires additional parsing libraries).
- **Advanced Agent Capabilities:**
    - Dynamic tool selection based on user prompts (e.g., using an LLM).
    - Tool chaining for more complex workflows.
    - Agent memory to retain context between operations.
- **Downloadable Reports:** Allow users to download the scan results as a CSV or JSON file.
- **Error Handling Improvements:** More robust error reporting and user feedback for file processing issues.

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please feel free to:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add YourFeature'`).
5. Push to the branch (`git push origin feature/YourFeature`).
6. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
