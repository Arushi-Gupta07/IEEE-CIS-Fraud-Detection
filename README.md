# IEEE-CIS-Fraud-Detection

<img width="490" alt="image" src="https://user-images.githubusercontent.com/116758652/203837992-3e69f739-4898-411c-9148-93d3f9a6c0f5.png">


The data for this project broken into two files identity and transaction, which are joined by TransactionID. 
Not all transactions have corresponding identity information.
The data seems to be Highly imbalanced.

Files are present in csv format:
train_{transaction, identity}.csv - The training data set
test_{transaction, identity}.csv - The test set data (we need to predict the isFraud value for these test observations)


Application Link - https://ieee-cis-fraud-predictionapi.herokuapp.com/
