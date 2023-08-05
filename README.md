# IMKB_Stock_Visualization_HTML_Parsing_Tkinter


Stock Visualizer

This project is an easy-to-use stock visualizer application. You can search for a stock by name and the application will pull its data, create a graph and display it within the GUI.

Features
Database of Stocks: Uses Beautiful Soup to scrape HTML data and create a comprehensive database of stocks.
Real-time Stock Data: Utilizes yfinance library to fetch real-time data for any stock.
Data Visualization: Forms a graph of the stock's data and visualizes it in a new window on the Tkinter application.


Prerequisites
Before you begin, ensure you have met the following requirements:

You have installed Python 3.6+.
You have installed the necessary Python libraries: beautifulsoup4, yfinance, tkinter, matplotlib.

Enter a part of the stock's actual name in the GUI. The application will find the symbol of the stock from the database and visualize the graph of the stock on a new window.

Usage
Upon launching the application, you will see a search bar. Here, you can type the name or partial name of the stock you want to visualize. The application will fetch the relevant data and generate a graph, which will appear in a new window.

