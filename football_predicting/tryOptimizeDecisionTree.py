import pandas as pd
import matplotlib.pyplot as plt

#import findspark
#import pyspark

from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id, lit, when

from pyspark.ml.classification import LogisticRegression, DecisionTreeClassifier, NaiveBayes, RandomForestClassifier
from pyspark.ml.feature import OneHotEncoder,StringIndexer,VectorAssembler
#from pyspark.ml.regression import LinearRegression, DecisionTreeRegressor
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

from pyspark.ml.stat import ChiSquareTest
from pyspark.sql.types import *

from google.cloud import bigquery
from google.cloud import storage
#from google.colab import auth
import numpy as np
import os

def EncodedData(matches, unused_cols, output_cols, encode_cols):
    #String Indexer
    indexer = StringIndexer(inputCols=encode_cols, outputCols = [encode_col+ "_Index" for encode_col in encode_cols])
    encoded_df = indexer.fit(matches).transform(matches)

    #OneHot Encoder
    encodeer = OneHotEncoder(inputCols=[encode_col+"_Index" for encode_col in encode_cols],
                             outputCols=[encode_col+"_Onehot" for encode_col in encode_cols])
    encoded_df = encodeer.fit(encoded_df).transform(encoded_df)

    #Lấy ra những cột bị Index
    indexed_cols = [encode_col +"_Index" for encode_col in encode_cols]

    #Những cột được assembled là những cột không nằm trong unused_cols và indexed_cols và encode_cols và output_cols
    vector_assembled_input_cols = [col for col in encoded_df.columns 
                                            if col not in unused_cols
                                            and col not in indexed_cols
                                            and col not in encode_cols
                                            and col not in output_cols
                                            ]
    assembler = VectorAssembler(inputCols=vector_assembled_input_cols,outputCol="Features")
    encoded_df = assembler.transform(encoded_df.select('*'))
    return encoded_df
def Reduce_Matches(matches_df):

    matches_df = matches_df.withColumn("id", monotonically_increasing_id())

    filtered_data = matches_df.filter(matches_df.id >= 20)
    filtered_data = filtered_data.drop("id")

    return filtered_data
def Train_Dataset(matches_df): 

    test_count = 30

    encoded_test_matches = matches_df.limit(test_count)
    encoded_train_matches = matches_df.subtract(encoded_test_matches)
    
    return encoded_train_matches

def Test_Dataset(matches_df): 

    test_count = 30

    encoded_test_matches = matches_df.limit(test_count)
    
    return encoded_test_matches
def Measure_Function(predictions, measure):

    evaluator = MulticlassClassificationEvaluator(labelCol="Label")

    measure_method = evaluator.evaluate(predictions, {evaluator.metricName: measure})

    return measure_method
def Model_Predictions(model, X_test):

    predictions = model.transform(X_test)
    
    return predictions
def LogisticRegression_Optimize_Func(matches_df, encoded_matches_label):
    df_measures = pd.DataFrame(columns = ['maxDepth', 'maxBins', 'minInstancesPerNode', 'impurity', 'accuracy'])

    for maxDepth in np.arange(3,10,2):
        for maxBins in np.arange(32, 70, 10):  
            for minInstancesPerNode in np.arange(1, 5, 1):
                for impurity in ['gini', 'entropy']:  
                    matches_df = encoded_matches_label
                    list_accuracy = []
                    for i in range(0,15):
                        print("i: ", i, "maxDepth: ", maxDepth, "maxBins: ", maxBins, "minInstancesPerNode: ", minInstancesPerNode, "impurity: ", impurity)
                        X_train = Train_Dataset(matches_df)

                        X_train = X_train.select('Features', 'Label')

                        X_test = Test_Dataset(matches_df)
                        X_test = X_test.select('Features', 'Label')

                        decisionTree = DecisionTreeClassifier(featuresCol = "Features", 
                                                            labelCol = "Label", 
                                                            maxDepth=5, 
                                                            maxBins=32, 
                                                            minInstancesPerNode=1, 
                                                            minInfoGain=0.0, 
                                                            maxMemoryInMB=256, 
                                                            cacheNodeIds=False, 
                                                            checkpointInterval=10, 
                                                            impurity="gini", 
                                                            seed=None)
                        decisionTree_model = decisionTree.fit(X_train)
                        predictions = Model_Predictions(decisionTree_model, X_test)
                        accuracy = Measure_Function(predictions, "accuracy")
                        list_accuracy.append(accuracy)
                        matches_df = Reduce_Matches(matches_df)
                    df_row_measure = pd.DataFrame([[maxDepth, maxBins, minInstancesPerNode, impurity, np.mean(list_accuracy)]], columns = ['maxDepth', 'maxBins', 'minInstancesPerNode', 'impurity', 'accuracy'])
                    df_measures = pd.concat([df_measures, df_row_measure],ignore_index=True)
                    if not os.path.exists('./measures'):
                        os.makedirs('./measures')
                    df_measures.to_csv('./measures/DecisionTree_Optimize.csv', index = False)
    return df_measures
