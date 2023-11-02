from tflite_model_maker import model_spec
from tflite_model_maker import object_detector

import tensorflow as tf
assert tf.__version__.startswith('2')

tf.get_logger().setLevel('ERROR')
from absl import logging
logging.set_verbosity(logging.ERROR)

spec = model_spec.get("efficientdet_lite0")

classes = ["blue", "red"]

train_data = object_detector.DataLoader.from_pascal_voc("./train", "./train", classes)
validation_data = object_detector.DataLoader.from_pascal_voc("./valid", "./valid", classes)
test_data = object_detector.DataLoader.from_pascal_voc("./test", "./test", classes)

model = object_detector.create(train_data, model_spec=spec, epochs=20, validation_data=validation_data, train_whole_model=True, batch_size=8)
print(model.summary())

model.evaluate(test_data)

option = input("Export? (Y/n)")

if option != "n":
    print("Exporting...")
    model.export(export_dir=".")
