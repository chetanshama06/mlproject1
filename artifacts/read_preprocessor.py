import pickle
import os

file_path = os.path.join("artifacts", "preprocessor.pkl")

if os.path.exists(file_path):
    with open(file_path, "rb") as f:
        preprocessor = pickle.load(f)

    print("Preprocessor Loaded Successfully")
    print("Type:", type(preprocessor))
    print("Content:\n", preprocessor)
else:
    print("preprocessor.pkl not found at", file_path)
