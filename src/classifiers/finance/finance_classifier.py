from ..industry_classifier import IndustryClassifier
import joblib
import os

FINANCE_KEYWORDS = [
    'bank', 'statement', 'invoice', 'income', 'expense',
    'profit', 'loss', 'balance', 'cash', 'credit', 'debit',
    'account', 'audit', 'tax', 'cost', 'revenue', 'loss'
]

FINANCE_FILE_CLASSES = ['bank statement', 'invoice']


class FinanceClassifier(IndustryClassifier):
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Load the pre-trained model and vectorizer
        self.vectorizer = joblib.load(os.path.join(current_dir, 'vectorizer.joblib'))
        self.model = joblib.load(os.path.join(current_dir, 'model.joblib'))
    
    def classify(self, file_content: str) -> str:
        """
        Classify a new document.

        Args:
            file_content: String content of the document.

        Returns:
            Predicted class from FINANCE_FILE_CLASSES.
        """
        # Transform new text using the same vectorizer
        X = self.vectorizer.transform([file_content])
        # Predict the class
        prediction = self.model.predict(X)[0]
        return prediction