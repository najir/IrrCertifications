import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('./fcc-forum-pageviews.csv', parse_dates=True, index_col='date')
# Clean data
df = df[
(df['value'] >= df['value'].quantile(.025)) &
(df['value'] <= df['value'].quantile(.975))]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(25,8))
    plt.rcParams['font.size'] = 16
    plt.plot(df.index, df['value'], '-r')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = [d.strftime('%B') for d in df_bar.index]
    df_bar['year'] = df_bar.index.year
    monthOrder=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=monthOrder, ordered=True)
    # Draw bar plot
    fig = plt.figure(figsize=(12,12))
    sns.barplot(data=df_bar, y='value', x='year', hue='month',   width=0.5, edgecolor="0.5", errwidth=0, palette=sns.color_palette("husl", 9))
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(loc='upper left', title="Months")




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    boxOrder = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2, figsize=(25,10))
    plt.rcParams['font.size'] = 16
    sns.boxplot(data=df_box, x='year', y='value', ax=ax[0]).set(
      xlabel="Year",
      ylabel = "Page Views",
      title="Year-wise Box Plot (Trend)"
    )
    sns.boxplot(data=df_box, x='month', y='value', ax=ax[1], order=boxOrder).set(
      xlabel = "Month",
      title = "Month-wise Box Plot (Seasonality)",
      ylabel = "Page Views"
    )


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
