# IEEE-CIS-Fraud-Detection

<img width="270" alt="image" src="https://user-images.githubusercontent.com/116758652/203837379-9206df0a-dd1e-44e1-a895-9e0eb7897c5c.png">

The data for this project broken into two files identity and transaction, which are joined by TransactionID. 
Not all transactions have corresponding identity information.
The data seems to be Highly imbalanced.

Files are present in csv format:
train_{transaction, identity}.csv - The training data set
test_{transaction, identity}.csv - The test set data (we need to predict the isFraud value for these test observations)
