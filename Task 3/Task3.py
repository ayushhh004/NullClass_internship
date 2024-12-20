import os
import pandas as pd
import plotly.express as px
from datetime import datetime
import pytz
import plotly.io as pio

# Reading the dataset
app_data = pd.read_csv("C:/Users/Ayush Singh/NullClass/google_play_store_data/googleplaystore.csv")
print("App Data Columns:", app_data.columns)

# Clean 'Size' column, replace 'Varies with device' with None, and converting to numeric
app_data['Size'] = app_data['Size'].replace('Varies with device', None)
app_data['Size'] = app_data['Size'].str.replace('M', '').str.replace('k', '')
app_data['Size'] = pd.to_numeric(app_data['Size'], errors='coerce')

# Converting 'Last Updated' to datetime
app_data['Last Updated'] = pd.to_datetime(app_data['Last Updated'], errors='coerce')

# Converting 'Reviews' column to numeric
app_data['Reviews'] = pd.to_numeric(app_data['Reviews'], errors='coerce')

# Filtering the data
df_filtered = app_data[ 
    ~(app_data['Rating'] < 4.0) & 
    ~(app_data['Reviews'] < 10) & 
    (app_data['App'].str.contains('C', case=False, na=False))
]

# Filter by category with more than 50 apps
category_counts = df_filtered['Category'].value_counts()
valid_categories = category_counts[category_counts > 50].index
df_filtered = df_filtered[df_filtered['Category'].isin(valid_categories)]

# Getting the remaining categories after filtering
remaining_categories = df_filtered['Category'].unique()
print("Remaining Categories:", remaining_categories)

# Counting the number of apps per category in the filtered dataset
category_counts_remaining = df_filtered['Category'].value_counts()
print("Remaining Categories and their app counts:\n", category_counts_remaining)

# all categories are included, even those with no data after filtering
all_categories = app_data['Category'].unique()

# Current time
now_ist = datetime.now(pytz.timezone('Asia/Kolkata'))
current_hour = now_ist.hour

# Checking current time is between 4 PM and 6 PM
if 16 <= current_hour < 18:
    # Creating violin plot 
    fig_violin = px.violin(
        df_filtered,
        x='Category',
        y='Rating',
        color='Category',
        box=True, 
        points='all', 
        title='Distribution of Ratings for App Categories (Filtered)',
        labels={"Category": "App Category", "Rating": "App Rating"},
        category_orders={"Category": sorted(remaining_categories)}, 
        template='plotly'
    )

    # Layout for the violin plot
    fig_violin.update_layout(
        title_font_size=16,
        xaxis_title_font_size=12,
        yaxis_title_font_size=12,
        xaxis_tickangle=45,
        xaxis_tickfont=dict(size=10),
        yaxis_tickfont=dict(size=10),
        showlegend=False
    )

    # Path to save HTML and PNG files
    html_files_path = "./"  
    if not os.path.exists(html_files_path):
        os.makedirs(html_files_path)
    
    # Save as HTML
    file_path_html = os.path.join(html_files_path, "Violin_Plot.html")
    fig_violin.write_html(file_path_html)

    # Save as PNG
    file_path_png = os.path.join(html_files_path, "Violin_Plot.png")
    pio.write_image(fig_violin, file_path_png)

    # Show
    fig_violin.show()

else:
    print("The graph is only available between 4 PM and 6 PM.")
