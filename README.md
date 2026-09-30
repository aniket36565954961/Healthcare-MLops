\# Healthcare ML Model Deployment on Kubernetes



This project demonstrates a simple MLOps workflow by deploying a machine learning model using FastAPI, Docker, and Kubernetes (Minikube).



\## Project Overview



The application predicts the risk of diabetes using a trained machine learning model based on patient health data.



\## Technologies Used



\- Python

\- Scikit-learn

\- FastAPI

\- Docker

\- Kubernetes

\- Minikube



\## Project Architecture



Dataset → Model Training → FastAPI API → Docker Container → Kubernetes Deployment → NodePort Service



\## Training the Model



Run:



python train.py



This generates the trained model file:



model.pkl



\## Run API Locally



Install dependencies:



pip install -r requirements.txt



Start API:



python -m uvicorn app:app --reload



Open:



http://127.0.0.1:8000/docs



\## Docker Build



docker build -t healthcare-ml .



Run container:



docker run -p 8000:8000 healthcare-ml



\## Kubernetes Deployment



Apply deployment:



kubectl apply -f deployment.yaml



Apply service:



kubectl apply -f service.yaml



Access service:



minikube service healthcare-ml-service



\## Example Prediction Request



POST /predict



{

&#x20;"Pregnancies": 6,

&#x20;"Glucose": 180,

&#x20;"BloodPressure": 90,

&#x20;"SkinThickness": 35,

&#x20;"Insulin": 200,

&#x20;"BMI": 40,

&#x20;"DiabetesPedigreeFunction": 0.8,

&#x20;"Age": 55

}



Response:



{

&#x20;"diabetes\_prediction": 1

}

