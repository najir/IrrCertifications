import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("./epa-sea-level.csv", index_col="Year")

    # Create scatter plot
    df_scatter = df.copy()
    fig, ax = plt.subplots(figsize=(15,15))
    plt.scatter(data=df_scatter, x=df_scatter.index, y='CSIRO Adjusted Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    

    
    # Create first line of best fit
    df_line1 = df.copy()
    df_line1 = df_line1.reindex(list(range(1880, 2051)))
    baseX = df_scatter.index
    futureX = df_line1.index
    line1Result = linregress(baseX, df_scatter['CSIRO Adjusted Sea Level'])
    line1xint = line1Result.intercept
    line1Slope = line1Result.slope
    line1Y = line1Slope*futureX + line1xint
    plt.plot(futureX, line1Y, color="black", linewidth=2)
  

    # Create second line of best fit
    df_line2 = df.copy()
    df_line2 = df_line2.reindex(list(range(2000, 2051)))
    adjusted_years = df.copy()
    adjusted_years = adjusted_years.reindex(list(range(2000,2014)))
    baseX2 = adjusted_years.index
    futureX2 = df_line2.index
    line2Result = linregress(baseX2, adjusted_years['CSIRO Adjusted Sea Level'])
    line2xint = line2Result.intercept
    line2Slope = line2Result.slope
    line2Y = line2Slope*futureX2 + line2xint
    plt.plot(futureX2, line2Y, color='red', linewidth=2)

    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()