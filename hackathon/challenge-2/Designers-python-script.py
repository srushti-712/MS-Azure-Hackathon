import pandas as pd


def azureml_main(dataframe1= None, dataframe2 = None):
    scored_results= dataframe1[['age','Scored Labels', 'Scored Probabilities']]
    scored_results.rename(columns={'Scored Labels':'HeartDiseasePrediction', 'Scored Probabilities':'Probability'},
                            inplace=True)
    return scored_results