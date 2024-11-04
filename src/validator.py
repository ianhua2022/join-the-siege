from werkzeug.datastructures import FileStorage

ALLOWED_CATEGORIES = {'document', 'image'}

# Dictionary mapping MIME types to categories
MIME_CATEGORIES = {
    # Documents
    'application/pdf': 'document',
    'application/msword': 'document',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document': 'document',
    'application/vnd.ms-excel': 'document',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': 'document',
    'application/vnd.ms-powerpoint': 'document',
    'application/vnd.openxmlformats-officedocument.presentationml.presentation': 'document',
    'text/plain': 'document',
    
    # Images
    'image/jpeg': 'image',
    'image/png': 'image',
    'image/gif': 'image',
    'image/bmp': 'image',
    'image/webp': 'image',
    'image/svg+xml': 'image',
    
    # Audio
    'audio/mpeg': 'audio',
    'audio/wav': 'audio',
    'audio/midi': 'audio',
    'audio/ogg': 'audio',
    'audio/x-m4a': 'audio',
    
    # Video
    'video/mp4': 'video',
    'video/mpeg': 'video',
    'video/x-msvideo': 'video',
    'video/quicktime': 'video',
    'video/webm': 'video',
    
    # Archives
    'application/zip': 'archive',
    'application/x-rar-compressed': 'archive',
    'application/x-7z-compressed': 'archive',
    'application/x-tar': 'archive',
    'application/gzip': 'archive'
}

def categorize_file(file: FileStorage) -> str:
    """
    Categorize a file based on its MIME type.
    
    Args:
        file (FileStorage): The uploaded file object from Flask/Werkzeug
        
    Returns:
        str: Category of the file ('document', 'image', 'audio', 'video', 'archive', or 'unknown')
    """
    if not file or not isinstance(file, FileStorage):
        return False
        
    return MIME_CATEGORIES.get(file.content_type, 'unknown')

def is_allowed_file(file: FileStorage) -> bool:
    """
    Check if the uploaded file is allowed based on its category.
    
    Args:
        file (FileStorage): The uploaded file object from Flask/Werkzeug
        
    Returns:
        bool: True if the file category is allowed, False otherwise
    """
    return categorize_file(file) in ALLOWED_CATEGORIES
