from mlbootstrap.base import MlbtsBaseModule
import os


class AbstractModel(MlbtsBaseModule):
    def __init__(self):
        self.name = None
        self.tag = None
        self.dataset = None

    def set_model_name(self, name: str):
        self.name = name

    def set_tag(self, tag: str):
        self.tag = tag

    def model_dir(self):
        fullname = self.fullname()
        model_dir = self._config['model']['save_path']
        model_dir = os.path.join(model_dir, fullname)
        return model_dir

    def log_dir(self):
        fullname = self.fullname()
        log_dir = self._config['model']['log_path']
        log_dir = os.path.join(log_dir, fullname)
        return log_dir

    def fullname(self):
        fullname = self.name
        if self.tag:
            fullname += '-' + self.tag
        fullname += '_' + self._config['task']

        return fullname

    def train(self):
        raise NotImplementedError

    def evaluate(self):
        raise NotImplementedError

    def predict(self):
        raise NotImplementedError

    def set_dataset(self, dataset):
        self.dataset = dataset

    def set_visible_gpus(self):
        visible_gpus = self._config.get('gpu', None)
        if visible_gpus:
            os.environ['CUDA_VISIBLE_DEVICES'] = visible_gpus


class BasicModel(AbstractModel):
    def train(self):
        pass

    def evaluate(self):
        pass

    def predict(self):
        pass
