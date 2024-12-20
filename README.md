# NullClass_internship
A data analytics project for Google Play Store app data with real-time dashboard visualizations.

**Task 1**

# Word Cloud for 5-Star Reviews of Health & Fitness Apps
This project generates a word cloud from the most frequent keywords found in 5-star reviews of apps in the "Health & Fitness" category from the Google Play Store. It excludes common stopwords and app names, providing meaningful insights into user sentiments.

Features:
Data Filtering: Filters reviews to include only those from the "Health & Fitness" category.
Text Cleaning: Excludes common stopwords and app names.
Word Cloud Generation: Creates a visual word cloud of the most frequent 5-star review keywords. Library Used: pandas: For data manipulation and handling. re: For regular expressions to clean text data. wordcloud: To generate the word cloud from review data. plotly: For visualizing and displaying the word cloud as an interactive dashboard.

**Task 2**

# Grouped Bar Chart for Top 10 App Categories
This project analyzes data from the Google Play Store, filtering it based on specific criteria to generate a grouped bar chart comparing the average rating and total review count for the top 10 app categories by number of installs. The chart is designed to update dynamically, with two different views: Average Rating View (Blue bars) Total Review Count View (Yellow bars) The graph is shown only between 3 PM IST and 5 PM Features: Data Filtering: Filters out apps with an average rating below 4.0. Excludes apps with a size less than 10 MB. Focuses on apps updated in January. Grouped Bar Chart: The x-axis displays the top 10 app categories. The y-axis shows the values for average rating (blue) and total review count (yellow). You can switch between these views by clicking the respective buttons for each metric. Graph Explanation: Blue Bars (Average Rating): Clicking the blue button will display the chart with average ratings of apps in the top categories. Yellow Bars (Total Review Count): Clicking the yellow button will display the chart showing the total review counts for the apps in the top categories.

**Task 3**

# Violin Plot for Distribution of Ratings in App Categories
This project visualizes the distribution of ratings for Google Play Store app categories using a violin plot. The plot is filtered based on the following criteria: Only categories with more than 50 apps. App names must contain the letter "C". Apps with fewer than 10 reviews and ratings greater than or equal to 4.0 are excluded. Visualizes the distribution of ratings for each app category. Displays the chart only between 4 PM and 6 PM. Shows rating distribution with box plots and individual data points for each category. Graph Explanation: The violin plot displays the distribution of ratings for apps in different categories. Each category is represented by a color-coded violin shape, which shows the distribution and variability of ratings. The chart helps analyze the spread of app ratings and identifies categories with higher or lower ratings.

Each task will generate output in both HTML and PNG formats.

**Dashboard** This project visualizes Google Play Store review data through an interactive dashboard that displays different charts based on the time of day. Features: Word Cloud: Shows the most frequent words in 'Health & Fitness' app reviews. Bar Chart: Displays top 10 app categories by average rating or review count. Available between 3 PM and 5 PM. Violin Plot: Shows the distribution of ratings for app categories. Available between 4 PM and 6 PM.
