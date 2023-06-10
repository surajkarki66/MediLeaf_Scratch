import requests
import json
import numpy as np
from tensorflow.keras.preprocessing import image

def predict_top_classes(image_path):
    url = 'http://localhost:8601/v1/models/vgg_model:predict'

    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = x / 255.0
    x = np.expand_dims(x, axis=0)

    data = json.dumps({"instances": x.tolist()})

    response = requests.post(url, data=data)

    predictions = json.loads(response.text)['predictions']
    predicted_class_indices = np.argsort(predictions[0])[::-1][:3]

    class_indices = {
    0: 'Arive-Dantu',
    1: 'Basale',
    2: 'Betel',
    3: 'Crape_Jasmine',
    4: 'Curry',
    5: 'Drumstick',
    6: 'Fenugreek',
    7: 'Guava',
    8: 'Hibiscus',
    9: 'Indian_Beech',
    10: 'Indian_Mustard',
    11: 'Jackfruit',
    12: 'Jamaica_Cherry-Gasagase',
    13: 'Jamun',
    14: 'Jasmine',
    15: 'Karanda',
    16: 'Lemon',
    17: 'Mango',
    18: 'Mexican_Mint',
    19: 'Mint',
    20: 'Neem',
    21: 'Oleander',
    22: 'Parijata',
    23: 'Peepal',
    24: 'Pomegranate',
    25: 'Rasna',
    26: 'Rose_apple',
    27: 'Roxburgh_fig',
    28: 'Sandalwood',
    29: 'Tulsi'
}

    
    predicted_labels = [class_indices[i] for i in predicted_class_indices]

    return predicted_labels

image_path = 'lemon.jpg'
predicted_classes = predict_top_classes(image_path)
print('Top three predicted classes:', predicted_classes)
