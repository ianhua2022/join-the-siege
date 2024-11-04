from abc import ABC, abstractmethod


class IndustryClassifier(ABC):
    @abstractmethod
    def classify(self, file_content: str) -> str:
        """Classify the industry based on file content.

        Args:
            file_content: String content of the file to classify

        Returns:
            String indicating the specific class/category within the industry
        """
        pass