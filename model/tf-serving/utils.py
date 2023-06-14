import requests
import json
import numpy as np
from tensorflow.keras.preprocessing import image
from flask import Flask, request, jsonify

app = Flask(__name__)

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
<<<<<<< HEAD
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
=======
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
>>>>>>> bde84ff2f38da0f96395dcfb2305bd6b8fd8b900
}
 
    predictions = predictions[0]
    predicted_classes_with_probs = [
        {"species": class_indices[i], "probability": float(predictions[i])}
        for i in predicted_class_indices
    ]

<<<<<<< HEAD
    prediction_response =  predicted_classes_with_probs

    return prediction_response
=======
    predicted_labels = [class_indices[i] for i in predicted_class_indices]

    return predicted_labels

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image found in the request'})

    image_file = request.files['image']
    image_file.save('input_image.jpg')

    predicted_classes = predict_top_classes('input_image.jpg')
    return jsonify({'predictions': predicted_classes})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> bde84ff2f38da0f96395dcfb2305bd6b8fd8b900
