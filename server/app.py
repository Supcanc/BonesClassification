from fastapi import FastAPI, HTTPException
import tensorflow as tf
import numpy as np
import uvicorn
import  os
from PIL import Image

app = FastAPI()

model = tf.keras.models.load_model('../models/model.keras')

@app.get('/predict/{images_path:path}')
def predict(images_path: str):
    images = []
    images_names = []
    classes = ['Non-Fractured', 'Fractured']

    try:
        for image_name in os.listdir(images_path):
            image_path = os.path.join(images_path, image_name)
            image = Image.open(image_path)
            image = image.resize((512, 512))
            images_names.append(image_name)
            images.append(np.array(image))

        images = np.array(images)

        predicted_probabilities = model.predict(images)
        predicted_classes = np.round(predicted_probabilities)

        with open('../predictions.txt', 'w') as f:
            for i in range(len(predicted_classes)):
                f.write(f'{i + 1}) Filename: {images_names[i]}\n'
                        f'Class: {classes[int(predicted_classes[i][0])]}\n'
                        f'Probability for fractured class: {round(float(predicted_probabilities[i][0] * 100), 2)}%\n\n')

        return {'status': 'Prediction completed.'}

    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

if __name__ == '__main__':
    uvicorn.run('server.app:app')