import matplotlib.pyplot as plt
import random
import math
import pandas as pd


def plot_infrences(actual_predicted_pairs, sample_size=100):
    """
    plot actual and predicted values curve
    :param actual_predicted_pairs:
    :param sample_size:
    """
    data_pairs_sample = random.sample(actual_predicted_pairs, sample_size)
    actual_data_sample = [pair[0] for pair in data_pairs_sample]
    train_pred_sample = [pair[1] for pair in data_pairs_sample]
    fig = plt.figure(figsize=(25, 12))
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(actual_data_sample, color='tab:blue', label="actual values")
    ax.plot(train_pred_sample, color='tab:orange', label="predicted values")
    plt.legend()


def model_inference(predictor, data: pd.DataFrame, output_label:str):
    """
    get the actual and predicted outputs in pair and calculate the mse
    :param predictor: autogluon predictor
    :param data: dat
    :param output_label:
    :return: list of (actual_value,predicted_value) pair
    """
    predictions = predictor.predict(data)
    actual_values = data[output_label]

    actual_predicted_pairs = list(zip(actual_values, predictions))
    squared_error_sum = 0.0
    for actual_value, train_perdiction in actual_predicted_pairs:
        squared_error_sum += (train_perdiction - actual_value) ** 2
    rmse = math.sqrt(float(squared_error_sum) / len(actual_predicted_pairs))
    print(f"root mean squared error = {round(rmse, 4)}")
    return actual_predicted_pairs, rmse
