#!/usr/bin/env python
# coding: utf-8

# In[11]:


from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from torchvision import models, transforms
from transformers import ViTForImageClassification
import torch
from PIL import Image
import os
import json


# In[12]:


# Initialize FastAPI
app = FastAPI()


# In[13]:


# Load the best model from prod_model directory
prod_model_path = "./prod_model/model.pth"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load classes
classes = ['dresses', 'tshirts_and_tops', 'jeans', 'jackets_and_blazers', 'coats', 'shirts_and_blouses']


# In[14]:


# Check model type (ResNet34 or ViT) and load accordingly
def load_model(model_path):
    # Load metadata
    metadata_path = os.path.join(os.path.dirname(model_path), "metadata.json")
    if not os.path.exists(metadata_path):
        raise ValueError("Metadata file is missing in production directory!")

    with open(metadata_path, "r") as f:
        metadata = json.load(f)

    model_name = metadata.get("model_name")
    if model_name == "ResNet34":
        model = models.resnet34(pretrained=False)
        model.fc = torch.nn.Linear(model.fc.in_features, len(classes))
    elif model_name == "ViT":
        model = ViTForImageClassification.from_pretrained(
            'google/vit-base-patch16-224-in21k', num_labels=len(classes)
        )
    else:
        raise ValueError(f"Unknown model type in metadata: {model_name}")

    model.load_state_dict(torch.load(model_path, map_location=device, weights_only=True))
    return model.to(device)

model = load_model(prod_model_path)
model.eval()

# Define image transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Prediction function
def predict(image: Image.Image):
    image_tensor = transform(image).unsqueeze(0).to(device)
    outputs = model(image_tensor)
    if isinstance(outputs, torch.Tensor):  # ResNet34
        _, predicted = torch.max(outputs, 1)
    else:  # ViT
        _, predicted = torch.max(outputs.logits, 1)
    return classes[predicted.item()]

# Endpoints
@app.post("/predict")
async def predict_category(file: UploadFile = File(...)):
    try:
        # Load the image
        image = Image.open(file.file).convert("RGB")
        category = predict(image)
        return {"predicted_category": category}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/health")
def health_check():
    return {"status": "ok"}


# In[ ]:




