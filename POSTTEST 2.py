import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('vgsales.csv')
numeric_df = df.select_dtypes(include=['number'])

# Tampilkan rata-rata, standar deviasi, nilai minimum, nilai maksimum, Q1, Q2, dan Q3 dari attribute bertipe angka.
print(numeric_df.describe())
print("\n")


# Tampilkan 10 record pertama dari dataset dengan attribute bertipe angka.
print(numeric_df.head(10))
print("\n")


# Tampilkan informasi jumlah record, jumlah attribute, nama attribute, jumlah attribute dengan tipe angka.
print(numeric_df.info())
print("\n")


# Tampilkan jumlah label dari semua attribute yang bernilai object (contoh : Jenis Kelamin, Agama).
print(df.select_dtypes(include=['object']).nunique())
print("\n")

# Visualisasi data kategorikal genre menggunakan bar 
plt.figure(figsize=(10,6))
df['Genre'].value_counts().plot(kind='bar')
plt.title('Jumlah Game per Genre')
plt.xlabel('Genre')
plt.ylabel('Jumlah Game')
plt.show()

# Visualisasi data numerik total global sales over the year menggunakan line plot
plt.figure(figsize=(10,6))
df.groupby('Year')['Global_Sales'].sum().plot(kind='line')
plt.title('Total Global Sales Over the Years')
plt.xlabel('Year')
plt.ylabel('Total Global Sales (in millions)')
plt.show()

# Visualisasi data genre per publisher menggunakan bar
plt.figure(figsize=(12,6))
df['Publisher'].value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Publishers by Number of Games Published')
plt.xlabel('Publisher')
plt.ylabel('Number of Games Published')
plt.show()

# Visualisasi data genre per platform menggunakan pie chart
platform_counts = df['Platform'].value_counts().head(10)
plt.figure(figsize=(8,8))
platform_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title('Top 10 Platforms by Number of Games')
plt.ylabel('')
plt.show()

# Tampilkan korelasi dataset menggunakan heatmap
plt.figure(figsize=(10,8))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Korelasi Antar Atribut Numerik')
plt.show()