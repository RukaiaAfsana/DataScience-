import seaborn as sns
import matplotlib.pyplot as plt

def Numerical_Feature_Distribution(df):
    numeric_df = df.select_dtypes(include=['number'])
    figure_counter = 1 
    for col in numeric_df:
        sns.histplot(df[col], kde=True)
        plt.title(f"Distribution of {col}")
        plt.savefig(f"fig{figure_counter}: Distribution of {col}")
        plt.show()
        figure_counter += 1


def Boxplot_Numerical_Features(df):
    plt.figure(figsize=(12,6))
    sns.boxplot(data=df)
    plt.xticks(rotation=90)  # Rotate x-axis labels if necessary
    plt.tight_layout()
    plt.show()
