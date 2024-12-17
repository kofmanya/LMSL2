
# ML Image Classifier
## LSML2. Final project. Kofman Anna.
![image_classifier](https://github.com/user-attachments/assets/c1cba538-2f9e-4138-8c91-147eb70204d6)
This repository contains an end-to-end ML service for recognizing clothing categories (dresses, t-shirts, jeans, jackets, coats, and shirts) from photos. The service uses a trained machine learning model deployed with a FastAPI backend and a client application for user interaction.

## Overview

This project delivers a machine learning service for image-based clothing classification. The development workflow includes the following steps:

1. **Dataset Preparation**:
   - The dataset was scraped from [zalando.ch](https://www.zalando.ch), comprising 1,000 images for each category:
     - Dresses
     - T-shirts
     - Jeans
     - Jackets
     - Coats
     - Shirts
   - Scripts `1_zalando_dataset_get_pages.ipynb` and `2_zalando_dataset_get_images.ipynb` were used to scrape the dataset, followed by cleaning and labeling through `3_prepare_dataset.ipynb`.
   - Due to GitHub's file size restrictions, the dataset is not included in this repository. The prepared dataset can be downloaded from [Google Drive](https://drive.google.com/file/d/1IMmKOuUBQqBzMN76NHuC4KFjj-a7IYf2/view?usp=sharing) or fetched using the `4_upload_dataset.ipynb` script.

2. **Model Training**:
   - The `5_LSML2_Final_Project_Kofman_Anna_model_trainer.ipynb` script trained two models:
     - **ResNet34**: Test set accuracy of 75.40%.
     - **ViT (Vision Transformer)**: Test set accuracy of 81.60%.
   - The ViT model was selected for deployment due to its higher accuracy.
   - The trained model is not included in this repository due to size constraints. It can be downloaded from [Google Drive](https://drive.google.com/drive/folders/1qAkUL4Q0dmuzKyS3FrdChe-dCqh91Pjn?usp=sharing) and placed in the `service/prod_model` directory.

3. **Experiment Tracking**:
   - Model training and evaluation were tracked using [Neptune.ai](https://neptune.ai/).
   - The best-performing ViT model was exported for deployment.
   - Neptune.ai screenshots:
     <img width="1685" alt="Screenshot 2024-12-17 at 14 04 52" src="https://github.com/user-attachments/assets/4353836d-076c-4a86-a952-e2f3b751f0ac" />
     <img width="1683" alt="Screenshot 2024-12-17 at 14 05 52" src="https://github.com/user-attachments/assets/2a18de39-39dc-460f-91dd-fd8e02a06f80" />
     <img width="1048" alt="Screenshot 2024-12-17 at 14 06 33" src="https://github.com/user-attachments/assets/76d61d6e-df61-412b-9644-1823f32cf0f6" />

4. **Service Deployment**:
   - The service leverages a **FastAPI** backend and is containerized using **Docker** and **Docker Compose** for easy deployment.

---

## Features

- **Model**: ViT model with 81.60% test set accuracy.
- **API**: FastAPI-based service for receiving image uploads and returning predictions.
- **Client**: Web-based interface for user interaction.
- **Deployment**: Docker Compose setup for seamless deployment.
- **Experiment Tracking**: Integration with Neptune.ai for logging and monitoring model performance.
- **MLOps**: A complete ML pipeline for serving and monitoring the deployed model.

---

## Architecture

- **Backend**: FastAPI processes incoming requests and performs model inference.
- **Frontend/Client**: A web application for uploading images and viewing predictions.
- **Docker Compose**: Orchestrates the backend and client services.
- **Experiment Tracking**: Logs and metrics are recorded using Neptune.ai.

---

## Setup Instructions

### Prerequisites

- Docker
- Docker Compose
- Python 3.9+

### Steps to Run
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```
2. Build and start the services using Docker Compose:
   ```bash
   docker-compose up --build
   ```
3. Access the Service:
   - **API**: Open a browser or use tools like `curl` or Postman to interact with the API at:
   ```bash
   http://localhost:8000/docs
   ```
   - **Client**: Access the client application at:
   ```bash
   http://localhost:5050
   ``` 

### Directory Structure
```
.
├── 1_zalando_dataset_get_pages.ipynb      # Notebook for scraping Zalando dataset pages
├── 2_zalando_dataset_get_images.ipynb     # Notebook for downloading Zalando images
├── 3_prepare_dataset.ipynb                # Notebook for dataset preparation
├── 4_upload_dataset.ipynb                 # Notebook for uploading prepared dataset
├── 5_LSML2_Final_Project_Kofman_Anna_model_trainer.ipynb  # Notebook for training the ML model
├── service/                               # Service-related files
│   ├── Dockerfile                         # Docker configuration for the service
│   ├── docker-compose.yml                 # Docker Compose configuration
│   ├── app.py                             # FastAPI backend logic
│   ├── client/                            # Client application for user interaction
│   │   ├── Dockerfile                     # Docker configuration for the client
│   │   ├── requirements.txt               # Python dependencies for the client
│   │   ├── web_client.py                  # Client logic for interacting with the backend
│   │   ├── static/                        # Static files for the client
│   │   │   ├── uploads/                   # Directory for uploaded images
│   │   └── templates/                     # HTML templates for the client
│   │       ├── index.html                 # Main client HTML page
│   ├── prod_model/                        # Directory for production-ready model
│   │   └── ... (model files)
│   ├── requirements.txt                   # Python dependencies for the backend 
└── README.md                              # Project documentation
```

## API Endpoints
- `POST /predict`: Upload an image and get a clothing category prediction.
- `GET /`: Health check endpoint.

## Future Improvements
- Improve model accuracy with additional training.
- Collect bigger dataset.
- Expose the service for searching the most similar product from Zalando based on uploaded photo.
- Enhance client application design.
- Set up monitoring and logging for live deployment.

## UI Secreenshots
<img width="1367" alt="Screenshot 2024-12-14 at 22 51 31" src="https://github.com/user-attachments/assets/fc2b6b5f-f532-4870-9554-dd8265fb6404" />
<img width="1400" alt="Screenshot 2024-12-14 at 22 50 57" src="https://github.com/user-attachments/assets/ad4933ff-a826-412c-9a77-6ae1f15bdd34" />


---
