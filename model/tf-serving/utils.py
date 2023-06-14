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
    0: 'Amaranthus Viridis',
    1: 'Basella Alba',
    2: 'Piper Betle',
    3: 'Tabernaemontana Divaricata',
    4: 'Murraya Koenigii',
    5: 'Moringa Oleifera',
    6: 'Trigonella Foenum-graecum',
    7: 'Psidium Guajava',
    8: 'Hibiscus Rosa-sinensis',
    9: 'Pongamia Pinnata',
    10: 'Brassica Juncea',
    11: 'Artocarpus Heterophyllus',
    12: 'Muntingia Calabura',
    13: 'Syzygium Cumini',
    14: 'Jasminum',
    15: 'Carissa Carandas',
    16: 'Citrus Limon',
    17: 'Mangifera Indica',
    18: 'Plectranthus Amboinicus',
    19: 'Mentha',
    20: 'Azadirachta Indica',
    21: 'Nerium Oleander',
    22: 'Nyctanthes Arbor-tristis',
    23: 'Ficus Religiosa',
    24: 'Punica Granatum',
    25: 'Alpinia Galanga',
    26: 'Syzygium Jambos',
    27: 'Ficus Auriculata',
    28: 'Santalum Album',
    29: 'Ocimum Tenuiflorum'
}
 
    predictions = predictions[0]
    predicted_classes_with_probs = [
        {"species": class_indices[i], "probability": float(predictions[i])}
        for i in predicted_class_indices
    ]

    prediction_response =  predicted_classes_with_probs

    return prediction_response
