from taipy.gui import Gui
import pandas as pd
import plotly.express as px

data = pd.read_csv('data/city.csv')
representation_toggle = ['Page 1', 'Page 2']
selected_representation = representation_toggle[0]
selected_city = 'Paris'
cities= data['City'].unique()


layout_map = {
    "dragmode": "zoom",
    "mapbox": {
        "style": "open-street-map",
        "center": {"lat": 46.2276, "lon": 2.2137}, 
        "zoom":5
}
}

max_size = 80  # Maximum marker size
min_population = data['Population'].min()
max_population = data['Population'].max()
data['Size'] = data['Population'].apply(lambda x: ((x - min_population) / (max_population - min_population)) * 80 + 45)  


marker_map = { "size": "Size", "showscale":True, "colorscale":"Viridis"}

page_1="""# Interactive Dashboard: Exploring Streamlit & Taipy Fundamentals

**French Cities Dashboard**


Data Frame:

<|{data}|table|page_size=5|>

<|{data}|chart|type=bar|x=City|y=Population|title=Population of French Cities|>

<|layout|columns=1 1|
#City <|{selected_city}|selector|lov={cities}|dropdown|class_name=fullwidth|label=Select a City|default_value='Paris'|>
<| 
#Population 
<|The population of {selected_city} is {data[data['City'] == selected_city]['Population'].to_list()[0]}|text|>
|>
|>
|>
"""

page_2="""
<|{data}|chart|type=scattermapbox|lat=Latitude|lon=Longitude|marker={marker_map}|layout={layout_map}|text=Text|mode=markers|height=800px|>
"""
page_md = """
<|layout|columns=200px 1|
<|part|render=True|class_name=sidebar|
# Taipy by **Zahra**
|>

<|
<|{selected_representation}|toggle|lov={representation_toggle}|>

<|part|render={selected_representation == "Page 1"}|
"""+page_1+"""


<|part|render={selected_representation == "Page 2"}|
"""+page_2+"""


|>
|>
"""

Gui(page_md).run(dark_mode=False,port=6001)