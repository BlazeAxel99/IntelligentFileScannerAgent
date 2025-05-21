from typing import List, Dict

class FileScanResult:
    def __init__(self, file_name: str, num_lines: int, num_chars: int):
        self.file_name = file_name
        self.num_lines = num_lines
        self.num_chars = num_chars

    def to_dict(self) -> Dict:
        return {
            "File Name": self.file_name,
            "Number of Lines": self.num_lines,
            "Number of Characters": self.num_chars
        }

class AgentExecutionResult:
    def __init__(self, success: bool, message: str, data: List[FileScanResult] = None):
        self.success = success
        self.message = message
        self.data = data if data is not None else []