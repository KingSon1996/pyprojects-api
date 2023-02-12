from flask import request
from PIL import Image
from werkzeug.utils import secure_filename

from .generate_filename import generate_filename

ALLOWED_EXTENSIONS = set(['jpg', 'png', 'jpeg', 'webp', 'bmp', 'tiff', 'gif', 'jfif'])

def allowed_file(filename):
    """
        Only accept image files
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def read_image():
    """
        Read the image in request
    """
    image = request.files['image'] # Get image
    filename = secure_filename(image.filename) # Secure filename to avoid unexpected errors

    # Check if it's an image
    if allowed_file(filename):
        image = Image.open(image).convert('RGB') # Convert to Jpeg
        image_path = generate_filename() # Generate a filename (random characters)
        image.save(image_path, quality=95) # Save image

        return image_path # Return path
    else:
        return False