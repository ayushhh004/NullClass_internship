import os
import webbrowser
import pytz
from datetime import datetime

# Path for HTML and image files
html_files_path = "./"
if not os.path.exists(html_files_path):
    os.makedirs(html_files_path)

# Placeholder for chart containers
plot_containers = ""

# Current time
now_ist = datetime.now(pytz.timezone('Asia/Kolkata'))
current_hour = now_ist.hour

#HTML Dashboard
dashboard_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Google Play Store Review Analytics</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #333;
            color: #fff;
            margin: 0;
            padding: 0;
        }}
        .header {{
            text-align: center;
            padding: 20px;
            background-color: #444;
        }}
        .container {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            padding: 20px;
        }}
        .plot-container {{
            border: 2px solid #555;
            margin: 10px;
            padding: 10px;
            width: 400px;
            height: 300px;
            background-color: #222;
            border-radius: 8px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.6);
            text-align: center;
            position: relative;
            cursor: pointer;
        }}
        .plot-container img {{
            max-width: 100%;
            max-height: 80%;
            border-radius: 4px;
        }}
        .plot-container:hover {{
            background-color: #444;
        }}
        .insights {{
            margin-top: 10px;
            font-size: 14px;
            color: #ddd;
        }}
        .message {{
            font-size: 16px;
            color: #ff6347;
            margin-top: 20px;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Google Play Store Reviews Analytics</h1>
    </div>
    <div class="container">
        {plots}
        <div class="message">
            {message}
        </div>
    </div>
</body>
</html>
"""

# Task 1: Show Word Cloud
plot_containers += """
<div class="plot-container" onclick="window.open('file:///C:/Users/Ayush%20Singh/NullClass/Task1/wordcloud_health_fitness.html', '_blank')">
    <img src="file:///C:/Users/Ayush%20Singh/NullClass/Task1/wordcloud_health_fitness.png" alt="Word Cloud Preview">
    <div class="insights">Word Cloud: Health & Fitness Reviews</div>
</div>
"""

# Task 2: Show Bar Chart (Available from 3 PM to 5 PM)
bar_chart_message = ""
if 15 <= current_hour < 17:
    plot_containers += """
    <div class="plot-container" onclick="window.open('file:///C:/Users/Ayush Singh/NullClass/Task 2/Bar_Graph.html', '_blank')">
        <img src="C:/Users/Ayush Singh/NullClass/Task 2/Bar_Graph.png" alt="Bar Chart Preview">
        <div class="insights">Bar Chart: Top 10 Categories</div>
    </div>
"""
else:
    bar_chart_message = "Bar Chart is available between 3 PM and 5 PM."

# Task 3: Show Violin Plot (Available from 4 PM to 6 PM)
violin_plot_message = ""
if 16 <= current_hour < 18:
    plot_containers += """
    <div class="plot-container" onclick="window.open('file:///C:/Users/Ayush Singh/NullClass/Task 3/Violin_Plot.html', '_blank')">
        <img src="C:/Users/Ayush Singh/NullClass/Task 3/Violin_Plot.png" alt="Violin Plot Preview">
        <div class="insights">Violin Plot: Distribution of Ratings</div>
    </div>
"""
else:
    violin_plot_message = "Violin Plot is available between 4 PM and 6 PM."

# Combining the plot containers and messages
message = bar_chart_message + "<br>" + violin_plot_message
final_html = dashboard_html.format(plots=plot_containers, message=message)

# Save the dashboard
dashboard_path = os.path.join(html_files_path, "dashboard.html")
with open(dashboard_path, "w", encoding="utf-8") as file:
    file.write(final_html)

print("Dashboard HTML file generated successfully!")

# Open the dashboard in web browser
webbrowser.open('file://' + os.path.realpath(dashboard_path))
