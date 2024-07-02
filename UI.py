import streamlit as st
from data_util import get_dfs
import plotly.express as px
import pandas as pd
from streamlit_card import card
import plotly.graph_objects as go

st.set_page_config(
    page_title="Expense Analysis",
    layout="wide",
)

tab_labels, dfs = get_dfs()
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



for i in range(len(tabs)-1):
    with tabs[i]:
        df = dfs[tab_labels[i]]

        st.header(tab_labels[i].replace('.csv',''))
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

    st.subheader("Amount per Day")
    fig = px.bar(comb_df, x='Date', y='Amount',color='Category',text_auto=True)
    fig.update_layout(showlegend=True)
    st.plotly_chart(fig)

