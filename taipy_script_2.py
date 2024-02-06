from taipy.gui import Gui
import pandas as pd
import plotly.express as px

data = pd.read_csv('data/city.csv')


page_md = """
# Interactive Dashboard: Exploring Streamlit & Taipy Fundamentals

**French Cities Dashboard**


Data Frame:

<|{data}|table|page_size=5|>
"""

Gui(page_md).run(dark_mode=False,port=6001)