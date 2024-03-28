import tensorflow as tf
import pandas as pd

# 定义TFRecord文件路径
tfrecord_file = "predict.tfrecord"

# 定义特征的名称和数据类型
feature_description = {
    "label": tf.io.FixedLenFeature([], tf.string),
    "comment": tf.io.FixedLenFeature([], tf.string),
}

# 定义解析函数
def _parse_function(example_proto):
    return tf.io.parse_single_example(example_proto, feature_description)

# 创建TFRecordDataset对象
dataset = tf.data.TFRecordDataset(tfrecord_file)

# 解析数据
parsed_dataset = dataset.map(_parse_function)

# 遍历解析后的数据
for example in parsed_dataset:
    print(example)