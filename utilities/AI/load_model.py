import tensorflow as tf
import tensorflow_hub as hub


def load_model(model_path):
  """
    Load the tensorflow model
  """
  model = tf.keras.models.load_model(model_path,
                                     custom_objects={"KerasLayer": hub.KerasLayer})
  return model