from sklearn.datasets import make_blobs
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

filepath=''
def doKMeanAnalysis():
    filepath=input("Please enter the complete file path of csv file for which you want to do k-means analysis-Eg. C:\Users\Downloads\SampleData.csv ")
    demoprint(filepath)  


def demoprint(filepath):
    kvalue=input('Please enter k value:')
    df=pd.read_csv(filepath)
#df=df.drop('day',axis=1)
    cols = df.columns
    num_cols = df._get_numeric_data().columns
    num_cols
    categories=list(set(cols) - set(num_cols))
    df_tr=df
    df_tr = pd.get_dummies(df_tr, columns=categories)
    scalar =StandardScaler()
    scalar.fit(df_tr)
    scaled_features=scalar.transform(df_tr)
    df2=pd.DataFrame(scaled_features,columns=df_tr.columns)
    model=KMeans(n_clusters=int(kvalue),random_state=101)
    model=model.fit(df2)
    labels = model.labels_
    df_tr['clusters'] = labels
# analyze the clusters
    print('The mean values of each attribute are shown below for each cluster')
    print (df_tr.groupby('clusters').mean())

    features=list(df_tr.columns)
    print("In order to visualise...")
    print(features)
    xaxis=input("Enter feature for x axis from these available features listed above")
    yaxis=input("Enter feature for y axis from these available features listed above")
    sns.lmplot(xaxis, yaxis, 
           data=df_tr, 
           fit_reg=False, 
           hue="clusters",  
           scatter_kws={"marker": "D", 
                        "s": 100})
    plt.title(xaxis+" vs "+  yaxis)
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.show()

    print('now in the demo file,kvalue=',kvalue)
    answer=input("Do you wish to enter a new k-value for the same file(y/n)")
    if(str.lower(answer)=='y'):
        demoprint(filepath)
    else:
        doKMeanAnalysis()