import numpy as np
import tensorflow as tf


def process_image(image_path, image_size=300):
    """
    Takes an image file path and turns the image into a Tensor.
    """
    # Read in an image file
    image = tf.io.read_file(image_path)

    # Turn the jpeg image into numerical Tensor with 3 color channels
    image = tf.image.decode_jpeg(image, channels=3)

    # Convert the color channel values from 0-255 to 0-1 vales
    image = tf.image.convert_image_dtype(image, tf.float32)

    # Resize the image to our desired value (244, 244)
    image = tf.image.resize(image, size=(image_size, image_size))
    
    # Expand image dimension
    image = np.expand_dims(image, axis=0)
    
    return image
