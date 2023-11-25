import pickle
import pandas as pd

pipe2 = pickle.load(open("random.pkl", "rb"))

input_df = pd.DataFrame(
    {
        "category": ["misc_net"],
        "state": ["NC"],
        "amt": [4.97],
        "zip": [28654.0],
        "lat": [36.0788],
        "long": [-81.1781],
        "city_pop": [3495.0],
        "merch_lat": [36.011003],
        "merch_long": [-82.048315],
        "age": [35.0],
        "hour": [0.0],
        "day": [1.0],
        "month": [1.0],
    }
)
print(input_df)
result = pipe2.predict(input_df)
print(result)
