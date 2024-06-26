## Data Visualizer

This is a Streamlit web application for visualizing data from CSV files. The application allows users to select a CSV file from a specified directory, view the data, and create various types of plots using Seaborn and Matplotlib.

### Datasets Sources:

AIDS_ClinicalTrial_GroupStudy175.csv: https://www.kaggle.com/datasets/tanshihjen/aids-clinical-trials

breast_cancer_data.csv: This is from sklearn dataframe

diabetes.csv: https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset/data

parkinsons.csv: https://www.kaggle.com/datasets/vikasukani/parkinsons-disease-data-set

titanic.csv: https://www.kaggle.com/datasets/sakshisatre/titanic-dataset

### Features

- Load and display CSV files from a specified folder
- Select columns for the X and Y axes
- Generate different types of plots:
  - Line Plot
  - Bar Chart
  - Scatter Plot
  - Distribution Plot
  - Count Plot

### Link to my Webapp
https://ck-data-visualizer-webapp.streamlit.app/

### Usage

1. **Select a CSV file:**
Use the dropdown menu to select a CSV file from the data folder.

2. **View the data:**
The first few rows of the selected CSV file will be displayed.

3. **Select columns for plotting:**
Choose the columns for the X and Y axes from the dropdown menus.

4. **Choose a plot type:**
Select a plot type from the available options.

5. **Generate the plot:**
Click the "Generate Chart" button to visualize the selected data.

### Acknowledgements
- Streamlit
- Pandas
- Seaborn
- Matplotlib
