# World Happiness Report 2019 – Exploratory Data Analysis with Pandas

## 1. Dataset Overview

First, I loaded the World Happiness Report 2019 dataset using Pandas.

The dataset contains **156 rows and 9 columns**. Each row represents a country, and each column contains information about a different factor, such as happiness score, GDP per capita, social support, healthy life expectancy, freedom, generosity, and perceptions of corruption.

I used data exploration methods to understand the dataset structure, view the first rows, check data types, and get basic statistical information.

I also checked data quality, including missing values and duplicate rows. The results showed that there were no missing values or completely duplicated rows.

## 2. Data Preparation and Exploration

I used data preparation methods to make the column names easier to work with in Jupyter Notebook.

I also explored country names and happiness score frequencies to understand the dataset better.

The dataset contains 156 different countries, and each country has one record. One happiness score appeared twice, but this does not mean there are duplicate rows.

## 3. Happiness Score Analysis

I explored happiness scores using statistical methods to calculate the average, minimum, and maximum values.

The average happiness score was approximately **5.407**.

I also used grouping and sorting methods to organize and compare happiness scores between countries.

## 4. Exploring and Selecting Countries

I used different data selection and filtering methods to select specific rows and columns from the dataset.

I also searched for specific countries, such as Saudi Arabia and Bahrain, and applied multiple conditions to find countries that matched certain criteria.

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

The results showed:

- Highest GDP per capita: Qatar.
- Highest freedom score: Uzbekistan.
- Highest social support score: Iceland.
- Highest perceptions of corruption value: Singapore.

I also used statistical aggregation methods to calculate the mean, minimum, and maximum values for several columns at the same time.

Finally, I explored the data types of all columns.

## 7. Mean Centering

I used a method called **Mean Centering** to calculate the difference between each value and the overall average.

I applied this method to happiness scores and social support values.

The results helped me identify which countries had values above or below the average:

- A positive value means the country's value is above the average.
- A negative value means the country's value is below the average.
- A value close to zero means the value is close to the average.

This helped me understand how each country compares to the overall average.

## 8. Correlation Analysis

In the final part, I explored the relationship between happiness scores and other numerical factors using correlation analysis.

The results showed a strong positive correlation between GDP per capita and happiness score, with a correlation value of approximately **0.794**.

I also created a correlation matrix to explore the relationships between all numerical columns.

The correlation values with happiness score were:

- GDP per capita: 0.794
- Healthy life expectancy: 0.780
- Social support: 0.777
- Freedom to make life choices: 0.567
- Perceptions of corruption: 0.386
- Generosity: 0.076

These results show that GDP per capita had the strongest positive correlation with happiness score, followed by healthy life expectancy and social support.

Generosity had a very weak positive correlation with happiness score.

## 10. Final Conclusion

Through this project, I used Pandas to explore and analyze the World Happiness Report 2019 dataset.

I started by loading the data and checking its structure and quality. Then, I explored the columns, checked for missing and duplicate values, selected specific countries, and used different statistical methods to understand the data.

The results showed that Finland had the highest happiness score, while South Sudan had the lowest. Saudi Arabia ranked 28th with a happiness score of 6.375, which was higher than the overall average.

The correlation analysis also showed that GDP per capita had the strongest positive relationship with happiness score among the factors I explored.

This project helped me practice the basics of Pandas and understand how to work with real-world data, explore different factors, and turn numerical results into clear findings.
