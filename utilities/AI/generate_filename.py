import random
import string


def generate_filename():
    """
        Generate a random string for the filename
        (To avoid collision between files with the same filename)
    """
    all_chars = list(string.digits + string.ascii_letters)
    random.shuffle(all_chars)
    filename = './pyprojects-api/images/' + ''.join(all_chars) + ".jpg"

    return filename