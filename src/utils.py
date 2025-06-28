import os
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path, obj):
    """
    Save a Python object to the given file path using pickle.
    """
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok=True)
    with open(file_path, 'wb') as file_obj:
        pickle.dump(obj, file_obj)

def evaluate_models(X_train, y_train, X_test, y_test, models: dict, params: dict):
    """
    Evaluate multiple models using GridSearchCV and return their R2 scores
    and the best trained model objects.
    """
    report = {}
    best_trained_models = {}

    for name, model in models.items():
        param_grid = params.get(name, {})
        gs = GridSearchCV(model, param_grid, cv=3, n_jobs=-1, scoring='r2')
        gs.fit(X_train, y_train)

        best_model = gs.best_estimator_
        best_trained_models[name] = best_model

        y_pred = best_model.predict(X_test)
        score = r2_score(y_test, y_pred)
        report[name] = score

    return report, best_trained_models
