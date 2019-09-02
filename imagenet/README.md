## HarDNet models for ImageNet 

Training prodedure modified from https://github.com/pytorch/examples/tree/master/imagenet

Training:
```
python main.py -a hardnet68 [imagenet-folder with train and val folders]
```

Evaluating:
```
python main.py -a hardnet68 --pretrained -e [imagenet-folder with train and val folders]
```

### Hyperparameters
- epochs 150 ~ 250
- initial lr = 0.05
- batch size = 256
- weight decay = 6e-5
- cosine learning rate decay
- nestrov = True

### Results

| Method | MParam | GMACs | Top-1 | 
| :---: | :---:  | :---:  | :---:  | 
| **HarDNet39DS** | 3.5  | 0.44 | 72.1 | 
| **HarDNet68DS** | 4.2  | 0.8  | 74.3 | 
| **HarDNet68**   | 17.6 | 4.3  | 76.5 | 
| **HarDNet85**   | 36.7 | 9.1  | 78.0 | 
