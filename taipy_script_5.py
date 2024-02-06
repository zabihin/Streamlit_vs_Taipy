from taipy.gui import Gui
import pandas as pd
import plotly.express as px

data = pd.read_csv('data/city.csv')

selected_city = 'Paris'
cities= data['City'].unique()
page_md = """
<|layout|columns=200px 1|
<|part|render=True|class_name=sidebar|
# Taipy by **Zahra**
|>

<|
# Interactive Dashboard: Exploring Streamlit & Taipy Fundamentals

**French Cities Dashboard**


Data Frame:

<|{data}|table|page_size=5|>

<|{data}|chart|type=bar|x=City|y=Population|title=Population of French Cities|>

<|layout|columns=1 1|
#City <|{selected_city}|selector|lov={cities}|dropdown|class_name=fullwidth|label=Select a City|default_value='Paris'|>
<| 
# Population 
<|The population of {selected_city} is {data[data['City'] == selected_city]['Population'].to_list()[0]}|text|>
|>
|>
|>
|>


"""

Gui(page_md).run(dark_mode=False,port=6001)