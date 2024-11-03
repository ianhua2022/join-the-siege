from werkzeug.datastructures import FileStorage

def classify_file(file: FileStorage) -> str:
    """
    Classifies a file based on its filename.
    
    Args:
        file (FileStorage): The uploaded file object
        
    Returns:
        str: The classification of the file
    """
    CLASSIFICATIONS = {
        "drivers_license": "drivers_licence",
        "bank_statement": "bank_statement", 
        "invoice": "invoice"
    }

    filename = file.filename.lower()
    
    for keyword, classification in CLASSIFICATIONS.items():
        if keyword in filename:
            return classification
            
    return "unknown file"

