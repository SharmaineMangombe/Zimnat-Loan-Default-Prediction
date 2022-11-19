import pandas as pd
import numpy as np

client_data = pd.read_csv('client_data.csv')
payment_history=pd.read_csv('payment_history.csv')
policy_data = pd.read_csv('policy_data.csv', parse_dates=['NP2_EFFECTDATE'])
train=pd.read_csv('train.csv')
sub=pd.read_csv('sample_sub.csv')

payment_history['DATEPAID'] = pd.to_datetime(payment_history['DATEPAID']).dt.year

policy_data['NP2_EFFECTDATE']= policy_data['NP2_EFFECTDATE'].dt.year

client_data.columns
payment_history.columns
policy_data.columns
train.columns


client_data=client_data[['Policy ID','NPH_TITLE', 'NPH_BIRTHDATE']]
payment_history=payment_history[['Policy ID','AMOUNTPAID', 'DATEPAID','PREMIUMDUEDATE']]
policy_data=policy_data[['Policy ID','NP2_EFFECTDATE','NPR_PREMIUM']]

policy_data['Lapse']=np.zeros(282815)

policy_data.isnull.sum()

payment_history=payment_history.sort_values(by='Policy ID')
policy_data=policy_data.sort_values(by='Policy ID')
train=train.sort_values(by='Policy ID')
policy_data=policy_data.sort_values(by='Policy ID')


Pivot = pd.read_csv('pivot.csv')


Pivot=pd.merge(Pivot,train,how='inner', on ='Policy ID')

Pivot['DATEPAID']=Pivot['DATEPAID'].astype(int)
policy_data.drop(['Policy ID'],axis=1, inplace=True)
policy_data.rename(columns={'NP2_EFFECTDATE':'DATEPAID',
                            'NPR_PREMIUM':'AMOUNTPAID'}, inplace= True)

Pivot.drop(['Policy ID','Lapse Year','PREMIUMDUEDATE'],axis=1, inplace=True)


Train=Pivot[Pivot['Lapse']=='1']
Test= Pivot[Pivot['Lapse']=='?']

Train=Train.replace('1', 1)

Train=pd.concat([Train,policy_data])


X=Train.iloc[:,:2]
Y=Train.iloc[:,2:]

from sklearn.utils import shuffle
Train = shuffle(Train)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 500, random_state=25)
classifier.fit(X, Y)

pred =classifier.predict(x_test )














    
