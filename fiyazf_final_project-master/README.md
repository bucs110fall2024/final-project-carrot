# Interactive United States Financial Services Company Map

## CS110 Final Project Semester 1, 2024

## Team Members

Fiyaz Ferdouse

***

## Project Description

My project is an interactive map of the United States of America that focuses on states that house some of the top companies in financial services and asset management, providing users with information on these companies.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. The map of the USA (possibly with Alaska and Hawaii for fun)
2. Nodes atop states with the headquarters of some of the top financial services companies in America
3. Basic information on the included companies, such as CEO, headquarters address, and year founded
4. A way to keep track of the real time stock price of the companies
5. Images of the logos of the companies
6. I created all of the art myself (apart from the logos of course)

### Classes

CityNode
    - this initializes the images used to create the little node with a city icon, assigns a state to the node
    - with this initizalization, the node can be placed at a coordinate
    - it can detect when it is clicked, returning a boolean value
    - uses a dictionary to return a list of the ticker symbols from all companies recorded for the state

CompanyInfo
    - uses a given ticker symbol in order to retrieve information for the company
    - uses yfinance to return stock information on the company
    - use of a json dictionary to provide file paths to the 'companies' folder in assets in order to retrieve information on the company
    - also can create a path to the logo file for the company
    - uses wikipedia module to give just a little bit more information

StateInfo
    - given the name of a state, it will use the censusdata module to connect to an API to return the population of the state
    - also uses a dictionary to return the GDP of the state from prewritten values

Controller
    - houses the main loop and event loop for the interactive map, allowing users to click and hover around to receive information

### External Modules Used
    - yFinance: in order to retrieve stock information
    - censusData: in order to retrieve information on the populations of US states
    - wikipedia: provides a little bit of context on the company, albeit not a whole lot

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | hover over node      | node becomes highlighted and state and population are shown     |
|  2                   | hover over 2 nodes   | only one node becomes highlighted            |
|  3                   | click node           | information is displayed to the right  |
|  4                   | click off node       | information is removed from the right  |
|  5                   | press left and right arrow keys      | the information for the companies switches to the next company in the index, with the index either going +1 or -1|



