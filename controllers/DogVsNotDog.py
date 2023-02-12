import os

from flask_restful import Resource

from utilities.AI.load_model import load_model
from utilities.AI.process_image import process_image
from utilities.AI.read_image import read_image


class DogVsNotDog(Resource):
    def post(self):
        # Read image
        image = read_image()

        if image:
            # Process image
            processed_image = process_image(image, 224)

            # Load model
            model = load_model("./pyprojects-api/models/20230207-98.37%-mn3-dogvsnotdog-801010.h5")

            # Predict the emotion of model
            prediction = model.predict(processed_image)

            # delete the image
            os.remove(image)
            
            # Return response as list.
            return prediction[0].tolist()
        else:
            return {"message": "Please upload a valid image", "success": False}