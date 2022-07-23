# System for receiving and displaying data from Google Spreadsheets

The system consists of a parser, a microservice for adding data to the database, a web-api service for receiving data from the database, and a web interface.

### Parser-service 

Get data from google spreadsheet using google api. Gets the current exchange rate from the site of the Central Bank of the Russian Federation. Transforms the data and sends it using JSON-rpc to the microservice.

### Data-microservice

Takes parser data and adds it to the database. If necessary, the data in the database is updated or deleted. Powered by FastAPI and SQLAlchemy

### Api-service

Api-service sends data to the client application.

Has the following methods:

* GET /api/data/ - to get the whole table
* GET /api/total/ - receives the full dollar amount
* GET /api/per_day/ - receives distribution by day

