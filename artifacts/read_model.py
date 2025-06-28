import pickle
import os

MODEL_PATH = os.path.join("artifacts", "model.pkl")

def load_model(path):
    with open(path, "rb") as file:
        model = pickle.load(file)
    return model

if __name__ == "__main__":
    if os.path.exists(MODEL_PATH):
        model = load_model(MODEL_PATH)
        print("Model loaded successfully!")
        print("Model object:", model)
    else:
        print("Model file not found at:", MODEL_PATH)
