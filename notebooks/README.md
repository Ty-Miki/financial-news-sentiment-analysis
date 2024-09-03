# 1. Exploratory Data Analysis (EDA)

## 1.1 Data understanding

- Before performing any analysis, it's crucial to understand the structure and content of the data. This step involves loading the data, inspecting the first few rows, and identifying key features.
  - `import pandas as pd`
  - `file_path = 'Path_to_the_csv_file'`
  - `df = pd.read_csv(file_path)`
  - **`print(df.head())`** -*This line displays the first few rows.*

## 1.2 Descriptive statistics

- Descriptive statistics provide a summary of the central tendency, dispersion, and shape of the data distribution. For text data, this might include statistics like the length of headlines, the count of articles per publisher, and the distribution of publication dates.
  - *Claculate headline lengths,*
    - `df['headline_length'] = df['headline'].apply(len)`
  - *Basic statistics for headline lengths*
    - `headline_stats = df['headline_length'].describe()`
  - *Count the number of articles per publisher,*
    - `publisher_counts = df['publisher'].value_counts()`
  - *Analyze the publication dates,*
    - `df['date'] = pd.to_datetime(df['date'])`
    - `df['date'].describe()`

## 1.3 Text Analysis / Sentiment analysis

- Sentiment analysis aims to determine the sentiment behind the text, whether positive, negative, or neutral. Topic modeling identifies common topics or themes within the text.
  - *Perform sentiment analysis*
    - `from textblob import TextBlob`
    - `df['sentiment'] = df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)`
  - *Display sentiment statistics*
    - `df['sentiment'].describe()`

## 1.4 Time series analysis

- Time series analysis examines the data points indexed in time order. For this dataset, it involves analyzing publication trends over time, which can reveal insights into the frequency of articles during specific events.
  - *Resample data by day and count the number of articles*
    - `import matplotlib.pyplot as plt`
    - `df.set_index('date', inplace=True)`
    - `daily_articles = df['headline'].resample('D').count()`
  - *Plot the number of articles over time*
    - `plt.figure(figsize=(10, 5))`
    - `daily_articles.plot()`
    - `plt.title("Number of Articles Published Over Time")`
    - `plt.xlabel("Date")`
    - `plt.ylabel("Number of Articles")`
    - `plt.show()`
- *Detailed TSA is shown at `./TSA/TAS_headline.ipynb`*

## 1.5 Publisher analysis

- Publisher analysis involves examining the contributions of different publishers to the dataset. This can help identify which publishers are most active and the nature of the news they report.
  - Analyze the contribution of each publisher
    - `publisher_contribution = df['publisher'].value_counts(normalize=True) * 100`
  - Display the top contributors
    - `publisher_contribution.head()`

## How to Run the Notebook

1. Ensure all required libraries are installed. Use `pip install -r requirements.txt` if a `requirements.txt` file is provided.
2. Open the Jupyter Notebook.
3. Run each cell sequentially to perform the analysis.
