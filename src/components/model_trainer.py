# src/components/model_trainer.py

from dataclasses import dataclass
import os
import pickle
from sklearn.linear_model import LogisticRegression

@dataclass
class ModelTrainerConfig:
    trained_model_path: str = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train_model(self, X_train, y_train):
        model = LogisticRegression()
        model.fit(X_train, y_train)
        with open(self.config.trained_model_path, "wb") as f:
            pickle.dump(model, f)
        return model

