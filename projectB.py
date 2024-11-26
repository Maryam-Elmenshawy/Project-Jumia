import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
Jumia = pd.read_csv('Jumia_info_final.csv')

# Create a numeric column for '% change'
Jumia['numeric_change'] = Jumia['Discount %'].str.replace('%', '', regex=True).astype(float)

# Streamlit UI
st.title('Jumia Product Analysis')

# Sidebar navigation
st.sidebar.title('Navigation')
option = st.sidebar.selectbox(
    'Choose a section:',
    ('Raw Data', 'Top Discounts Visualization', 'Summary Statistics')
)

# Display content based on selection
if option == 'Raw Data':
    st.subheader('Raw Data')
    st.write(Jumia.head())

elif option == 'Top Discounts Visualization':
    # Sort by % change and select top 10
    top_discounts = Jumia.nlargest(10, 'numeric_change')
    
    st.subheader("Top 10 Products with Largest Discounts")

    # Create the figure and plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Product Name', y='numeric_change', data=top_discounts, palette='viridis', ax=ax)
    ax.set_title('Top 10 Products with Largest Discounts', fontsize=16)
    ax.set_xlabel('Product Name', fontsize=12)
    ax.set_ylabel('% Change', fontsize=12)
    
    # Rotate x-axis labels
    ax.tick_params(axis='x', rotation=45)
    
    # Adjust layout to fix alignment issues
    plt.tight_layout()
    
    # Optional: Fine-tune the spacing manually if needed
    fig.subplots_adjust(bottom=0.25)  # Adjust the bottom margin if labels overlap
    
    # Display the plot
    st.pyplot(fig)

elif option == 'Summary Statistics':
    st.subheader('Summary Statistics of Discounts')
    st.write(Jumia['numeric_change'].describe())
