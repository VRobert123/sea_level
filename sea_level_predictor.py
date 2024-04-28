import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    line_2050 = [intercept + slope*year for year in range(df['Year'].min(), 2051)]
    plt.plot(range(df['Year'].min(), 2051), line_2050, 'r', label='Best Fit Line 1')

    # Create second line of best fit (from year 2000 onwards)
    recent_years_df = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_years_df['Year'], recent_years_df['CSIRO Adjusted Sea Level'])
    line_recent_2050 = [intercept_recent + slope_recent*year for year in range(2000, 2051)]
    plt.plot(range(2000, 2051), line_recent_2050, 'g', label='Best Fit Line 2')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Add legend
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
