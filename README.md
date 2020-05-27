# Train CIFAR10 with PyTorch

Training different architectures with [PyTorch](http://pytorch.org/) on the CIFAR10 dataset without any tricks i.e., auto-augmentation, cutout, droppath, dropout.

## Prerequisites
- Python 3.6+
- PyTorch 1.5+

## Accuracy
| Model             | Acc.        | FLOPS        | param        | training time|
| ----------------- | ----------- |
| [VGG16](https://arxiv.org/abs/1409.1556)              |       |
| [ResNet18](https://arxiv.org/abs/1512.03385)          | 95.59%      |
| [ResNet50](https://arxiv.org/abs/1512.03385)          | 93.62%      |
| [ResNet101](https://arxiv.org/abs/1512.03385)         | 93.75%      |
| [RegNetX_200MF](https://arxiv.org/abs/2003.13678)     | 94.24%      |
| [RegNetY_400MF](https://arxiv.org/abs/2003.13678)     | 94.29%      |
| [MobileNetV2](https://arxiv.org/abs/1801.04381)       | 94.43%      |
| [ResNeXt29(32x4d)](https://arxiv.org/abs/1611.05431)  | 94.73%      |
| [ResNeXt29(2x64d)](https://arxiv.org/abs/1611.05431)  | 94.82%      |
| [DenseNet121](https://arxiv.org/abs/1608.06993)       | 95.04%      |
| [PreActResNet18](https://arxiv.org/abs/1603.05027)    | 95.11%      |
| [DPN92](https://arxiv.org/abs/1707.01629)             | 95.16%      |

## Learning rate adjustment
The learning rate is adjusted by the consine learning schedular.

Resume the training with `python main.py --resume --lr=0.1`
