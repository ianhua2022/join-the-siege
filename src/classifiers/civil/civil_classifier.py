from ..industry_classifier import IndustryClassifier
import joblib
import os


CIVIL_KEYWORDS = [
    'passport',
    'driving',
    'driver',
    'drivers',
    "driver's",
    'license',
    'licence',
    'permit',
    'ID',
    'identification'
]

CIVIL_FILE_CLASSES = ['passport', 'driver licence']


class CivilClassifier(IndustryClassifier):
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.vectorizer = joblib.load(os.path.join(current_dir, 'vectorizer.joblib'))
        self.model = joblib.load(os.path.join(current_dir, 'model.joblib'))

    def classify(self, file_content: str) -> str:
        """Classify a new document.

        Args:
            file_content: String content of the document

        Returns:
            Predicted class from CIVIL_FILE_CLASSES
        """
        X = self.vectorizer.transform([file_content])
        prediction = self.model.predict(X)[0]
        return prediction