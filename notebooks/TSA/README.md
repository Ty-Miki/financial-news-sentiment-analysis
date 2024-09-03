# Time series analysis

- Time series analysis examines data collected at regular intervals over a defined timespan. This method focuses on studying patterns in sequentially ordered observations, rather than analyzing sporadic or arbitrarily gathered data points. By consistently recording measurements at set time intervals, analysts can identify trends, cycles, and other temporal characteristics within the dataset.
- I have performed the TSA on the raw data using the headline counts as the variable of concern.

## Steps for TSA on the raw data

### 1. Loading the data

- First I loaded the raw data from the specified CSV file into a Pandas DataFrame. The file path is relative, meaning it looks for the file in a directory one level above the current working directory, inside the `data` folder.
  - `file_path = '../data/raw_analyst_ratings.csv'`
  - `df = pd.read_csv(file_path)`

### 2. Counting headlines per day

- Here, I grouped the data by the `date` column and counts the number of headlines per day.
- I have used the `size()` function to return the count of occurrences for each date, resulting in a time series of headline counts.
  - `daily_headlines = df.groupby('date').size()`

### 3. Creating a DataFrame for Time Series Analysis

- Next I converted the grouped data into a DataFrame suitable for time series analysis. The index is set to `Date`, making it easier to perform operations like **decomposition**, **plotting**, and further analysis.
  - ` time_series_data = pd.DataFrame({'Date': daily_headlines.index, 'Headlines_Count': daily_headlines.values})`
  - `time_series_data.set_index('Date', inplace=True)`

### 4. Seasonal decomposition of Time Series

- Here, I used the `seasonal_decompose` function to decomposes the time series into three components:

  - **Trend**,
  - **Seasonal**, and
  - **Residual** or I**rregular**.
    - `decomposition = seasonal_decompose(time_series_data['Headlines_Count'], model='additive', period=4)`
- *The `model='additive'` parameter assumes that these components are additive, meaning that the observed data is the sum of the trend, seasonal, and residual components.*
- *The `period=4` parameter specifies the periodicity of the seasonal component.*

### 5. Plotting the Decomposed Components

- Here, I have created a series of plots to visualize the original time series and its decomposed components:
  - `plt.figure(figsize=(15, 10))`

#### 5.1 Original plot

- The first subplot shows the original time series data (`Headlines_Count`), which is the daily count of headlines.
  - `plt.subplot(511)`
  - `plt.plot(time_series_data['Headlines_Count'], label='Original', color='blue')`
  - `plt.legend(loc='upper left')`
  - `plt.title('Original Time Series')`

#### 5.2 Trend componeny plot

- The second subplot shows the trend component, which captures the long-term movement in the data.
  - `plt.subplot(512)`
  - `plt.plot(decomposition.trend, label='Trend', color='green')`
  - `plt.legend(loc='upper left')`
  - `plt.title('Trend Component')`

#### 5.3 Seasonal component plot

- The third subplot shows the seasonal component, which captures periodic fluctuations in the data.
  - `plt.subplot(513)`
  - `plt.plot(decomposition.seasonal, label='Seasonal', color='orange')`
  - `plt.legend(loc='upper left')`
  - `plt.title('Seasonal Component')`

#### 5.4 Residual/Irregular component plot

- The final subplot shows the residual component, which represents the random noise or irregular variations in the data.
  - `plt.subplot(414)`
  - `plt.plot(decomposition.resid, label='Residual/Irregular', color='red')`
  - `plt.legend(loc='upper left')`
  - `plt.title('Residual/Irregular Component')`

*The `plt.tight_layout()` function ensures that the subplots are spaced out neatly without overlapping.*

## Simulating the data for validation

- Next I have generated the simulated headline count data for the purpose of testing and validating the decomposition process.
- I used a **Poisson distribution** to generate random headline counts with a mean of 5 per day, for the dates ranging from `January 1, 2023, to May 1, 2023`.
  - `np.random.seed(0)`
  - `dates = pd.date_range(start="2023-01-01", end="2023-02-01", freq='D')`
  - `headline_counts = np.random.poisson(lam=5, size=len(dates))`
  - `simulated_data = pd.DataFrame({'Date': dates, 'Headlines_Count': headline_counts})`
  - `simulated_data.set_index('Date', inplace=True)`
- Then I used the same decomposition as the original data and plotted the different components of the simulated data.

## How to Run the Notebook

1. Ensure all required libraries are installed. Use `pip install -r requirements.txt` if a `requirements.txt` file is provided.
2. Open the Jupyter Notebook.
3. Run each cell sequentially to perform the analysis.
