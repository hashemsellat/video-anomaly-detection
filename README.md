

# Anomaly Dectection in Videos
## Objective
Video anomaly detection system with multiple algorithms, and real-time support.

## Help us make the project bigger
<form action="https://www.paypal.com/donate" method="post" target="_top">
<input type="hidden" name="hosted_button_id" value="35622GW3TFVTQ" />
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
<img alt="" border="0" src="https://www.paypal.com/en_CZ/i/scr/pixel.gif" width="1" height="1" />
</form>


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
