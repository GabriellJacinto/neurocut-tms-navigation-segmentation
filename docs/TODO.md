# TODO: Neurocut Project Roadmap

A checklist to track the main deliverables and tasks for the brain MRI segmentation project.

## 1. Problem Understanding & Data Collection
- [x] Study basics of brain MRI segmentation
- [x] Download and explore datasets (IBSR, BraTS subset, MNI template)
- [x] Standardize data format (e.g., NIfTI `.nii.gz`)
- [x] Create a small sample subset for prototyping
- [x] Document image formats, segmented structures, and resolutions

## 2. Preprocessing Implementation
- [x] Implement Z-score intensity normalization
- [x] Apply N4ITK bias correction (SimpleITK)
- [x] Implement histogram equalization (OpenCV or scikit-image)
- [x] Apply noise reduction (Gaussian filter, anisotropic diffusion)
- [x] Save preprocessed images
- [/] Visualize before/after for each technique
- [/] Write a short report on preprocessing impact

## 3. Classical Segmentation Pipeline
- [x] Implement Otsu thresholding
- [x] Implement Watershed segmentation with automatic markers
- [x] Implement K-means clustering (scikit-learn)
- [x] Apply mathematical morphology for refinement
- [x] Compare classical methods visually (at least 3 samples)
- [x] Document code in notebooks/scripts
- [x] Compute initial metrics (e.g., percentage of voxels segmented)

## 4. Evaluation of Classical Methods
- [x] Calculate Dice Coefficient
- [ ] Calculate Hausdorff Distance
- [ ] Calculate Volume Similarity
- [ ] Visualize overlay of segmentation vs. ground truth
- [/] Create comparative metrics table
- [ ] Write qualitative analysis (strengths/weaknesses)
- [ ] Generate plots and overlay images

## 5. Deep Learning Segmentation (3D U-Net)
- [x] Set up MONAI, nnU-Net, or Segmentation Models 3D
- [x] Run inference with pre-trained weights (no training from scratch)
- [ ] Compare deep learning results visually with classical methods
- [ ] Generate segmentations using deep learning
- [ ] Create notebook/script for batch inference
- [ ] Side-by-side visual comparison

## 6. Results Evaluation & Comparison
- [ ] Recalculate quantitative metrics for both approaches
- [ ] Generate comparative plots (bar plots, boxplots, heatmaps)
- [ ] Discuss runtime, robustness, interpretability
- [ ] Consolidate metrics table
- [ ] Write critical analysis text

## 7. Interactive 3D Visualization
- [ ] Build a basic interface for segmentation exploration
- [ ] Use itkwidgets, vedo, nilearn.plotting, or napari
- [ ] Allow switching between methods and slices
- [ ] (Optional) Mark known anatomical regions
- [ ] Record a short demo video or GIF
- [ ] Capture screenshots for the report

## 8. Final Report & Presentation
- [ ] Write the technical report (introduction, methods, results, discussion)
- [ ] Prepare final presentation slides or poster
- [ ] Organize GitHub repository with code and examples
- [ ] Export final report as PDF

## Optional Extensions
- [ ] Simulate or mockup integration with InVesalius
- [ ] Implement fusion of multiple segmentation methods 