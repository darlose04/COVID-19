# COVID-19

This project downloads data from the [Johns Hopkins CSSEGISandData COVID-19 repository](https://github.com/CSSEGISandData/COVID-19).

Johns Hopkins displays the data from their repository [here](https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6).

Currently, I am working on using bash scripting to automate pull requests from the Github repository, which will update the CSV files containing data related to COVID-19 (confirmed cases and deaths). With Python, I am working on creating scripts that can parse the CSV files and push the necessary data into a SQL database. From there, I will create a Node.js API that can be accessed from a frontend built with React.js.
