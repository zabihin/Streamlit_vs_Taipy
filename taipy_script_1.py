from taipy.gui import Gui
import pandas as pd
import plotly.express as px

df = pd.read_csv('data/city.csv')


page_md = """
# Interactive Dashboard: Exploring Streamlit & Taipy Fundamentals

**French Cities Dashboard**
"""

Gui(page_md).run(dark_mode=False,port=6001)