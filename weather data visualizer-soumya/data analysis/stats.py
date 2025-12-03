import pandas as pd
import numpy as np

def show_numpy_stats(df):
    """
    Calculates basic statistics using NumPy.
    """
    print("\n--- NumPy Statistics ---")
    
    # Convert the column to a numpy array first
    t = df['Temperature_C'].to_numpy()

    # Using numpy functions as requested
    print("Mean Temp:", np.mean(t))
    print("Max Temp:", np.max(t))
    print("Min Temp:", np.min(t))
    print("Std Dev:", np.std(t))

def show_monthly_averages(df):
    """
    Groups data by month and shows averages.
    """
    print("\n--- Monthly Averages (Task 5) ---")
    
    # Get month name from the Date column
    df['Month'] = df['Date'].dt.month_name()

    # Sort the months correctly so they don't appear alphabetically (Apr, Aug...)
    months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']
    
    # Making it categorical fixes the sorting order
    df['Month'] = pd.Categorical(df['Month'], categories=months_order, ordered=True)

    # Group by month and calculate mean
    grp_data = df.groupby('Month', observed=True)[['Temperature_C', 'Rainfall_mm']].mean()
    print(grp_data)
    
    return grp_data