import pandas as pd
import src.preprocessing as preprocessing
import src.feature_Selection as FS
import src.data_analysis as Data_analysis
def main():
    df =  preprocessing.load_data("/home/rukaia/Desktop/client_ /organized_final/data/processed/final_Data.xlsx") ## pd.DataFrame is done in preprocessing file 
    df = preprocessing.preprocess_data(df)
    print(df.columns)
    y = df['categories']
    X = df.drop(['categories','Time','Serial Number'],axis= 1)
    # print(X)
    technique = "randomforest"
    selected_features = FS.feature_selection(X,y,technique)
    print(selected_features)
    print(f'selected features',selected_features.columns)
    #Data_analysis.Numerical_Feature_Distribution(selected_features)
    Data_analysis.Boxplot_Numerical_Features(selected_features)
if __name__ == "__main__":
    main()