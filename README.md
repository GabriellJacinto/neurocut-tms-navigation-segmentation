# Neurocut: Computer Vision for brain MRI segmentation in TMS navigation.

This project explores and compares classical computer vision techniques and deep learning approaches for brain structure segmentation in T1-weighted MRI scans. The goal is to build a modular and interpretable pipeline that supports both traditional methods (e.g., thresholding, watershed, morphology) and modern 3D convolutional networks (U-Net), focusing on accuracy, robustness, and visualization for neuro-navigation use cases such as Transcranial Magnetic Stimulation (TMS).

## Project Goals

- Implement and evaluate classical image processing techniques for brain MRI segmentation.
- Apply a pre-trained 3D U-Net model for anatomical structure extraction.
- Compare methods using quantitative metrics (Dice, Hausdorff, etc.).
- Visualize results in 3D and highlight practical use in clinical navigation scenarios.

## Folder Structure

```bash
Neurocut/
├── data/                
├── notebooks/            
├── src/                   
│   ├── classical/         
│   ├── deep_learning/    
│   ├── utils/             
├── results/               
├── figures/               
├── requirements.txt       
├── README.md              
└── docs/                
```

📁 data/ -> Datasets and preprocessed files
📁 src/ -> Modular source code (classical & DL)
📁 notebooks/ -> Prototyping and experimentation
📁 results/ -> Segmentations, plots, metrics
📁 docs/ -> Final report and documentation

## Requirements

Install dependencies via:

```bash
pip install -r requirements.txt
```