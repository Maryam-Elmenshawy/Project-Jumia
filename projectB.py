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

# Sort by % change and select top 10
top_discounts = Jumia.nlargest(10, 'numeric_change')

# Streamlit title and subheader
st.title("Top Discounts Visualization")
st.subheader("Top 10 Products with Largest Discounts")

# Create the figure and plot
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Product Name', y='numeric_change', data=top_discounts, palette='viridis', ax=ax)
ax.set_title('Top 10 Products with Largest Discounts')
ax.set_xlabel('Product Name')
ax.set_ylabel('% Change')

# Rotate x-axis labels
ax.tick_params(axis='x', rotation=45)

# Display the plot in Streamlit
st.pyplot(fig)

# Show summary statistics
st.subheader('Summary Statistics of Discounts')
st.write(Jumia['numeric_change'].describe())

