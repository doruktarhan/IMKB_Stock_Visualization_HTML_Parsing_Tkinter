# IMKB_Stock_Visualization_HTML_Parsing_Tkinter


## Stock Visualizer

This project is an easy-to-use stock visualizer application. You can search for a stock by name from IMKB and the application will pull its data, create a graph and display it within the GUI.

## Features

__Database of Stocks__: Uses Beautiful Soup to scrape HTML data and create a comprehensive database of stocks.

__Real-time Stock Data__: Utilizes yfinance library to fetch real-time data for any stock.

__Data Visualization__: Forms a graph of the stock's data and visualizes it in a new window on the Tkinter application.


## Prerequisites

You have installed the necessary Python libraries: beautifulsoup4, yfinance, tkinter, matplotlib.



## Usage
You only need to run IMKB_Tkinter.py file in order to run the app. The other files are for forming the DB with beautifulsoup and a tutorial on how to use yfinance library. 

Enter a part of the stock's actual name in the GUI. The application will find the symbol of the stock from the database and visualize the graph of the stock on a new window.

Upon launching the application, you will see a search bar. Here, you can type the name or partial name of the stock you want to visualize. The application will fetch the relevant data and generate a graph, which will appear in a new window.

