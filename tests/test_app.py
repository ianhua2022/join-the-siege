from io import BytesIO
import pytest
from werkzeug.datastructures import FileStorage

from src.app import app
from src.validator import is_allowed_file
from src.classifiers.civil.civil_classifier import CivilClassifier
from src.classifiers.finance.finance_classifier import FinanceClassifier
from src.classifiers.classifier import get_file_content


@pytest.fixture
def client():
    """Test client fixture."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


MIME_TYPE_TEST_CASES = [
    ("application/pdf", True),
    ("application/msword", True),
    ("application/vnd.openxmlformats-officedocument.wordprocessingml.document", True),
    ("application/vnd.ms-excel", True),
    ("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", True),
    ("application/vnd.ms-powerpoint", True),
    ("application/vnd.openxmlformats-officedocument.presentationml.presentation", True),
    ("text/plain", True),
    ("image/jpeg", True),
    ("image/png", True),
    ("image/gif", True),
    ("image/bmp", True),
    ("image/webp", True),
    ("image/svg+xml", True),
    ("audio/mpeg", False),
    ("audio/wav", False),
    ("audio/midi", False),
    ("audio/ogg", False),
    ("audio/x-m4a", False),
    ("video/mp4", False),
    ("video/mpeg", False),
    ("video/x-msvideo", False),
    ("video/quicktime", False),
    ("video/webm", False),
    ("application/zip", False),
    ("application/x-rar-compressed", False),
    ("application/x-7z-compressed", False),
    ("application/x-tar", False),
    ("application/gzip", False),
    ("application/octet-stream", False),
]


@pytest.mark.parametrize("mime_type, expected", MIME_TYPE_TEST_CASES)
def test_validator(mime_type, expected):
    """Test file type validation."""
    file = FileStorage(
        stream=BytesIO(b"test content"),
        filename="test.file",
        content_type=mime_type
    )
    assert is_allowed_file(file) == expected


def test_no_file_in_request(client):
    """Test API response when no file is provided."""
    response = client.post('/classify_file')
    assert response.status_code == 400


def test_no_selected_file(client):
    """Test API response when empty file is provided."""
    data = {'file': (BytesIO(b""), '')}
    response = client.post('/classify_file', data=data, content_type='multipart/form-data')
    assert response.status_code == 400


def test_success(client, mocker):
    """Test successful file classification."""
    mocker.patch('src.app.classify_file', return_value='test_class')

    data = {'file': (BytesIO(b"dummy content"), 'file.pdf')}
    response = client.post('/classify_file', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert response.get_json() == {"status": "success", "file_class": "test_class"}


def test_success_with_civil_classifier():
    """Test civil classifier with a driver's license image."""
    with open('tests/test_data/driving_licence_test.jpg', 'rb') as f:
        file_content = f.read()
        file = FileStorage(
            stream=BytesIO(file_content),
            filename='driving_license_test.jpg',
            content_type='image/jpeg'
        )
        civil_classifier = CivilClassifier()
        assert civil_classifier.classify(get_file_content(file)) == "driver licence"


def test_success_with_finance_classifier():
    """Test finance classifier with an invoice text file."""
    with open('tests/test_data/invoice_test.txt', 'rb') as f:
        file_content = f.read()
        file = FileStorage(
            stream=BytesIO(file_content),
            filename='invoice_test.txt',
            content_type='text/plain'
        )
        finance_classifier = FinanceClassifier()
        assert finance_classifier.classify(get_file_content(file)) == "invoice"