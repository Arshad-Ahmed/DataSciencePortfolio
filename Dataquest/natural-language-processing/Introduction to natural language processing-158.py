## 3. Tokenization ##

tokenized_headlines = []

tokenized_headlines = submissions["headline"].str.split(" ")

## 4. Preprocessing ##

punctuation = [",", ":", ";", ".", "'", '"', "’", "?", "/", "-", "+", "&", "(", ")"]
clean_tokenized = []
clean_tokenized = []
for item in tokenized_headlines:
    tokens = []
    for token in item:
        token = token.lower()
        for punc in punctuation:
            token = token.replace(punc, "")
        tokens.append(token)
    clean_tokenized.append(tokens)



## 5. Assembling a matrix ##

import numpy as np
unique_tokens = []
single_tokens = []

for i in clean_tokenized:
    ct = 0
    for j in i:
        ct += 1
    if ct > 1:
        single_tokens.append(j)
    else:
        unique_tokens.append(j)
        
        
counts = pd.DataFrame(0, index=np.arange(len(clean_tokenized)), columns=unique_tokens)

## 6. Counting tokens ##

# clean_tokenized and counts have been loaded in.

for i, item in enumerate(clean_tokenized):
    for token in item:
        if token in unique_tokens:
            counts.iloc[i][token] += 1

## 7. Removing extraneous columns ##

# clean_tokenized and counts have been loaded in.

word_counts = counts.sum()
filt = (word_counts >= 5) & (word_counts <= 100)
counts = counts.loc[:,filt]

## 9. Making predictions ##

from sklearn.linear_model import LinearRegression

clf = LinearRegression()

clf.fit(X_train,y_train)

predictions = clf.predict(X_test)



## 10. Calculating error ##

mse = sum((predictions-y_test)**2)/len(predictions)