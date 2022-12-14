# MA705 Final Project

This repository contains files used in the MA705 dashboard project.

The final dashboard is deployed on Heroku [here](https://takutakuo.herokuapp.com)

## Dashboard Description

This dashboard invites people who are interested in setting up a home bar. This dashboard summarizes market prices of products in 5 most popular categories. Those who are just started adding to their collection can take a look with a few clicks. The generated table provides a basic info, such as name, size, price, and proof (alcohol content). The generated graph allows users to see the difference in prices.

### Data Sources

The dataframe for this project was collected from Blanchards website [here](https://blanchards.net). Total Wine has a more collections and information; however, their website refuses an access to scrape data. Although Blanchards has a few selection, their website has enough products to generate moderate size of dataframe. I scraped data for each category of my choice. Then, I used pd.concat function to combine 5 dataframes that I scraped. 

Original dataframe only had three columns 'name', 'size', and 'price'. I extracted the proof values and created a new column from the name values as their value contained the info regarding proof. I generated the type column based on index numbers. 

Scraping data for each kind of liquors took a great amount of time and often caused the program to crash. I saved each dataframe to csv. 



