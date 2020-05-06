# COVID19 | Stealthify Web App
​
> Official Github repo for Stealthify's Covid19 app.
​
​
## 🚩 Table of Contents
- [Introduction](#-what-is-covid19)
- [Directory Structure](##-directory-structure)
- [File structure description](#-what-each-file-is-for)
- [Technology Stack](#-technology-stack)
    - [Packages](#-packages)
    - [Database](#-database)
    - [IaaS](#-iaas)
    - [Dataset](#-dataset)
- [Contributing Guidelines](#-contributing-guidelines)
- [License](#-license)
​
---
​
​
#### What is COVID19 
​
![](header.jpg)
​
> Coronavirus disease (COVID-19) is an infectious disease caused by a new virus.
The disease causes respiratory illness (like the flu) with symptoms such as a cough, fever, and in more severe cases, difficulty breathing. As of 30 March 2020, 199 Countries and Territories around the world have reported a total of 737,204 confirmed cases of the coronavirus COVID-19 that originated from Wuhan, China, and a death toll of 34,959 deaths.
​
---
​
## Directory Structure
```
covid19
│   README.md
|   LICENSE.md
|   header.jpg
|
└───data\
│   │   dbfile1
│   │   dbfile2
└───geo\
|   |
|   |  requirements.txt
|   |  fetch_data.py
│   |  notebook.ipynb
|   |  geomaps.py
|
|  run.py
└───instance/
|   |  config.py
|
|
└───stealthify/
|   |  __init__.py
|   |    views.py
|   |    models.py
|   |    forms.py
|   └───static/
|   |    
|   |
|   └───templates/
    
```
​
---
​
​
## What each file is for
​
* README.md - The file that you are currently reading.
* LICENSE.md - License file.
* header.jpg - Image usedin README.md
* requirements.txt - All the packages required on a server to be installed before running the app.
* data\ -  A folder where all the data files (PostgreSQL database) can be stored. If the db is hosted on a server, we can remove this folder.
* geo\ -  A directory to keep all the geospatial plots, mainly contributed by Samar, Nitika, & Shivani
* run.py - POC file for the app
* config.py - Any special configurations for the app shall be handled here
* stealthify - Main app directory
* view.py - Controls the views
* models.py - Controls the models
* forms.py - Handles user interaction with the app
* static -  A directory containing static files like images to be used in UI
* templates - A directory to store core HTML files for UI.
​
---
​
​
## Technology Stack
​
* ### Packages
​
* Numpy
* Pandas
* scikit-learn
* matplotlib
* plotly
* seaborn
* bokeh
​
---
​
* ### Database
​
* PostgreSQL
​
---
​
* ### IaaS
​
* ### Dataset
​
---
​
## Contributing guidelines
​
> Please make a seperate branch with your name and raise PRs to be merged into master.
​
​
