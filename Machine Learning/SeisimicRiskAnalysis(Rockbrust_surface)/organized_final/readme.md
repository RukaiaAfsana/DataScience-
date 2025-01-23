# project structure
SeismicPrediction/
│── data/                     # Raw & processed datasets
│   ├── raw/  
│   ├── processed/  
│── notebooks/                 # Jupyter notebooks for exploration
│── src/                       # Source code
│   ├── data_preprocessing.py  # Data cleaning & feature engineering
│   ├── feature_extraction.py  # Feature selection & transformation
│   ├── model_training.py      # Model training pipeline
│   ├── evaluation.py          # Model performance evaluation
│   ├── fragility_analysis.py  # 3D fragility curve computation
│── models/                    # Saved ML models
│── scripts/                   # Bash or Python scripts for automation
│── results/                   # Results & generated plots
│── config.yaml                # Configuration file
│── requirements.txt           # Dependencies
│── README.md                  # Documentation

# Data-Driven Machine Learning for Seismic Resilience Analysis of Rockburst Fragility Surfaces
Welcome to the **Seismic Resilience Analysis of Rockburst Fragility Surfaces*! This project aims to predict seismic risks of rockburst fragility surfaces by generating a 3D fragility curve. 

## 📋 Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Dataset](#dataset)
5. [Model Architecture](#model-architecture)
6. [Results](#results)
7. [Future Work](#future-work)
8. [Contributing](#contributing)
9. [License](#license)
10. [Open Source Code](#open-source-code)

## 🌍 Introduction
Rockbursts represent significant hazards in underground mining, tunnelling, and excavation endeavours, presenting serious risks to infrastructure, human safety, and operational effectiveness. Sudden and violent rock failures can lead to fatalities, considerable structural damage, loss of machinery, and interruptions in operations. The precise forecasting and examination of rockbursts are crucial for reducing their effects and guaranteeing the durability of subterranean aims in seismic environments. 
## 💻 Installation
To install and run this project locally, follow these steps:
1. Clone this repository to your local machine.
2. Install the required dependencies listed in the `requirements.txt` file using pip:
   ```bash
   pip install -r requirements.txt
    ```
3. Run the main script `main.py` to train the  model and make predictions.

## 🚀 Usage
After installing the necessary dependencies and running the main script, you can use the trained LSTM model to make earthquake magnitude predictions. Additionally, you can customize the model architecture and hyperparameters to improve prediction accuracy.

## 📊 Dataset
The dataset utilized in this project comprises historical earthquake records, encompassing attributes such as timestamp, geographic coordinates, depth, and magnitude. Prior to employment, the data undergoes preprocessing and partitioning into training and testing subsets for model training and assessment.


## 🧠 Model Architecture
The LSTM neural network architecture used in this project consists of multiple LSTM layers followed by dense layers for regression. The model takes sequential earthquake data as input and learns to predict the magnitude of future earthquakes.
## 📉 Results

The performance of the LSTM model is evaluated using the following metrics:

- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**
- **Mean Absolute Error (MAE)**

Additionally, the correlation coefficient between predicted and actual earthquake magnitudes is calculated to assess the model's performance.

<details>
<summary>View Results</summary>

| `Metric`                       | `Value`     |
|------------------------------|-----------|
| Mean Squared Error (MSE)     | 1.9480    |
| Root Mean Squared Error (RMSE)| 1.3957    |
| Mean Absolute Error (MAE)    | 1.3818    |

</details>

## 🔮 Future Work

There are several opportunities for future improvement and expansion of this project:

- Incorporating additional features such as seismic waveforms and geological data.
- Experimenting with different neural network architectures and hyperparameters.
- Developing a web-based application for real-time earthquake prediction and monitoring.

<details>
<summary>Contribute to Future Work</summary>

If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.


