import streamlit as st
from data_util import get_dfs
import plotly.express as px
import pandas as pd
from streamlit_elements import elements, mui, html
from streamlit_elements import dashboard
from streamlit_elements import nivo
tab_labels, dfs = get_dfs()
# tab_labels.append("YTD")

tab = st.sidebar.radio("Select a File", tab_labels)

f_name = tab.replace('.csv','')

df = dfs[tab]
cat_grp = df[['Category','Amount']].groupby(by='Category').sum().reset_index()


with elements("new_element"):
    layout = [
        # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
        dashboard.Item("first_item", 0, 0, 2, 2),
        dashboard.Item("second_item", 2, 0, 2, 2),
        dashboard.Item("third_item", 0, 2, 1, 1),
    ]

    # Next, create a dashboard layout using the 'with' syntax. It takes the layout
    # as first parameter, plus additional properties you can find in the GitHub links below.


