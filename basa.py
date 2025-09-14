import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Configuration de la connexion à la base de données SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=RAY_DINERI;'
    'DATABASE=Amazon;'
    'Trusted_Connection=yes;'  # Utiliser l'authentification Windows
)



# Requête SQL pour récupérer les données
query = """
SELECT  [Row ID]
      ,[Order ID]
      ,[Order Date]
      ,[Ship Date]
      ,[Ship Mode]
      ,[Customer ID]
      ,[Customer Name]
      ,[Segment]
      ,[Country]
      ,[City]
      ,[State]
      ,[Postal Code]
      ,[Region]
      ,[Product ID]
      ,[Category]
      ,[Sub-Category]
      ,[Product Name]
      ,[Sales]
      ,[Quantity]
      ,[Discount]
      ,[Profit]
  FROM [Amazon].[dbo].[AmazonProd]
"""

# Lire les données dans un DataFrame pandas
df = pd.read_sql(query, conn)

# Fermer la connexion
conn.close()

# Afficher les premières lignes du DataFrame
print(df.head())

# Exemple de statistique :

#Distribution des ventes par catégorie
plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Sales', data=df, estimator=sum, ci=None)
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()


#repartition de ventes par region (diagramme de sequteur).
sales_by_region = df.groupby('Region')['Sales'].sum().reset_index()
plt.figure(figsize=(8, 8))
plt.pie(sales_by_region['Sales'], labels=sales_by_region['Region'], autopct='%1.1f%%', startangle=140)
plt.title('Sales Distribution by Region')
plt.axis('equal')
plt.show()

#benifice par segements de client
plt.figure(figsize=(10, 6))
sns.barplot(x='Segment', y='Profit', data=df, estimator=sum, ci=None)
plt.title('Total Profit by Customer Segment')
plt.xlabel('Customer Segment')
plt.ylabel('Total Profit')
plt.show()

#histograme des quantités par categorie
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Quantity', hue='Category', multiple='stack', bins=20)
plt.title('Distribution of Quantity by Category')
plt.xlabel('Quantity')
plt.ylabel('Count')
plt.show()



