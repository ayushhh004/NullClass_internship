import pandas as pd
import re
from wordcloud import WordCloud, STOPWORDS
import plotly.graph_objects as go
import plotly.io as pio
import os

# Load datasets
app_data = pd.read_csv("C:/Users/Ayush Singh/NullClass/google_play_store_data/googleplaystore.csv")
reviews_data = pd.read_csv("C:/Users/Ayush Singh/NullClass/google_play_store_data/googleplaystore_user_reviews.csv")

# Filter for Health & Fitness category
health_fitness_apps = app_data[app_data['Category'] == 'HEALTH_AND_FITNESS']

# Extract unique app names in the 'Health & Fitness' category
health_fitness_app_names = health_fitness_apps['App'].unique()
print("Number of Health & Fitness Apps:", len(health_fitness_app_names))

# Filter reviews for apps in 'Health & Fitness' category
health_fitness_reviews = reviews_data[reviews_data['App'].isin(health_fitness_app_names)]

# Focus on 5-star reviews (Positive Sentiment)
filtered_reviews = health_fitness_reviews[health_fitness_reviews['Sentiment'] == 'Positive']
print("Number of 5-Star Reviews:", len(filtered_reviews))

# Combine all reviews into a single string
review_text = " ".join(filtered_reviews['Translated_Review'].dropna())
print("Sample Review Text:", review_text[:300])

# List of stopwords from WordCloud's built-in stopwords
stopwords = set(STOPWORDS)
app_names = health_fitness_app_names.tolist()

def clean_text(text):
    # Convert text to lowercase
    text = text.lower()  
    
    # Remove app names from the text
    text = re.sub(r'\b(' + '|'.join(map(re.escape, app_names)) + r')\b', '', text)  
    
    # Remove special characters, digits, and punctuation
    text = re.sub(r'[^a-z\s]', '', text)  
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)  
    
    return text

# Clean the review text
cleaned_text = clean_text(review_text)

# Remove stopwords
cleaned_text = " ".join([word for word in cleaned_text.split() if word not in stopwords]) 

print("Sample Cleaned Text:", cleaned_text[:300])

wordcloud = WordCloud(width=1500, height=1000, background_color='white', colormap='plasma').generate(cleaned_text)

# Convert the WordCloud object to a NumPy array
wordcloud_array = wordcloud.to_array()

# Save the word cloud as a PNG file
png_file_path = "wordcloud_health_fitness.png"
wordcloud.to_file(png_file_path)
print(f"Word Cloud saved as PNG at: {png_file_path}")

# Create the HTML folder 
html_files_path = "./"
if not os.path.exists(html_files_path):
    os.makedirs(html_files_path)

# Function to save the plot as an HTML file
plot_containers = ""

def save_plot_as_html(fig, filename, insight):
    global plot_containers
    filepath = os.path.join(html_files_path, filename)
    html_content = pio.to_html(fig, full_html=False, include_plotlyjs='inline')
   
    plot_containers += f"""
    <div class="plot-container" id="{filename}" onclick="openPlot('{filename}')">
        <div class="plot">{html_content}</div>
        <div class="insights">{insight}</div>
    </div>
    """
    fig.write_html(filepath, full_html=False, include_plotlyjs='inline')

fig = go.Figure()


fig.add_trace(
    go.Image(
        z=wordcloud_array
    )
)

fig.update_layout(
    title={
        'text': 'Word Cloud for 5-Star Reviews in Health & Fitness Apps',
        'y': 0.9,
        'x': 0.5,  
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 16, 'color': 'black'}
    },
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    margin=dict(l=0, r=0, t=100, b=0), 
)

# Display the figure
fig.show()

# Save the plot as HTML
save_plot_as_html(fig, "wordcloud_health_fitness.html", "This word cloud represents the most frequent words in 5-star reviews for Health & Fitness apps.")
