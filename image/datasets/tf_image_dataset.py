import tensorflow as tf

class TFImageClassificationDataset(object):

    def __init__(self, data_dir, **kwargs):
        self.data_dir = data_dir
        self.h = kwargs.get('h')
        self.w = kwargs.get('w')
        self.batch_size = kwargs.get('batch_size')
        self.crop_prop = kwargs.get('crop_prop')
        self.preprocess_type=kwargs.get('preprocess_type', 'vgg')
        self.num_parallel_calls=kwargs.get('num_parallel_calls', 2)
        self._get_datasets()

    def _get_datasets(self):
        pass 
        

