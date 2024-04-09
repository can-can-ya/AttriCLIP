# AttriCLIP

This is the pytorch version code of "AttriCLIP: A Non-Incremental Learner for Incremental Knowledge Learning" in CVPR2023.

## Content

- [AttriCLIP](#attriclip)
  - [Content](#content)
  - [Introduce of AttriCLIP](#introduce-of-attriclip)
  - [1. Environment](#1-Environment)
  - [2. Datasets](#2-Datasets)
  - [3. Pretrained CLIP](#3-Pretrained-CLIP)
  - [4. Train](#4-Train)

## [Introduce of AttriCLIP](#Content)

AttriCLIP is introduced from《AttriCLIP: A Non-Incremental Learner for Incremental Knowledge Learning》

Paper ：Runqi Wang, Xiaoyue Duan, Guoliang Kang, Jianzhuang Liu, Shaohui Lin, Songcen Xu, Jinhu Lv, Baochang Zhang. "Few-Shot Learning with Visual Distribution Calibration and Cross-Modal Distribution Alignment". In CVPR, 2023.

## [1. Environment](#Content)

```python
conda create -n AttriCLIP python=3.8
conda activate AttriCLIP
pip install torch==1.12.1+cu116 torchvision==0.13.1+cu116 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu116 (CUDA 11.6)
pip install -r requirements.txt
```

## [2. Datasets](#Content)

The test Datasets：CIFAR100, [Download link](https://www.cs.toronto.edu/~kriz/cifar-100-binary.tar.gz)  
Datasets size：100 classes and 32*32 pixels for each image. 

The test Datasets：a subset of ImageNet, [Download link](https://www.image-net.org/)  
Datasets size：100 classes. The chosen classes are shown in supplementary materials of the paper and dataset/imagenet100.py of this project.

Steps to prepare ImageNet100 Dataset:
Suppose in the path `'/NAS02/RawData'`
1. mkdir ILSVRC2012 && cd ILSVRC2012
2. wget https://image-net.org/data/ILSVRC/2012/ILSVRC2012_img_train.tar --no-check-certificate
3. wget https://image-net.org/data/ILSVRC/2012/ILSVRC2012_img_val.tar --no-check-certificate
4. wget https://image-net.org/data/ILSVRC/2012/ILSVRC2012_devkit_t12.tar.gz --no-check-certificate
5. mkdir train && tar -xvf ILSVRC2012_img_train.tar -C train && for x in `ls train/*tar`; do fn=train/`basename $x .tar`; mkdir $fn; tar -xvf $x -C $fn; rm -f $fn.tar; done
6. mkdir val && tar -xvf ILSVRC2012_img_val.tar -C ./val
7. tar -xzf ILSVRC2012_devkit_t12.tar.gz
8. Execute the `'AttriCLIP/dataset/unzip.py'` file to organize the pictures in the val folder. (Determine the path of `val_dir` and `devkit_dir`.)
9. Execute the `'AttriCLIP/dataset/extract_category.py'` file to create the subset of ImageNet, i.e., ImageNet100. (Determine the path of `train_dir`, `val_dir` and `output_dir`.)
10. cp ILSVRC2012_devkit_t12.tar.gz ../ILSVRC2012_100/ILSVRC2012_devkit_t12.tar.gz

## [3. Pretrained CLIP](#Content)

We use the pretrained CLIP model from [here](https://openaipublic.azureedge.net/clip/models/b8cca3fd41ae0c99ba7e8951adf17d267cdb84cd88be6f7c2e0eca1737a03836/ViT-L-14.pt)

Pre-training weight placement position: `path/ViT-L-16.pt`

## [4. Train](#Content)

```python
python main_incremental_sumbit.py --root /NAS02/RawData/ILSVRC2012_100 (your data_path)
```