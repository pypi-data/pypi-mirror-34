# text-autoencoder
Various autoencoder for text data.

## Usage

### Grab one autoencoder first
```python
from text_autoencoder.variational_autoencoders import VAEXXX
model = VAEXXX(n_steps=..., latent_size=..., state_size=..., ...)
```

### How to train
- Warning: please preprocess your data to be a numpy array with shape (data_size, maxlen, embedding_size)
```python
model.fit(x=..., mask=..., epochs=10)
```

### How to save model
```python
model.save(output_path)
```

### How to get latent vector `z`
```python
model.get_latent_vector(x=..., mask=..., batch_size=1)
```

### How to get output of encoder
```python
model.encode(x=..., mask=..., batch_size=1)
```

### How to load a trained model
```python
model.load(path)
```

### How to monitor the training process
- get the output_dir you input when calling `model.fit`
- monitor training loss
```shell
> tensorboard --logdir="<output_dir>/summary/subtrain/"
```

- monitor validation loss
```shell
> tensorboard --logdir="<output_dir>/summary/valid/"
```
