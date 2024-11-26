import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
Jumia = pd.read_csv('Jumia_info_final.csv')

#Create a numeric column for '% change'
Jumia['numeric_change'] = Jumia['Discount %'].str.replace('%', '', regex=True).astype(float)

# Streamlit UI
st.title('Jumia Product Analysis')

# Display the raw data
st.subheader('Raw Data')
st.write(Jumia.head())

# Plotting Top Products with Largest Discounts
st.subheader('Top Products with Largest Discounts')
top_discounts = Jumia.nlargest(10, 'numeric_change')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Product Name', y='Discount %', data=top_discounts, ax=ax)
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

# Show summary statistics
st.subheader('Summary Statistics of Discounts')
st.write(Jumia['numeric_change'].describe())

