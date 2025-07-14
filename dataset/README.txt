## X-Ray Imaging Dataset for the Detection of Bone Integrity Fractured vs. Non-Fractured

#Description
This dataset comprises 9,000 images, evenly categorized into 2 distinct classes. It was developed for a computer vision thesis undertaken by postrgraduate students in Department of  Computer Science and Engineering. Netrokona University, Netrokona, Bangladesh. The collection features both original and augmented images, all uniformly resized to 512x512 pixels using high-quality LANCZOS interpolation to maintain visual clarity.

## Folder Structure
The dataset is organized into the following class folders:

-Fractured  
-Non-Fractured


Each folder contains:
- Original images (named like Healthy_0001.JPG)
- Augmented images (named like Healthy _001.jpg)

## Data Augmentation Techniques
To increase variability and robustness for machine learning models, the following augmentations were applied:
- Random Horizontal Flip
- Rotation up to ±20 degrees
- Color Jitter (brightness, contrast, saturation, hue)
- Random Resized Crop to 512x512

These transformations were applied using PyTorch's torchvision library.

## Image Format
- Format: JPG
- Size: 512x512 pixels
- Color Mode: RGB

## Use Case
This dataset is suitable for:
- Image classification tasks
- Transfer learning model fine-tuning
- Federated Learning
- Dataset augmentation research
- Student or academic thesis

## Authors

**Farhan Masud Nayem**  
Department of Computer Science and Engineering  
Netrokona University  
📧 farhan.masud.mn@gmail.com  
📱 01761826010  

**Co-authors:**

**Farida Siddiqi Prity**  
Department of Computer Science and Engineering  
Netrokona University  
📧 prity@neu.ac.bd  
📱 01877557081 

**Md. Maruful Islam Rafe**  
Department of Computer Science and Engineering  
Netrokona University  
📧 maruful.rafe.mr@gmail.com  
📱 01918927246 

**Arifur Rahman Arif** 
Department of Electrical and Electronic Engineering
Faridpur Engineering College
📧 mdarifurrahmanj@gmail.com
📱 01772441559 



## License
This dataset is shared under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. You are free to use, share, and adapt the dataset with proper attribution.

## Citation
If you use this dataset in your research or projects, please cite:
DOI: 10.17632/w8sw34p752.1

Thank you for using this dataset!
