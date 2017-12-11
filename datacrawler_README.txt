Data Crawler README

Data crawler and preprocessor are used interchangeably.

Choose an API key by selecting user=(0,1). If the max number of requests is hit, then switch the API key.

The preprocessor assumes that you ahve a folder titled "Tweets" in which it can put the parsed data. It also assumes that you've downloaded the yahoo finance data in csv format for the tickers you're interested in and the time range you want. These need to be placed in a folder called "StockData" in the same working directory as the preprocessor. 

Choose the tickers you wish to pull from in the last Jupyter cell, within the list variable "tickers". Specify the start date and the end date via variables start_date and end_date respectively. Set base_date = start_date - 1 day. Run all of the cells and then execute the last cell, and it will pull the tweets and deposit them.

Note: CSV file size does not update instantaneously. To see if anything has been deposited in the CSV files, open the files.