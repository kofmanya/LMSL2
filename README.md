# ML Clothing Recognition Service

This repository contains an end-to-end ML service for recognizing clothing categories (dresses, t-shirts, jeans, jackets, coats, and shirts) from photos. The service uses a trained machine learning model deployed with a FastAPI backend and a client application for user interaction.

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
3. Access the FastAPI Swagger UI at:
   ```bash
   http://127.0.0.1:8000/docs
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
- Add more clothing categories.
- Enhance client application design.
- Set up monitoring and logging for live deployment.

---