#Áp dụng model trên tập test

            
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./keys/key.json"

project_id = 'kltn-cloud-420208'
bigQuery_client = bigquery.Client(project=project_id)
storage_client = storage.Client()

query_factMatchStatistics = """
SELECT * FROM `kltn-cloud-420208.Football_DataWarehouse.Fact_Match_Statistics`
"""
query_dimMatch = """
SELECT * FROM `kltn-cloud-420208.Football_DataWarehouse.Dim_Match`
"""

query_dimTeam = """
SELECT * FROM `kltn-cloud-420208.Football_DataWarehouse.Dim_Team`
"""
match_dataset_model_desc = pd.read_csv('gs://football-data-etl/football-data-predicting/match_dataset_model_desc.csv')

dataset_model = match_dataset_model_desc.copy()
list_result = ['Win' if home_score > away_score 
               else 'Draw' if home_score == away_score 
               else 'Lose' for home_score, away_score 
               in zip(dataset_model['Home_Score'], dataset_model['Away_Score'])]
dataset_model['Result'] = list_result
nan_rows = dataset_model.isna().sum(axis=1)
num_nan_rows = len(nan_rows[nan_rows > 0])
dataset_model[dataset_model.isna().any(axis=1)]
dataset_model = dataset_model[dataset_model['Match_Key'] != 10768]
dataset_model = dataset_model[dataset_model['Match_Key'] != 10753]

#attack_mid_defense = 0
dataset_model = dataset_model[(dataset_model['Home_Attack'] != 0) & 
                              (dataset_model['Home_Midfield'] != 0) & 
                              (dataset_model['Home_Defense'] != 0)]
dataset_model = dataset_model[(dataset_model['Away_Attack'] != 0) & 
                              (dataset_model['Away_Midfield'] != 0) & 
                              (dataset_model['Away_Defense'] != 0)]

spark = (SparkSession
         .builder
         .appName("Classifications Technique")
         .config("spark.executor.memory", "4g") \
        .config("spark.driver.memory", "4g") \
         .getOrCreate())

matches = spark.createDataFrame(dataset_model)
#Attributes không dùng tới
unused_cols = ['Match_Key', 'Match_Date', 'Home_Score', 'Away_Score']
#Output
output_cols = ['Result']
input_cols = [column for column in matches.columns 
              if column not in output_cols and column not in unused_cols]
encode_cols = ['Home_Team','Away_Team']


encoded_matches = EncodedData(matches,unused_cols,output_cols,encode_cols)
class_indexer = StringIndexer(inputCol = 'Result', outputCol = 'Label')

encoded_matches_label = class_indexer.fit(encoded_matches).transform(encoded_matches)

matches_df = encoded_matches_label #Spark DataFrame so we can use pass by value
df_measures = LogisticRegression_Optimize_Func(matches_df,encoded_matches_label)

if not os.path.exists('./measures'):
    os.makedirs('./measures')
df_measures.to_csv('./measures/DecisionTree_Optimize.csv', index = False)