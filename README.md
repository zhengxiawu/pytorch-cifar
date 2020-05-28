# Train CIFAR10 with PyTorch

Training different architectures with [PyTorch](http://pytorch.org/) on the CIFAR10 dataset without any tricks i.e., auto-augmentation, cutout, droppath, dropout.

## Prerequisites
- Python 3.6+
- PyTorch 1.5+

## Accuracy
| Model             | Acc.        | FLOPS        | param        | training time (hours)|
| ----------------- | ----------- | -----------  | -----------  | -----------          |
| [Lenet](http://vision.stanford.edu/cs598_spring07/papers/Lecun98.pdf)|   77.56%    |0.65M | 0.06M | 0.63 |
| [googlenet](https://arxiv.org/pdf/1409.4842.pdf)      |   96.26%    |1529M | 6.16M | 6.16 |
| [Mobilenet](https://arxiv.org/pdf/1704.04861.pdf)     |   92.18%    |47M   | 3.21M | 0.85 |
| [MobilenetV2](https://arxiv.org/pdf/1801.04381.pdf)   |   93.81%    | 94M  | 2.296M| 1.95 |
| [ResNet18](https://arxiv.org/abs/1512.03385)          | 95.59%      | 556M |11.173M| 1.61 |
| [ResNet34](https://arxiv.org/abs/1512.03385)          | 95.32%      | 1161M|21.282M| 1.99 |
| [ResNet50](https://arxiv.org/abs/1512.03385)          | 95.74%      | 1304M|23.52M | 4.36 |
| [ResNet101](https://arxiv.org/abs/1512.03385)         | 95.43%      | 2520M|42.51M | 7.07 |
| [ResNet152](https://arxiv.org/abs/1512.03385)         | 95.91%      | 3736M|58.15M | 9.99 |
| [RegNetX_200MF](https://arxiv.org/abs/2003.13678)     | 94.24%      |
| [RegNetY_400MF](https://arxiv.org/abs/2003.13678)     | 94.29%      |
| [ResNeXt29(32x4d)](https://arxiv.org/abs/1611.05431)  | 94.73%      |
| [ResNeXt29(2x64d)](https://arxiv.org/abs/1611.05431)  | 94.82%      |
| [DenseNet121_Cifar](https://arxiv.org/abs/1608.06993) | 95.28%      | 128M | 1.0M | 2.46 |
| [DPN26](https://arxiv.org/abs/1707.01629)             | 95.64%      | 670M | 11.5M| 5.69 |
| [DPN92](https://arxiv.org/abs/1707.01629)             | 95.66%      |2053M | 34.2M|15.43 |
| [EfficientB0](https://arxiv.org/pdf/1905.11946.pdf)   | 93.24%      | 112M | 3.69M| 2.92 |

## Learning rate adjustment
The learning rate is adjusted by the consine learning schedular.

Resume the training with `python main.py --resume --lr=0.1`
