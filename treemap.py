import collections
import plotly.express as px
import pandas as pd

"""
Parses letters in a file and present the occurances in a treemap.
An interactive treemap will be rendered in web browser.
An image file will be saved locally too.

The sample program parses itself.
"""

# The file to parse and present in treemap
fn = "treemap.py"
img = "treemap.png"

def generate_treemap(filename):
    with open(filename, 'r') as file:
        text = file.read().lower()

    # Count the frequency of each letter
    letter_counts = collections.Counter(c for c in text if c.isalpha())

    # Prepare data for the treemap
    letters, frequencies = zip(*sorted(letter_counts.items(), key=lambda item: item[1], reverse=True))
    total_count = sum(frequencies)
    percentages = [f / total_count * 100 for f in frequencies]
    percentages_for_display = [f"{p:.2f}%" for p in percentages]

    # Generate a DataFrame
    df = pd.DataFrame({'letters': letters, 'frequencies': frequencies, 
                       'percentages': percentages, 'percentages_for_display': percentages_for_display})
    # Generate a treemap
    fig = px.treemap(df, path=['letters'], values='frequencies', color='percentages',
                     color_continuous_scale='YlOrRd', title="Treemap of Letters in {}".format(filename),
                     custom_data=['percentages_for_display'])

    fig.update_traces(textinfo='label+percent entry', hovertemplate='Letter: %{label}<br>Count: %{value}<br>Percentage: %{customdata[0]}')
            
    # Show the plot
    fig.show()

    # Save the figure
    fig.write_image(img)

# Call the function with your file
generate_treemap(fn)
