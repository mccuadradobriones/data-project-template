import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# reporting functions


def visualize_barplot(df_analysis,title):
    fig, ax = plt.subplots(figsize=(15,8))
    chart = sns.barplot(data=a_df, x='country', y='quantity_data_jobs_by_country')
    plt.title(title + "\n", fontsize=16)
    return chart
