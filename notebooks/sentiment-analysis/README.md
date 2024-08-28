# Sentiment analysis

- In this folder I have performed a more deeper sentiment analysis on the row data.

## Stpes to perform the sentiment analysis

### 1. Loading the data and making a copy of it

- After loading the dataset in-to a pandas dataframe I made a copy of the original data.

- `sentiment_data = df.copy()`

***Purpose:** To work on a copy of the original data, preserving the original DataFrame*

### 2. perform the sentiment analysis and inspect it

- Next, I created an instance of the `SentimentIntensityAnalyzer` class from the VADER tool.
  - `sia = SentimentIntensityAnalyzer()`
- Then I performed the sentiment analyis using the `SentimentIntensityAnalyzer` instance I created.
  - `sentiment_data['sentiment'] = sentiment_data['headline'].apply(lambda x: sia.polarity_scores(text=x)['compound'])`
    - *This line calculates the sentiment score for each headline in the `sentiment_data` DataFrame.*
    - *The `polarity_scores` method returns a dictionary with several sentiment scores (**positive, negative, neutral,** and **compound**).*
    - *The `compound` score is a normalized, weighted composite score that represents the overall sentiment of the text.*

### 3. Categorizing the sentiment scores

- Then I categorized the sentiment scores into four categories: **Very Negative**, **Negative**, **Neutral**, and **Positive**.
  - `sentiment_data['sentiment_category'] = pd.cut(sentiment_data['sentiment'], bins=[-1, -0.5, -0.0001, 0.5, 1], labels=['Very Negative', 'Negative', 'Neutral', 'Positive'])`
    - *The `pd.cut` function is used to bin the sentiment scores into these categories based on predefined intervals.*

***Purpose:** To categorize the sentiment scores into more understandable labels.*

### 4. Inspecting the catagorized sentiment scores

- Next, I used the `values_count()` method on the catagorized sentiment data to count the number of headlines that fall into each sentiment category.
  - `sentiment_data['sentiment_category'].value_counts()`

***Purpose:** To get a summary of how many headlines are classified as **Very Negative**, **Negative**, ***Neutral***, or ***Positive**.**

### 5. Inspecting the earliest and latest dates in the sentiment data

- Finally I used the `min()` and `max()` methods on the **date** column of the sentiment data to inspect the earliest and latest dates respectively.
  - `print(f'Earliest Date: {sentiment_data['date'].min()}')`
  - `print(f'Latest Date: {sentiment_data['date'].max()}')`

***Purpose:** To identify the time **range** covered by the dataset.*

## Performing sentiment analysis on common stocks

- I used the stocks column to capture data about some popular stocks like **Apple**, **Amazon**, **Google**, **NVIDIA, and Tesla.**
- The steps I used similar and here I will show a more generalized version of the steps I took.

### 1. Get the data for a specific stock

- `stock_data=sentiment_data[sentiment_data['stock'] =='STOCK_NAME']`

### 2. Inspect the catagorized sentiment score for that stock

- `stock_data['sentiment_category'].value_counts()`

### 3. Inspect the earliest and latest dates of the sentiemnt data for that stock

- `print(f'Earliest Date: stock_data['date'].max()}')`
- `print(f'Latest Date: {stock_data['date'].max()}')`
