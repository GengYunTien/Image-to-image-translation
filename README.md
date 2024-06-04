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
* Clone the repository in ./river and ./road respectively and move into the folder:

    git clone https://github.com/GengYunTien/AICUP2024-spring
    cd AICUP2024-spring
* An environment can be created with all the Python dependencies:

    conda env create -f conda/environment.yml
## Data preparation
After the data preprocessing, place the training dataset 'img' and 'label_img' in ./dataset/cityscapes/train_A and ./dataset/cityscapes/train_B

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


## Testing

## Acknowledgments
Our work is inspired by [pix2pixHD](https://github.com/NVIDIA/pix2pixHD) 
