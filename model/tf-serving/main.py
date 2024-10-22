import tensorflow as tf
from utils import predict_top_classes

# Load the pre-trained VGG19 model from .h5 file
# vgg19 = tf.keras.models.load_model('new_vgg_model.h5')

# # Convert the model to the SavedModel format
# export_path = '/home/rgrupesh/nHack/tf/model/1'
# tf.saved_model.save(vgg19, export_path)

image_path = 'lemon.jpg'
predicted_classes = predict_top_classes(image_path)
print('Top three predicted classes:', predicted_classes)
