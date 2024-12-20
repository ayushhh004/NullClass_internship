import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import pytz
import os
import plotly.io as pio

# Reading the dataset
app_data = pd.read_csv("C:/Users/Ayush Singh/NullClass/google_play_store_data/googleplaystore.csv")
print("App Data Columns:", app_data.columns)

# Handling 'Size' column and converting to numeric
app_data['Size'] = app_data['Size'].replace('Varies with device', None)
app_data['Size'] = app_data['Size'].str.replace('M', '').str.replace('k', '')
app_data['Size'] = pd.to_numeric(app_data['Size'], errors='coerce')

# Converting Last Updated to datetime
app_data['Last Updated'] = pd.to_datetime(app_data['Last Updated'], errors='coerce')

# Converting Reviews column to numeric, force errors
app_data['Reviews'] = pd.to_numeric(app_data['Reviews'], errors='coerce')

# Filtering data
df_filtered = app_data[
    (app_data['Rating'] >= 4.0) &
    (app_data['Size'] >= 10) & 
    (app_data['Last Updated'].notna())
]

# Last Updated is datetime
if not pd.api.types.is_datetime64_any_dtype(app_data['Last Updated']):
    app_data['Last Updated'] = pd.to_datetime(app_data['Last Updated'], errors='coerce')

# Filtering by apps updated in January
df_filtered = df_filtered[df_filtered['Last Updated'].dt.month == 1]

# Grouping data by Category
df_grouped = df_filtered.groupby('Category').agg(
    average_rating=('Rating', 'mean'),
    review_count=('Reviews', 'sum')
).sort_values(by='review_count', ascending=False).head(10)

# Getting current time
now_ist = datetime.now(pytz.timezone('Asia/Kolkata'))
current_hour = now_ist.hour

# Checking if the current time is between 3 PM and 5 PM
if 15 <= current_hour < 17:
    categories = df_grouped.index

    # Creating a bar chart
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=categories,
        y=df_grouped['average_rating'],
        name='Average Rating',
        marker_color='blue'
    ))

    fig.add_trace(go.Bar(
        x=categories,
        y=df_grouped['review_count'],
        name='Total Review Count',
        marker_color='orange'
    ))

    fig.update_layout(
        title="Top 10 App Categories by Average Rating and Review Count",
        xaxis_title="Category",
        yaxis_title="Values",
        barmode='group',
        xaxis_tickangle=45
    )

    # Path to save HTML and PNG files
    html_files_path = "./"
    if not os.path.exists(html_files_path):
        os.makedirs(html_files_path)

    # Save as HTML
    file_path_html = os.path.join(html_files_path, "Bar_Graph.html")
    fig.write_html(file_path_html)

    # Save as PNG
    file_path_png = os.path.join(html_files_path, "Bar_Graph.png")
    pio.write_image(fig, file_path_png)

    # Show the plot
    fig.show() 
else:
    print("The graph is only available between 3 PM and 5 PM.")
