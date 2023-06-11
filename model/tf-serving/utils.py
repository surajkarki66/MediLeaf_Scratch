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
    0: 'Arive-Dantu - Scientific name: Amaranthus',
    1: 'Basale - Scientific name: Basella alba',
    2: 'Betel - Scientific name: Piper betle',
    3: 'Crape_Jasmine - Scientific name: Tabernaemontana divaricata',
    4: 'Curry - Scientific name: Murraya koenigii',
    5: 'Drumstick - Scientific name: Moringa oleifera',
    6: 'Fenugreek - Scientific name: Trigonella foenum-graecum',
    7: 'Guava - Scientific name: Psidium guajava',
    8: 'Hibiscus - Scientific name: Hibiscus rosa-sinensis',
    9: 'Indian_Beech - Scientific name: Pongamia pinnata',
    10: 'Indian_Mustard - Scientific name: Brassica juncea',
    11: 'Jackfruit - Scientific name: Artocarpus heterophyllus',
    12: 'Jamaica_Cherry-Gasagase - Scientific name: Syzygium cumini',
    13: 'Jamun - Scientific name: Syzygium cumini',
    14: 'Jasmine - Scientific name: Jasminum spp.',
    15: 'Karanda - Scientific name: Carissa carandas',
    16: 'Lemon - Scientific name: Citrus limon',
    17: 'Mango - Scientific name: Mangifera indica',
    18: 'Mexican_Mint - Scientific name: Plectranthus amboinicus',
    19: 'Mint - Scientific name: Mentha spp.',
    20: 'Neem - Scientific name: Azadirachta indica',
    21: 'Oleander - Scientific name: Nerium oleander',
    22: 'Parijata - Scientific name: Nyctanthes arbor-tristis',
    23: 'Peepal - Scientific name: Ficus religiosa',
    24: 'Pomegranate - Scientific name: Punica granatum',
    25: 'Rasna - Scientific name: Pluchea lanceolata',
    26: 'Rose_apple - Scientific name: Syzygium jambos',
    27: 'Roxburgh_fig - Scientific name: Ficus auriculata',
    28: 'Sandalwood - Scientific name: Santalum album',
    29: 'Tulsi - Scientific name: Ocimum tenuiflorum'
}

    
    predicted_labels = [class_indices[i] for i in predicted_class_indices]

    return predicted_labels