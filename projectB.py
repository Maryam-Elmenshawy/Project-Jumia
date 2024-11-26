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

# Sidebar navigation with radio buttons
st.sidebar.title('Navigation')
option = st.sidebar.radio(
    'Choose a section:',
    ('Raw Data', 'Top Discounts Visualization', 'Summary Statistics', 'To Be Promoted', 'MongoDB')
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

elif option == 'To Be Promoted':
    st.subheader("Items that deserve a Promotion!")
    
    # List of items to be promoted
    promoted_items = [
        "OTG Type C To USB Converter Adapter To Connect...",
        "P9 Bluetooth Wireless Headphone - Blue4",
        "JOYROOM JR-QP191 Power Bank 10000 MAh Fast Charging",
        "Iphone Charger Head - 20w - Type-C Port - White",
        "Mobile Phone Holder With Base - Black",
        "Taha Offer Waterproof Mobile Phone Case 1 Piece",
        "Wireless Headset M90 With Power Bank-Black",
        "T900 Ultra Smart Watch 49mm 2.09 Infinite Display",
        "JOYROOM JR-OK3 Rotation & Adjustable Length Cable",
        "120W 6A Fast Charging Cable - Zinc Alloy 3.3ft",
        "OPPO Reno 11F Full Protection Case Visa Card &..."
    ]
    
    # Display the list
    for item in promoted_items:
        st.write(f"- {item}")

elif option == 'MongoDB':
    st.subheader('MongoDB Section')
    st.markdown("""
        [Jumia Data Base](https://cloud.mongodb.com/v2/673a260b07aa7d67bfcce2e6#/metrics/replicaSet/673a26d823f8100527987c45/explorer/jumia/products/find)
    """)
