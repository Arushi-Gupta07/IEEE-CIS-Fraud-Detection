# IEEE-CIS-Fraud-Detection

<img width="490" alt="image" src="https://user-images.githubusercontent.com/116758652/203837992-3e69f739-4898-411c-9148-93d3f9a6c0f5.png">

In recent years, the number of e-commerce users are getting increased day by day, and the scale of online transactions is also expanding exponentially. With the increase in number of banking transactions options, credit cards are becoming more widely used for transactions. Majority of people worldwide holding at least one credit card to do their daily life transactions without any hassle like limits on their spendings, time consuming process, and tracking monthlyexpenses unlike a cash payment methodas the credit card allows user to keep track of their spending and savings. But unfortunately, along with this trend the chances of getting cheated online with fraudulent transaction increased drastically over a period. The fraud criminals often use various channel to steal user’s card personal information using  password decoding tool and do online fraud by transferring a huge amount of money within notime, causing a lot of property losses to credit card user and companies, which  needs to be taken as serious problem and have some quick solution to predict fraudulent transactionin-order to save million dollars & the manual efforts and time to prevent from fraud transactions beforehand. Fraudulent transactions are usually a small probability events hidden in the large amount of data. Hence, finding the actual fraudtransactions with good accuracy is required for customersto have a good experience without any kind of inconvenience. So, to protect customers from their fund being misused and to prevent bank loss, let’s explore the Kaggle dataset and build a model to classify fraudulent and legit transactions.


Below is the brief overview about Kaggle dataset:

The data for this project broken into two files identity and transaction, which are joined by TransactionID. 
Not all transactions have corresponding identity information.
The data seems to be Highly imbalanced.

Files are present in csv format:
train_{transaction, identity}.csv - The training data set
test_{transaction, identity}.csv - The test set data (we need to predict the isFraud value for these test observations)

Modelling -

Best auc is given by LGBM model


<img width="479" alt="image" src="https://user-images.githubusercontent.com/116758652/203846363-2367cf7b-a34c-423f-a235-9e1bd381b7c2.png">
<img width="479" alt="image" src="https://user-images.githubusercontent.com/116758652/203846025-ab56c169-4469-45f8-a800-9c007617c421.png">



Competition Link - https://www.kaggle.com/competitions/ieee-fraud-detection


Application Link - https://ml-fraudtransaction-api.herokuapp.com/


Medium Blog - https://medium.com/@iamarushigupta07/ieee-cis-fraud-detection-89dfeb10a104
