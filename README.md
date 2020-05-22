

# Anomaly Dectection in Videos
## Configurations
Create a new Config.py by copying Config.py.example, which contains the following parameters.
- **DATASET_PATH**: path to USCDped1/Train directory.
- **SINGLE_TEST_PATH**: the test sample you want to run.
- **RELOAD_DATASET**: boolean parameter. set to `True` if when reading the database the first time or `False` to read from cache.
- **RELOAD_TESTSET**: boolean parameter. set to `True` if when reading the test sample the first time or `False` to read from cache.
- **RELOAD_MODEL**: set to `True` if you want to re-train the model, `False` otherwise.
- **CACHE_PATH**: path to the cache file.
- **BATCH_SIZE** & **EPOCHS**: parameters for training the model.
- **MODEL_PATH**: the path to save the model.
## Evaluation
After putting the desired configurations, run evaluation.py to get the result of the chosed sample test after processed by the model.

## Notes
LSTM autoencoder which I used in my article only exists as a jupyter notebook in notebooks/lstmautoencoder. It'll be integrated with the project later.