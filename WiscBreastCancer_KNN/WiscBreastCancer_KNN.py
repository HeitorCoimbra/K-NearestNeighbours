import pandas as pd
import numpy as np

# Converts each numerical data column to z-score to standardize the data.
def standardize_Dataframe(df):
    result = df.copy()
    
    for feature_name in df.columns:
        dtype=df[feature_name].dtypes
        # If the data type of the column is either integer or floating point.
        
        if dtype=='float64' or dtype=='int64':
            # Subtract each element by it's column's mean and divide the result by the standard deviation.
            mean = df[feature_name].mean()
            std = df[feature_name].std()
            result[feature_name] = (df[feature_name] - mean) / std
            
    return result
	
# Calculates the euclidian distance between two points, or individuals,
# by taking the square root of the sum of the squared differences of each feature.
def get_dist(obj1, obj2):
    distances=[]
    
    for i in range (30):
        distances.append(np.power(obj1[i+1]-obj2[i+1], 2))
        
    return np.sqrt(sum(distances))
	
# Analyzes an array of classes and distances and returns the most common class with the lowest k distances.
def get_best(k, arr):
    KNN = []
    arr.sort(key=lambda x : x[1])
    
    for i in range (k):
        KNN.append(arr[i][0])
        
    return max(set(KNN), key = KNN.count)

# Brings it all together. From a given odd integer K and a new object (individual), predicts it's class (diagnosis).
def get_knn(k, obj):
    distances=[]
    
    for i in range (len(traindf.index)):
        distances.append([traindf.diagnosis[i], get_dist(obj, traindf.loc[i])])
        
    return get_best(k, distances)

# Reads the .csv file from the web
maindf = pd.read_csv("https://bit.ly/2XNmkTG")

# Deletes the unnecessary 'id' column
del maindf['id']

# Standardization and subdivision of the main dataframe into test and "train" dataframes
maindf = standardize_Dataframe(maindf)
traindf = maindf.iloc[:479]
testdf = maindf.iloc[479:].reset_index(drop=True)

# Display and analysis of the results obtained
Range=len(testdf.index)

#From my analysis, the optimal K-value is 9 as it maximizes the recall with high accuracy and no detriment in precision
for k in range (9,10):
    print ('K: '+str(k)+'\n')
    
    fpositives=0
    fnegatives=0
    tpositives=0
    tnegatives=0
    
    for m in range (Range):
        model_diagnosis = get_knn(k, testdf.loc[m])
        actual_diagnosis = testdf.loc[m]['diagnosis']
        #if m<15:
        #    print ("Previsão do Modelo: "+model_diagnosis)
        #    print ("Espécie Real:       "+actual_diagnosis+'\n')
        if(actual_diagnosis == model_diagnosis): 
            if(actual_diagnosis == 'B'): tnegatives = tnegatives + 1
            else: tpositives = tpositives + 1
        else: 
            if(model_diagnosis == 'B'): fnegatives = fnegatives + 1
            else: fpositives = fpositives + 1
                
    mistakes = fpositives + fnegatives
    correct_guesses = tnegatives + tpositives
    total = correct_guesses + mistakes
    accuracy = round(100*(correct_guesses/total))
    precision = round(100*(tpositives/(tpositives + fpositives)))
    recall = round(100*(tpositives/(tpositives + fnegatives)))
    
    print('Total:           '+str(total)+'\n')
    print('Correct Guesses: '+str(correct_guesses))
    print('True Positives:  '+str(tpositives))
    print('True Negatives   '+str(tnegatives)+'\n')
    print('Mistakes:        '+str(mistakes))
    print('False Positives: '+str(fpositives))
    print('False Negatives  '+str(fnegatives)+'\n')
    print('Precision:       '+str(precision)+'%')
    print('Recall:          '+str(recall)+'%')
    print('Accuracy:        '+str(accuracy)+'%\n')