import io

class TextAnalysisTools:
    @staticmethod
    def count_lines_and_chars(file_content: str) -> tuple[int, int]:
        """
        Counts the number of lines and characters in a given text content.
        This acts as a "tool" the agent can use.
        """
        lines = file_content.splitlines()
        num_lines = len(lines)
        num_chars = len(file_content)
        return num_lines, num_chars

    # @staticmethod
    # def count_words(file_content: str) -> int:
    #     # Example of another tool
    #     words = file_content.split()
    #     return len(words)