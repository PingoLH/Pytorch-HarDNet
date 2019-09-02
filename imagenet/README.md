## HarDNet models for ImageNet 

Training prodedure is branched from https://github.com/pytorch/examples/tree/master/imagenet

Training:
```
python main.py -a hardnet68 [imagenet-folder with train and val folders]

arch = hardnet39ds | hardnet68ds | hardnet68 | hardnet85
```

Evaluating:
```
python main.py -a hardnet68 --pretrained -e [imagenet-folder with train and val folders]
```
for HarDNet85, please download pretrained weights from [here](https://drive.google.com/file/d/1I-qbZtpVlWbRyz1c3lT7rg2IqxCl28at/view?usp=sharing)

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

[Detailed Results](https://github.com/PingoLH/Pytorch-HarDNet)
