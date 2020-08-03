import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

google_app_rating = pd.read_csv("googleplaystore.csv")
print("\nTop 5 rows of the dataset")
print("-----------------------------------------------------------------\n")
print(google_app_rating.head())
print("\nBottom 5 rows of the dataset")
print("-----------------------------------------------------------------\n")
print(google_app_rating.tail())

# print("On plotting boxplot we can see an outlier, which shows that data needs cleaning. ")
# google_app_rating.boxplot()
# plt.show()

print("\nCheck for the null values:")
print("-----------------------------------------------------------------\n")
print(google_app_rating.isnull().sum())
print("\n")
print(google_app_rating.describe())
print("\n")
print(google_app_rating.info())

print("\nCheck for all outliers:")
print("-----------------------------------------------------------------\n")
print(google_app_rating[google_app_rating['Rating'] > 5])

print("\nDelete or drop the outlier")
print("-----------------------------------------------------------------\n")
google_app_rating.drop(index=10472, inplace= True)

# google_app_rating.boxplot()
# google_app_rating.hist()
# plt.show()
# plt.close()


# The histogram is right skewed/ left skewed data median is a more appropriate measure than mean, we will fill all empty or null values with median values for numeric and mode for categorical.

# STEP 1: REMOVE THE COLUMNS THAT ARE 90% EMPTY

threshold = len(google_app_rating)*0.1
print(threshold)
google_app_rating.dropna(thresh= threshold, axis = 1, inplace= True)
print(google_app_rating.isnull().sum())

# STEP 2: DATA IMPUTATION AND MANIPULATION

# fills a series/col with median value
def data_imputation(ser):
    return ser.fillna(ser.median)

google_app_rating['Rating'] = google_app_rating['Rating'].transform(data_imputation)
google_app_rating['Rating'] = pd.to_numeric(google_app_rating['Rating'], errors='coerce')
# print(google_app_rating.isnull().sum())

print(google_app_rating['Type'].mode(),"\n",
      google_app_rating['Current Ver'].mode(), "\n",
      google_app_rating['Android Ver'].mode())

google_app_rating['Price'] = google_app_rating['Price'].apply(lambda x: str(x).replace('$','') if '$' in str(x) else str(x))
google_app_rating['Price'] = google_app_rating['Price'].apply(lambda x: float(x))
google_app_rating['Reviews'] = pd.to_numeric(google_app_rating['Reviews'], errors='coerce')

google_app_rating['Installs'] = google_app_rating['Installs'].apply(lambda x: str(x).replace('+','') if '+' in str(x) else str(x))
google_app_rating['Installs'] = google_app_rating['Installs'].apply(lambda x: str(x).replace(',','') if ',' in str(x) else str(x))
google_app_rating['Installs'] = google_app_rating['Installs'].apply(lambda x: float(x))

print(google_app_rating.dtypes)
print(google_app_rating.describe())


# STEP 3: DATA VISUALISATION

grp = google_app_rating.groupby('Category')
x = grp['Rating'].agg(np.mean)
y = grp['Price'].agg(np.sum)
z = grp['Reviews'].agg(np.mean)

# print(x)
# print(y)
# print(z)

plt.figure(figsize=(8,8))
plt.plot(x, 'ro', color = 'orange')
plt.title("Category Wise Ratings")
plt.xlabel("Category")
plt.ylabel("Ratings")
plt.xticks(rotation = 90)
plt.show()
plt.close()


plt.figure(figsize=(8,8))
plt.plot(y, 'r--', color = 'purple')
plt.title("Category Wise Pricing")
plt.xlabel("Category")
plt.ylabel("Price")
plt.xticks(rotation = 90)
plt.show()
plt.close()

plt.figure(figsize=(8,8))
plt.plot(z, 'bs',color = 'red')
plt.title("Category Wise Reviews")
plt.xlabel("Category")
plt.ylabel("Reviews")
plt.xticks(rotation = 90)
plt.show()
plt.close()