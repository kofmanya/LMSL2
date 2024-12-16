
# ML Image Classifier
## LSMLS2. Final project. Kofman Anna.
![image_classifier](https://github.com/user-attachments/assets/c1cba538-2f9e-4138-8c91-147eb70204d6)
This repository contains an end-to-end ML service for recognizing clothing categories (dresses, t-shirts, jeans, jackets, coats, and shirts) from photos. The service uses a trained machine learning model deployed with a FastAPI backend and a client application for user interaction.

## Overview

This project focuses on building a machine learning service for recognizing clothing categories based on images. Here's an outline of our workflow:

1. **Dataset Preparation**:
   - We scraped the dataset from [zalando.ch](https://www.zalando.ch), gathering 1,000 images for each of the following categories:
     - Dresses
     - T-shirts
     - Jeans
     - Jackets
     - Coats
     - Shirts
   - *1_zalando_dataset_get_pages.ipynb* and *2_zalando_dataset_get_images.ipynb* were used for data scraping. 
   - The dataset was cleaned and labeled for training purposes with *3_prepare_dataset.ipynb*.
   - Due to the GitHub constraints, it's impossible to upload the dataset in this repository. You can upload the prepared dataset from Google Drive using this link: https://drive.google.com/file/d/1IMmKOuUBQqBzMN76NHuC4KFjj-a7IYf2/view?usp=sharing or call *4_upload_dataset.ipynb* script.

2. **Model Training**:
   - *5_LSML2_Final_Project_Kofman_Anna_model_trainer.ipynb* script trained two different models on the dataset:
     - **ResNet34**: Achieved an accuracy of 75.40% on the test set.
     - **ViT (Vision Transformer)**: Achieved an accuracy of 81.60% on the test set.
   - After evaluating the models, the **ViT model** was selected due to its superior performance.
   - Due to the GitHub constraints, it's impossible to upload the trained model in this repository. You can upload the trained model using this link: https://drive.google.com/drive/folders/1qAkUL4Q0dmuzKyS3FrdChe-dCqh91Pjn?usp=sharing and put it to a service/ direction. 

3. **Experiment Tracking**:
   - We used [Neptune.ai](https://neptune.ai/) for tracking model experiments and results.
   - The best-performing model (ViT) was exported and uploaded to the `service/prod_model` directory for production use.

4. **Service Deployment**:
   - The trained model is served using a **FastAPI** backend.
   - The service is containerized using **Docker** and orchestrated with **Docker Compose**.


## Features
- **Model**: A ViT model achieving 82.20% test set accuracy.
- **API**: A FastAPI-based service to accept image uploads and return predictions.
- **Client**: A web-based interface or bot for user interaction.
- **Deployment**: Docker Compose setup for seamless deployment.
- **Experiment Tracking**: Neptune integration for tracking model performance.
- **MLOps**: Full pipeline for serving and monitoring ML models.

## Architecture
- **Backend**: FastAPI handles requests and runs the trained ML model for inference.
- **Frontend/Client**: Interface for uploading images and receiving predictions.
- **Docker Compose**: Simplified deployment of both backend and client services.
- **Experiment Tracking**: Logs and metrics tracked using Neptune.

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
├── __pycache__/                           # Python cache files
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
