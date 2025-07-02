import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

img_path = Path("/home/orion23/Documents/repos/neurocut-tms-navigation-segmentation/data/raw/IBSR_01/images/analyze/IBSR_01_ana.img")
seg_path = Path("/home/orion23/Documents/repos/neurocut-tms-navigation-segmentation/data/raw/IBSR_01/segmentation/analyze/IBSR_01_seg_ana.img")

img = nib.load(str(img_path))
seg = nib.load(str(seg_path))
img_data = img.get_fdata()
seg_data = seg.get_fdata()
slice_z = img_data.shape[2] // 2

fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].imshow(np.rot90(img_data[:, :, slice_z]), cmap='gray')
ax[0].set_title("MRI T1 - Slice Axial (Centro)")
ax[0].axis('off')
ax[1].imshow(np.rot90(img_data[:, :, slice_z]), cmap='gray')
ax[1].imshow(np.rot90(seg_data[:, :, slice_z]), cmap='nipy_spectral', alpha=0.4)
ax[1].set_title("Segmentação Manual (43 Labels)")
ax[1].axis('off')
plt.tight_layout()
plt.savefig("ibsr01_mri_seg_overlay.png", dpi=300)
plt.show()
