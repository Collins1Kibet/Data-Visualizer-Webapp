import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(
    page_title= 'Data Visualizer',
    page_icon= '📊',
    layout='centered'
)


st.title('📊 Data Visualizer')


working_directory = os.path.dirname(os.path.abspath(__file__))
folder_path = f"{working_directory}/data"
files_list = [e for e in os.listdir(folder_path) if e.endswith('.csv')]

selected_file = st.selectbox('Select a File', files_list, index= None)

if selected_file:

    file_path = os.path.join(folder_path, selected_file)

    dataframe = pd.read_csv(file_path)

    col1, col2 = st.columns(2)

    columns = dataframe.columns.tolist()

    with col1:
        st.write("")
        st.write(dataframe.head())

    with col2:
        x_axis = st.selectbox('Select the X-axis', options= columns + ['None'], index= None)
        y_axis = st.selectbox('Select the Y-axis', options= columns + ['None'], index= None)

        chart_list = ['Line Plot', 'Bar Chart', 'Scatter Plot', 'Distribution Plot', 'Count Plot']

        selected_chart = st.selectbox('Select a Chart', options= chart_list, index= None)


if st.button('Generate Chart'):
    fig, ax = plt.subplots(figsize= (7, 5))

    if selected_chart == 'Line Plot':
        sns.lineplot(x= dataframe[x_axis], y= dataframe[y_axis], ax= ax)

    elif selected_chart == 'Bar Chart':
        sns.barplot(x= dataframe[x_axis], y= dataframe[y_axis], ax= ax)

    elif selected_chart == 'Scatter Plot':
        sns.scatterplot(x= dataframe[x_axis], y= dataframe[y_axis], ax= ax)

    elif selected_chart == 'Distribution Plot':
        sns.histplot(dataframe[x_axis], kde=True, ax= ax)

    elif selected_chart == 'Count Plot':
        sns.histplot(x= dataframe[x_axis], ax= ax)

    ax.tick_params(axis= 'x', labelsize= 11)
    ax.tick_params(axis= 'y', labelsize= 11)

    plt.title(f'{selected_chart} of {x_axis} vs {y_axis}', fontsize= 12)
    plt.xlabel(x_axis, fontsize= 10)
    plt.ylabel(y_axis, fontsize= 10)

    st.pyplot(fig)