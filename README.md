# RetinoAI: Advanced Diabetic Retinopathy Staging - A Deep Learning Method for Classifying Diabetic Retinopathy Stages

## Abstract
Diabetic retinopathy, a serious complication of diabetes that can lead to blindness if untreated, affects the retina's blood vessels and may have no early symptoms. Regular comprehensive dilated eye exams are crucial for early detection and treatment. However, accurate stage identification often requires expert analysis of fundus images, which is challenging and costly. To address this, we propose a deep learning-based method using convolutional neural networks (CNNs) for automatic diabetic retinopathy stage detection from single fundus photographs. Our approach also incorporates a multistage transfer learning technique to leverage similar datasets with varied labeling, offering a cost-effective screening solution for early detection.



## Understanding Diabetic Retinopathy: A Medical Overview
For a slight introduction to Diabetic Retinopathy, please refer to the document titled **"Diabetic Retinopathy: Medical Overview"**.
Diabetic Retinopathy progresses in 4 stages:
1. Mild non-proliferative retinopathy: the earliest stage, where only microaneurysms 
can occur.
2. Moderate non-proliferative retinopathy: a stage which can be described by losing 
the blood vessels’ ability of blood transportation due to their distortion and swelling 
with the progress of the Disease.
3. Severe non-proliferative retinopathy: results in deprived blood supply to the retina 
due to the increased blockage of more blood vessels, hence signaling the retina for 
the growing of fresh blood vessels; 
4. Proliferative diabetic retinopathy: It is the advanced stage, where the growth 
features secreted by the retina activate proliferation of the new blood vessels, 
growing along inside covering of retina in some vitreous gel, filling the eye.<br/>

Each stage has its characteristics and particular properties, so doctors possibly could 
not take some of them into account, and thus make an incorrect diagnosis. So this 
leads to the idea of creation of an automatic solution for DR detection.

## Problem Statement
This is a 5 Class Image Classification Task based on a Kaggle dataset 
from Eye Images (Aravind Eye hospital) - APTOS 2019 Challenge. The goal is to 
predict the Blindness Stage (0-4) class from the Eye retina Image using Deep 
Learning Models (CNN).
 The full dataset consists of 18590 fundus photographs, which are divided 
into 3662 training, 1928 validation, and 13000 testing images by organizers of 
Kaggle competition, each photography is of different resolution.
Here, we consider 5 stages of diabetic retinopathy:
3
1. No diabetic retinopathy (label 0)
2. Mild diabetic retinopathy (label 1)
3. Moderate diabetic retinopathy (label 2)
4. Severe diabetic retinopathy (label 3)
5. Proliferative diabetic retinopathy (label 4)

## Final Presentation of the project
A presentation summarizing the entire project is available in the file named **"RetinoAI_Final_PPT"** and project Report in the file named **"RetinoAI_Report"**.
