

# Anomaly Dectection in Videos
## Objective
Video anomaly detection system with multiple algorithms, and real-time support.

## Buy us a coffee
We have a lot of ideas and improvements to work on, and to make them a reality we need a massive amount of coffee and sugar, So if you are interested in supporting us, please send some money to the following bitcoin address:

bc1qt9fzr528fn0juqmlqnlqw2lcy4dvhwm4sg4za6

Or use QR code:

<img src="https://imgur.com/ciw2hJc.jpg" width="30%" height="30%"/>


## Currently Implemented Approaches
For each approach, there should be a jupyter notebook, evaluation support (taking a sample test and output whether it is anomaly or not), and real-time support.
<table style="width:100%;">
    <tr>
        <th>Approach</th>
        <th>Notebook Status</th>
        <th>Evaluation Support</th>
        <th>Real Time Support</th>
    </tr>
    <tr>
        <td><a href="http://arxiv.org/abs/1701.01546">STAE</a></td>
        <td>todo</td>
        <td>done</td>
        <td>todo</td>
    </tr>
    <tr>
        <td><a href="https://arxiv.org/abs/1604.04574">LSTM Autoencoder</a></td>
        <td>done</td>
        <td>todo</td>
        <td>todo</td>
    </tr>
</table>

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
