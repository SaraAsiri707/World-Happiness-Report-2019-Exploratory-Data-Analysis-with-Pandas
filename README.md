# World Happiness Report 2019 – Exploratory Data Analysis with Pandas

## 1. Dataset Overview

First, I loaded the World Happiness Report 2019 dataset using Pandas and `read_csv()`.

The dataset contains **156 rows and 9 columns**. Each row represents a country, and each column contains information about a different factor, such as happiness score, GDP per capita, social support, healthy life expectancy, freedom, generosity, and perceptions of corruption.

I used `head()` to view the first five rows, `info()` to check the data types and non-null values, and `shape` to find the number of rows and columns. I also used `describe()` to get some basic statistical information about the numerical columns.

After that, I checked for duplicate rows using `duplicated().sum()`. The result was 0, which means there were no completely duplicated rows.

I also checked for missing values using `isnull()` and `isnull().sum()`. The results showed that there were no missing values in the dataset.

## 2. Data Preparation and Exploration

I noticed that some column names contained spaces, which made them less convenient to use in my code. So, I used `rename()` to change some column names and make them easier to work with in Jupyter Notebook.

Then, I used `unique()` to explore the country names in the dataset. I also used `value_counts()` with `sort_index()` to check how often each happiness score appeared.

The dataset contains 156 different countries, and each country has one record. One happiness score appeared twice, but this does not mean there are duplicate rows.

## 3. Happiness Score Analysis

I started by exploring the happiness scores using some basic statistical methods:

- `mean()` to calculate the average happiness score for all countries. The result was approximately **5.407**.
- `min()` to find the lowest happiness score, which was **2.853**.
- `max()` to find the highest happiness score, which was **7.769**.

The results showed that Finland had the highest happiness score, while South Sudan had the lowest score in the report.

I also used `groupby()` with `mean()` to calculate the average happiness score for each country. Then, I used `sort_values(ascending=False)` to sort the countries from the highest score to the lowest.

Since each country has only one record, its average score is the same as its original score.

## 4. Exploring and Selecting Countries

I used `loc` and `iloc` to select specific rows and columns from the dataset.

I also used `isin()` to find information about specific countries, such as Saudi Arabia and Bahrain.

To select countries based on more than one condition, I used `loc` with comparison operators and the `&` operator. For example, I selected countries with a happiness score of 5 or more and social support of 1.50 or more.

These methods helped me find and compare information about different countries.

## 5. Saudi Arabia Comparison

I focused on Saudi Arabia to see its position compared to the other countries.

According to the 2019 data, Saudi Arabia had:

- **Overall Rank:** 28
- **Happiness Score:** 6.375

I compared Saudi Arabia's happiness score with the overall average, which was approximately 5.407.

Saudi Arabia's score was higher than the overall average by about **0.968 points**.

This means Saudi Arabia scored above the average happiness level in the 2019 report and ranked 28th out of 156 countries, placing it in the upper half of the ranking.

## 6. Exploring Different Happiness Factors

After that, I explored the other factors in the dataset to find which countries had the highest values.

I used `idxmax()` to find the country with the highest value in each column:

- Highest GDP per capita: Qatar.
- Highest freedom score: Uzbekistan.
- Highest social support score: Iceland.
- Highest perceptions of corruption value: Singapore.

I also used `agg()` to calculate the mean, minimum, and maximum values for several columns at the same time.

Finally, I used `dtypes` to check the data types of all columns.

## 7. Mean Centering

I used a method called **Mean Centering** to calculate the difference between each value and the overall average.

For the happiness score, I used `map()` with `lambda` to subtract the average happiness score from each country's score.

The results helped me identify which countries had scores above or below the average:

- A positive value means the country's score is above the average.
- A negative value means the country's score is below the average.
- A value close to zero means the score is close to the average.

I applied the same idea to social support using `apply()` and a custom function. I subtracted the average social support value from each country's value.

This helped me understand how each country compares to the overall average.

## 8. Correlation Analysis

In the final part, I used `corr()` to explore the relationship between happiness scores and other numerical factors.

The results showed a strong positive correlation between GDP per capita and happiness score, with a correlation value of approximately **0.794**.

I also used `corr(numeric_only=True)` to create a correlation matrix and explore the relationships between all numerical columns.

The correlation values with happiness score were:

- GDP per capita: 0.794
- Healthy life expectancy: 0.780
- Social support: 0.777
- Freedom to make life choices: 0.567
- Perceptions of corruption: 0.386
- Generosity: 0.076

These results show that GDP per capita had the strongest positive correlation with happiness score, followed by healthy life expectancy and social support.

Generosity had a very weak positive correlation with happiness score.

## 9. Correlation vs. Causation

It is important to understand the difference between correlation and causation when analyzing data.

**Correlation** means that two variables are statistically related. For example, the results showed a positive relationship between GDP per capita and happiness score. This means that countries with higher GDP per capita tend to have higher happiness scores in this dataset.

**Causation** means that a change in one variable directly causes a change in another variable.

However, correlation does not mean causation. We cannot say that higher income directly causes people to be happier based only on these results. Other factors may also affect happiness, and correlation alone cannot prove cause and effect.

## 10. Final Conclusion

Through this project, I used Pandas to explore and analyze the World Happiness Report 2019 dataset.

I started by loading the data and checking its structure and quality. Then, I explored the columns, checked for missing and duplicate values, selected specific countries, and used different statistical methods to understand the data.

The results showed that Finland had the highest happiness score, while South Sudan had the lowest. Saudi Arabia ranked 28th with a happiness score of 6.375, which was higher than the overall average.

The correlation analysis also showed that GDP per capita had the strongest positive relationship with happiness score among the factors I explored.

This project helped me practice the basics of Pandas and understand how to work with real-world data, explore different factors, and turn numerical results into clear findings.
