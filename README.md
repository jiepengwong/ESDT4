# Henesys Marketplace

## Group Members
1. Song Yu Xiang
2. Lim Yu Xuan
3. Lau Wei Ting
4. Too Min Jay
5. Wong Jie Peng
6. Kathy Tong

## Project Desc
- Henesys Marketplace is a community-driven marketplace for buying and selling food items that are near expiry. This reduces food waste and builds a “Kampong” spirit of sharing within the community. 
- For sellers, this platform allows them to list their items and choose to approve or reject offers from buyers. 
- For buyers, they are able to make an offer for a food item and make payment (physically) to foster a sense of community. 

## Twilio Configurations
- Note: We would need to add your number into the twilio account first as a verified number in order for a notification to be received 
- send 'join wood-fought' to the number: +14155238886 
- the above service only last around 2 days hence it is best to send "join wood-fought" everytime Henesys Marketplace is run 


## User Scenarios 
    1. Seller lists a food item 
    2. Buyer submits an offer for a food item 
    3. Seller Accept or Reject offer 
    4. Buyer leaves a rating for the seller 

## How to start/installation
1. Ensure that WAMP/MAMP server is up and running
2. Import the 'profile.sql' SQL file in PhpMyAdmin to create necessary databases for the microservices. This file can be found in the following path: 'ESDT4/profile/profile.sql'
3. To allow remote access to database(adding a new user): 
  
    i. Open phpMyAdmin and click 'User Accounts'
    ii. Click 'Add user account' and specify the following 
      a. User name: ESDT4
      b. Host name: %
      c. Password: Change to 'No Password'

4. Open file docker-compose.yml in directory 'ESDT4/docker-compose.yml' and replace all 'tinggzster' with your docker's username
5. Start and run all of the microservices by running command 'docker-compose up' in the directory 'ESDT4'
in directory 'ESDT4/docker-compose.yml'
6. Open the app by accessing 'localhost/ESDT4'
7. Login using your gmail account (google authentication)

## User Scenario 1: Seller lists a food item 
1. Seller can start selling items by clicking on 'Sell' on the UI 
2. Input the item details: Item Name, Category, Item Description, Location of Pick-up, and Date and Time of Collection and press 'Create Listing' 

## User Scenario 2: Buyer submits an offer for a food item 
1. Buyer presses on "Henesys Market" to direct to the homepage
2. Selects on "More Details"
3. Enters price on the offer text field and press"Make Offer Now". Buyer will be redirected back to the main page after a successful offer made.
4. A notification will be sent to the seller's whatsapp for an offer made by the Buyer 

## User Scenario 3: Seller Accept or Reject offer 
1. After receiving the notifications from whatsapp 
2. Seller will proceed to "My Listings" page on Henesys Marketplace to "Accept" or "Reject" 
3. Buyer will be notified for offer acceptance or rejection

## User Scenario 4: Buyer leaves a rating for the seller 
1. If offer is accepted, there will be an assumption that the buyer and the seller has met up and paid 
2. Buyer will leave rating on the "My Offers" page

## Side Scenarios: 
- If you realised that you made a wrong offer, you can remove your offer by clicking the remove offer in "My Offers" page 
- If you want to remove your listings that you have created as a seller, you can remove it under "My Listings" page

## API Acknowlegements
1. Google Oauth2 API
2. Twilio API

## Henesys Marketplace is built with the following libraries 

######  Python Libraries 
Flask
SQLAlchemy
DateTime
os
sys
requests
Pika
Json
flask_cors
pymongo 

## Project/Dependencies to install 
1. error microservice 
- pip install pymongo

2. twilio_notifs microservice
- python -m pip install pika
- pip3 install twilio OR easy_install twilio
- pip install python-dotenv

3. item microservice
- npm install -g nodemon

4. Others
- python -m pip install requests
- python -m pip install flask_cors