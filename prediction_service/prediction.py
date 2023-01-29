import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model("model.h5")
img = Image.open("/config/workspace/artifacts/data_ingestion/PetImages/Dog/15.jpg")
img = img.resize((224,224))


img_array = np.array(img)
img_array = np.expand_dims(img_array, axis=0)

result = model.predict(img_array)

argmax_index = np.argmax(result, axis=1)
if argmax_index[0] == 0:
    print('predicted as: CAT')
else:
    print('predicted as: DOG')