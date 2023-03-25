import pickle
import re
from pathlib import Path 

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/trained_pipeline-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)

def predict_pipeline(price_asking, bedrooms, bathrooms, parking, typeOf, sqft):
    predictedHousePrice = model.predict([price_asking, bedrooms, bathrooms, parking, typeOf, sqft])
    return predictedHousePrice