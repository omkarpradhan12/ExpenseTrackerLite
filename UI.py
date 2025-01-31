import streamlit as st
from data_util import get_dfs,get_ytd_df
import plotly.express as px
import pandas as pd
from streamlit_card import card
import plotly.graph_objects as go
import tkinter as tk
from tkinter import filedialog
import os
import dotenv

st.set_page_config(
    page_title="Expense Analysis",
    layout="wide",
)


def select_folder():
  """Opens a folder selection dialog and prints the chosen folder path."""

  root = tk.Tk()
  root.withdraw()

  folder_path = filedialog.askdirectory()

  if folder_path:
    return folder_path
  else:
    return "../CSV"


if os.path.isfile('.env')==False:
    f = open('.env','w+')
    f.write("dev='op'")
    f.close()

if os.path.isfile('.env'):
    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)
    if 'CSV-FOLDER' in os.environ:
        folder_path = os.getenv('CSV-FOLDER')
    else:
        folder_path = select_folder()
        # os.environ['CSV-FOLDER'] = folder_path
        dotenv.set_key(dotenv_file,key_to_set='CSV-FOLDER',value_to_set=folder_path)

# folder_path = select_folder()

tab_labels, dfs = get_dfs(folder_path=folder_path)
tab_labels.append("YTD")
# tab_labels = list(set(tab_labels))
tabs =  list(st.tabs(tab_labels))



# colorss = [
#     '#41B3F4',  # Light blue
#     '#208FBA',  # Ocean blue
#     '#0077C2',  # Cobalt blue
#     '#2CA02C',  # Forest green
#     '#FFFF00',  # Yellow
#     '#FFA500',  # Orange
#     '#FF0000'   # Red
#     ]

st.header(f'Folder Path : {folder_path}')
if st.button(label='Change Folder'):
    folder_path = select_folder()



for i in range(len(tabs)-1):
    with tabs[i]:
        df = dfs[tab_labels[i]]

        st.header(tab_labels[i].replace('.csv',''))

        # st.header("Summary")
        # st.markdown(generate_summary(data=df))

        cat_grp = df[['Category','Amount']].groupby(by='Category').sum().reset_index()
        cols = st.columns((1,2.5))
        with cols[0]:

            container = st.container(border=True)
            container.header("TOTAL : :blue["+str(sum(df['Amount']))+"]")

            st.dataframe(cat_grp, use_container_width=True)
            st.dataframe(df, use_container_width=True)
        # st.dataframe(df, use_container_width=True)
        with cols[1]:
            st.subheader("Amount per Category")
            fig = px.bar(cat_grp, x='Category', y='Amount',text_auto=True)
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig)

            st.subheader("Amount per Category")
            fig_donut = px.pie(cat_grp, values='Amount', names='Category', hole=0.4)
            st.plotly_chart(fig_donut)

        st.subheader("Amount per Day")
        fig = px.bar(df, x='Date', y='Amount',color='Category',text_auto=True)
        fig.update_layout(showlegend=True)
        st.plotly_chart(fig)

comb_df = pd.DataFrame()
for df in dfs:
    comb_df = pd.concat([dfs[df],comb_df])

cat_grp = comb_df[['Category','Amount']].groupby(by='Category').sum().reset_index()

with tabs[len(tabs)-1]:
    st.header("All Months")
    cols = st.columns((2.5,1))
    with cols[0]:
        st.dataframe(cat_grp, use_container_width=True)
        container = st.container(border=True)
        container = st.container(border=True)
        container.header("TOTAL : :blue["+str(sum(comb_df['Amount']))+"]")
        st.dataframe(comb_df, use_container_width=True)
    # st.dataframe(comb_df, use_container_width=True)
    with cols[1]:
        st.subheader("Amount per Category")
        fig = px.bar(cat_grp, x='Category', y='Amount',text_auto=True)
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig)

        st.subheader("Amount per Category")
        fig_donut = px.pie(cat_grp, values='Amount', names='Category', hole=0.4)
        st.plotly_chart(fig_donut)


    st.subheader("Amount by Month")
    cols_month = st.columns((2.5,1))

    month_wise = get_ytd_df(dfs)
    with cols_month[0]:
        fig = px.bar(month_wise, x='Month', y='Total',text_auto=True)
        fig.update_layout(showlegend=True)
        st.plotly_chart(fig)

    with cols_month[1]:
        st.dataframe(month_wise,use_container_width=True)

    st.subheader("Amount per Day")
    fig = px.bar(comb_df, x='Date', y='Amount',color='Category',text_auto=True)
    fig.update_layout(showlegend=True)
    st.plotly_chart(fig)

