from keras.callbacks import Callback
import numpy as np

from . import new_session
from . import log

class LeraCallback(Callback):
  def __init__(self):
    super(LeraCallback, self).__init__()

  def on_epoch_end(self, epoch, logs=None):
    self.send_metrics(logs)

  def on_epoch_begin(self, epoch, logs=None):
    #send('epoch', epoch + 1)
    pass

  def on_batch_begin(self, batch, logs=None):
    pass
  def on_batch_end(self, batch, logs=None):
    self.send_metrics(logs)

  def send_metrics(self, logs=None):
    if logs is not None:
      metrics = {}
      params = self.params['metrics']
      for k, v in logs.items():
        if k in params:
            metrics[k] = v
      log(metrics)

  def on_train_begin(self, logs=None):
    h = {}
    for key in ['epochs', 'batch_size']:
      if key in self.params:
        h[key] = self.params[key] 
    optimizer = self.model.optimizer
    config = optimizer.get_config()
    loss = self.model.loss 

    h["criterion"] = loss if isinstance(loss, str) else loss.__name__
    h["optimizer"] = optimizer if isinstance(optimizer, str) else optimizer.__class__.__name__
    for k,v in config.items():
      h[k] = v
    new_session(h)
  def on_train_end(self, logs=None):
      pass
