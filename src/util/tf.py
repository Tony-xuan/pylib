try:
    import tensorflow as tf
except:
    print "tensorflow is not installed, util.tf can not be used."
def summary_image(image, bboxes = None, name='image', fmt = "bhwc"):
    """Add image with bounding boxes to summary.
    """
    if fmt == "bhw":
        image = tf.cast(image, tf.float32);
        image = tf.transpose(image, [1, 2, 0]);        
        image = tf.expand_dims(image, 0)
    
    if bboxes is not None:
        if len(bboxes.shape) == 2:
            bboxes = tf.expand_dims(bboxes, 0);
        image = tf.image.draw_bounding_boxes(image, bboxes)
    tf.summary.image(name, image)
    
def is_gpu_available(cuda_only=True):
  """
  code from https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/platform/test.py
  Returns whether TensorFlow can access a GPU.
  Args:
    cuda_only: limit the search to CUDA gpus.
  Returns:
    True iff a gpu device of the requested kind is available.
  """
  from tensorflow.python.client import device_lib as _device_lib

  if cuda_only:
    return any((x.device_type == 'GPU')
               for x in _device_lib.list_local_devices())
  else:
    return any((x.device_type == 'GPU' or x.device_type == 'SYCL')
               for x in _device_lib.list_local_devices())



def get_available_gpus():
    """
    code from http://stackoverflow.com/questions/38559755/how-to-get-current-available-gpus-in-tensorflow
    """
    from tensorflow.python.client import device_lib as _device_lib
    local_device_protos = _device_lib.list_local_devices()
    return [x.name for x in local_device_protos if x.device_type == 'GPU']


def get_latest_ckpt(path):
# tf.train.latest_checkpoint
    import util
    path = util.io.get_absolute_path(path)
    if util.io.is_dir(path):
        ckpt = tf.train.get_checkpoint_state(path)
        ckpt_path = ckpt.model_checkpoint_path
    else:
        ckpt_path = path; 
    return ckpt_path
    
def get_all_ckpts(path):
    ckpt = tf.train.get_checkpoint_state(path)
    all_ckpts = ckpt.all_model_checkpoint_paths
    ckpts = [str(c) for c in all_ckpts]
    return ckpts

def get_iter(ckpt):
    import util
    iter_ = int(util.str.find_all(ckpt, '.ckpt-\d+')[0].split('-')[-1])
    return iter_
