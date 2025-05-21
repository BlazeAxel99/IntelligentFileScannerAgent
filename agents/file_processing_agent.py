from typing import List
from core.data_models import FileScanResult, AgentExecutionResult
from tools.text_analysis_tools import TextAnalysisTools
import io

class FileProcessingAgent:
    def __init__(self):
        self.tools = {
            "line_char_counter": TextAnalysisTools.count_lines_and_chars,
            # Add more tools here as the agent's capabilities expand
            # "word_counter": TextAnalysisTools.count_words,
        }

    def process_files(self, uploaded_files_data: List[bytes], file_names: List[str]) -> AgentExecutionResult:
        """
        The agent's main execution method. It takes raw file data, decides which
        tools to use, and returns structured results.
        """
        if not uploaded_files_data:
            return AgentExecutionResult(success=False, message="No files provided for processing.")

        scan_results: List[FileScanResult] = []
        errors = []

        for i, file_data in enumerate(uploaded_files_data):
            file_name = file_names[i]
            try:
                # Decode the file content
                string_io = io.StringIO(file_data.decode("utf-8"))
                file_content = string_io.read()

                # Agent decides to use the line_char_counter tool
                num_lines, num_chars = self.tools["line_char_counter"](file_content)

                scan_results.append(FileScanResult(file_name, num_lines, num_chars))
            except Exception as e:
                errors.append(f"Error processing file '{file_name}': {e}")

        if errors:
            return AgentExecutionResult(success=False, message=f"Processed with errors: {'; '.join(errors)}", data=scan_results)
        else:
            return AgentExecutionResult(success=True, message="Files processed successfully.", data=scan_results)