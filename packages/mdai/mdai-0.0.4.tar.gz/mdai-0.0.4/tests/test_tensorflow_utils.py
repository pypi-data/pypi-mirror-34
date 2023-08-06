import pytest
from utils import tensorflow_utils as ut
import tensorflow as tf

# TODO: for a small dataset, write to tfrecords, then validate with a decoder function

@pytest.fixture
def dataset():
    # TODO: create dataset object
    return d


def test_tfrecord_export(dataset):
    # write to tfrecord (as temporary file)

    tmpfile = None

    ut.write_to_tfrecords(tmpfile, dataset)

    # decode
    image_id, image, height, width, bboxes, label_text, label = decode_jpg(tmpfile)

    # check image_id, height, width, bboxes, label_text, label, etc
    assert image_id == 'test'
    assert height == 100


def test_decoder_jpg(n):
    count = 0

    filename_queue = tf.train.string_input_producer([VALID_OUTPATH], num_epochs=1)

    fetches = decode_jpg(filename_queue)

    coord = tf.train.Coordinator()
    with tf.Session() as sess:

        tf.global_variables_initializer().run()
        tf.local_variables_initializer().run()
        tf.train.start_queue_runners(sess=sess, coord=coord)

        try:
            while not coord.should_stop():
                outputs = sess.run(fetches)

                img_id = outputs[0]
                img = outputs[1]
                img_h = outputs[2]
                img_w = outputs[3]
                bboxes = outputs[4]
                label_text = outputs[5]
                label = outputs[6]

                if len(bboxes) >= 1:
                    print(img_id)
                    print(bboxes)
                    print(label_text)
                    print(label)
                    draw_box_on_image(img, bboxes, img_h, img_w)
                    plt.figure()
                    plt.imshow(img)

                    new_img_id = img_id[:-4].decode('ascii')
                    print(new_img_id)
                    fig = plt.figure()

                    original_image, gt_class_id, gt_bbox, gt_mask =\
                        vis.get_image_ground_truth(DATASET,
                                                   new_img_id,
                                                   label_ids_dict)

                    vis.display_annotations(original_image, gt_bbox,
                                            gt_mask, gt_class_id,
                                            class_text, ax=fig.gca())
                    count += 1
                    if count > n:
                        break

                    #return img, original_image
        except tf.errors.OutOfRangeError as e:
            pass


def decode_jpg(filename_queue):

    # Construct a Reader to read examples from the .tfrecords file
    reader = tf.TFRecordReader()
    _, serialized_example = reader.read(filename_queue)

    features = tf.parse_single_example(
        serialized_example,
        features={
            'image/height' : tf.FixedLenFeature([], tf.int64),
            'image/width' : tf.FixedLenFeature([], tf.int64),
            'image/filename' : tf.FixedLenFeature([], tf.string),
            'image/encoded' : tf.FixedLenFeature([], tf.string),
            'image/object/bbox/xmin' : tf.VarLenFeature(dtype=tf.float32),
            'image/object/bbox/ymin' : tf.VarLenFeature(dtype=tf.float32),
            'image/object/bbox/xmax' : tf.VarLenFeature(dtype=tf.float32),
            'image/object/bbox/ymax' : tf.VarLenFeature(dtype=tf.float32),
            'image/object/class/text': tf.VarLenFeature(dtype=tf.string),
            'image/object/class/label': tf.VarLenFeature(dtype=tf.int64)
        }
    )

    height = tf.cast(features['image/height'], tf.int32)
    width = tf.cast(features['image/width'], tf.int32)

    #image_shape = tf.stack([height, width, 3])
    image_shape = tf.stack([HEIGHT, WIDTH, 3])

    #image = tf.decode_raw(features['image/encoded'], tf.uint8)
    #image = tf.reshape(image, image_shape)

    image = tf.image.decode_jpeg(features['image/encoded'])
    image_id = features['image/filename']

    xmin = tf.expand_dims(features['image/object/bbox/xmin'].values, 0)
    ymin = tf.expand_dims(features['image/object/bbox/ymin'].values, 0)
    xmax = tf.expand_dims(features['image/object/bbox/xmax'].values, 0)
    ymax = tf.expand_dims(features['image/object/bbox/ymax'].values, 0)

    #num_bboxes = tf.cast(features['image/object/count'], tf.int32)
    label_text = features['image/object/class/text'].values
    label = features['image/object/class/label'].values

    bboxes = tf.concat(axis=0, values=[xmin, ymin, xmax, ymax])
    bboxes = tf.transpose(bboxes, [1, 0])

    return image_id, image, height, width, bboxes, label_text, label
