import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
import json
import yfinance as yf
from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


#get the stocks json as a dictionary
with open('IMKB_Stocks.json') as f:
    stocks = json.load(f)



#find the needed stock name from our dict
def find_key_value_pairs_by_phrase(phrase, dictionary):
    matching_pairs = {}
    for key, value in dictionary.items():
        if phrase in key:
            matching_pairs[key] = value
    return matching_pairs


#get the data of the desired stock from yahoo finance
def graph_data(stock_symbol):
    now= datetime.now()
    date=now.day
    month=now.month
    year=now.year
    hour=now.hour
    minute=now.minute
    second=now.second


    start=f'{int(year)-1}-{month}-{date}'
    end=f'{year}-{month}-{date}'

    df= yf.download(f'{stock_symbol}.IS',start,end)
    return df

#plot the graph and add as a tkinter widget 
def plot_stock_graph(stock_data,stock_name):
    # Create a new window to display the graph
    graph_window = tk.Toplevel(root)
    graph_window.title("Stock Graph")

    # Create a Matplotlib figure and axis
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plot the graph using the DataFrame data
    ax.plot(stock_data.index, stock_data['Adj Close'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Closing Value')
    ax.set_title(f'{stock_name} Closing Value Over Time')

    # Create a Matplotlib canvas and attach it to the graph window
    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack()




# Function to handle the search button click event
def search_button_click():
    # Get the search query from the entry widget
    search_query = search_entry.get()
    matching_stocks = find_key_value_pairs_by_phrase(search_query,stocks)
    
    
    stock_symbol = ''
    
    if len(matching_stocks) == 1:
        stock_name = next(iter(matching_stocks))
        stock_symbol = matching_stocks[stock_name]
        #get the stock data as a pandas df
        stock_data = graph_data(stock_symbol)
        
        # Check if the DataFrame is not empty and has required columns
        if not stock_data.empty and 'Adj Close' in stock_data.columns:
            # Call the function to plot and visualize the graph
            plot_stock_graph(stock_data,stock_name)
        else:
            messagebox.showinfo("Result", "Error: Invalid or empty stock data.")
        
        
        
    elif len(matching_stocks) == 0:
        messagebox.showinfo("Result", 'Wrong stock name try again')

    
    else:
        messagebox.showinfo("Result", f'Too many results, narrow your search \n {[key for key in matching_stocks.keys()]}')

    

# Create the main Tkinter window
root = tk.Tk()
root.title("IMKB Stock Application")

# Create a writing bar label
writing_bar_label = tk.Label(root, text="Enter the name of stock you want to display")
writing_bar_label.pack(pady=5)


# Create a frame for the search bar and button
search_frame = tk.Frame(root)
search_frame.pack(pady=10)

# Create a search entry widget
search_entry = tk.Entry(search_frame, width=30)
search_entry.pack(side=tk.LEFT)

# Create a search button
search_button = tk.Button(search_frame, text="Search", command=search_button_click)
search_button.pack(side=tk.LEFT, padx=5)

# Run the main event loop
root.mainloop()

