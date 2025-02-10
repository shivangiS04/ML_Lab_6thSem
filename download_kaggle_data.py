import os
import kaggle

# Tell Kaggle where to find kaggle.json

# Authenticate manually (Optional, but can help)
kaggle.api.authenticate()

# Define dataset name
dataset = "samithsachidanandan/most-popular-1000-youtube-videos"

# Download dataset
kaggle.api.dataset_download_files(dataset, path="./", unzip=True)

print("Dataset downloaded successfully!")
