# AICUP2024-Generative-AI Navigation Information Competition for UAV Reconnaissance in Natural Environments I : Image Data Generation
## Environment
* Operating system: CentOS 7.8
* Programmimg language: Python 3.8.19
* Hardware: NVIDIA Tesla V100-PCIE-32GB
## create folder

    ./
    ├── river
    ├── road
## Intallation(conda environment)
Clone the repository in ./river and ./road respectively and move into the folder.

    git clone https://github.com/GengYunTien/AICUP2024-spring
    cd AICUP2024-spring
  
An environment can be created with all the Python dependencies.

    conda env create -f conda/environment.yml
  
## Data preparation
After the data preprocessing, place the training dataset `img` and `label_img` in `train_B` and `train_A`.

    ./river/AICUP2024-spring/dataset/cityscapes
    ├── train_A
    │   ├── TRA_RI_1000000.png
    │              .
    |              .
    |              .
    │   └── TRA_RI_1002159.png
    ├── train_B
    │   ├── TRA_RI_1000000.jpg
    |              .
    |              .
    |              .
    │   └── TRA_RI_1002159.jpg
    ├── test_A
    |   ├── PRI_RI_1000000.png
    |              . 
    |              .
    |              .
    |   └── PRI_RI_1000359.png
    └── test_B


        ./road/AICUP2024-spring/dataset/cityscapes
    ├── train_A
    │   ├── TRA_RO_1002160.png
    │              .
    |              .
    |              .
    │   └── TRA_RO_1004319.png
    ├── train_B
    │   ├── TRA_RO_1002160.jpg
    |              .
    |              .
    |              .
    │   └── TRA_RO_1004319.jpg
    ├── test_A
    |   ├── PRI_RO_100360.png
    |              . 
    |              .
    |              .
    |   └── PRI_RO_1000719.png
    └── test_B
## Training
* river


    python train.py --name RIVER --label_nc 0 --no_instance

* road


    python train.py --name ROAD --label_nc 0 --no_instance

The model parameter will be saved in `checkpoints` folder.
> latest_net_G.pth

> latest_net_D.pth

## Testing
for river

    python test.py --name RIVER --label_nc 0 --no_instance --how_many 360

for road

    python test.py --name ROAD --label_nc 0 --no_instance --how_many 360

## Acknowledgments
Our work is inspired by [pix2pixHD](https://github.com/NVIDIA/pix2pixHD) 
