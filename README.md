# SYSC3010 Labs Repository for Varrahan Uthayan
## Lab1
Lab1 is about the basics of setting up and using the RPI and RPI SenseHat. It provides basic implementation on how we can use the RPI SenseHat's LED's and sensors. Lab1 contains 3 files. One file is a screenshot of the output when calling ifconfig from an ssh terminal. Another file, showmyname.py that outputs my username on a loop. The final file, showsensordata.py, displays te temperature, humidity, and pressure that is read from the RPI onto the SenseHat LED as a scrolling message.

[Lab1 README](./Lab1/README.md)

## Lab2
Lab2 is about setting up sqlite on the RPI and using the relational database along side python to build scripts to store data and visualize data from a sqlite database. This lab also covers receiving json responses from external sources and formatting the data to be suitible for sqlite databases. There are 3 python files in this project. The first file, lab2-database-data-logger.py, takes sensor data from the RPI Sense hat and stores it inside the sqlite database. The second file, lab2-database-data-visualizer.py, extracts data from a sqlite database, stores it in a pandas DataFrame, and plots the data on a plotly time series graph. The last python file, lab2-database-json.py, takes the data from an external API in the form of a json and stores it within a sqlite database.

[Lab2 README](./Lab2/README.md)

### Useful links and resources for the SYSC3010 labs:
 - [GitHub Starter Course Page with useful links](GitHubStarter.md) *(Provided by GitHub Classroom staff)*
 - *add other resources you find to be useful*
