# Henesys Marketplace

## Group Members
1. Song Yu Xiang
2. Lim Yu Xuan
3. Lau Wei Ting
4. Too Min Jay
5. Wong Jie Peng
6. Kathy Tong


## Project/Dependencies to install 

1. error microservice 
- pip install pymongo

2. twilio_notifs microservice
- python -m pip install pika
- pip3 install twilio --upgrade OR easy_install twilio
- pip install python-dotenv
  ## to install the virtual environemnt for twilio (if need)
- pip install --user virtualenv
- python -m virtualenv venv

3. Others 
- npm install -g nodemon

## Twilio Configurations
- Note: ESD G5 T2 would need to add your number into the twilio account first as a verified number in order for a notification to be received 
- send 'join wood-fought' to the number: +14155238886 
- the above service only last around 2-3 days hence it is best to send "join wood-fought" everytime Henesys Marketplace is run 


## Project Desc
- Henesys Marketplace is a consumer-to-consumer platform for buying and selling food items that are near expiry. This reduces food waste and builds a “Kampong” spirit of sharing within the community. 
- For sellers, this platform allows them to list their items and choose to approve or reject offers from buyers. 
- For buyers, they are able to make an offer for a food item and make payment.


## How to start/installation
1. Ensure that WAMP/MAMP server is up and running
2. Open file docker-compose.yml in directory 'ESDT4/docker-compose.yml' and replace all 'tinggzster' with your docker's username
3. Start and run all of the microservices by running command 'docker-compose up' in the 
in directory 'ESDT4/docker-compose.yml'
4.  Open the app by accessing <URL> (should be deployed on heroku)
5. After the deployed application has loaded, click ........ button on the right of the page to Sign in for the start of the first user scenario.


## User Scenarios 
    1. Seller lists a food item 
    2. Buyer submits an offer for a food item 
    3. Seller Accept or Reject offer 
    4. Buyer leaves a rating for the seller 

## To start of: 
1. Naviagte to <URL> for the deployed Henesys Markplace
2. Login in with google account

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
3. Buyer will be notified for offer acceptance or reject

## User Scenario 4: Buyer leaves a rating for the seller 
1. If offer is accepted, there will be an assumption that the buyer and the seller has met up and paid 
2. Buyer will leave rating on the "My Offers" page

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



## Project setup
```
npm i (to retrive mode_modules)
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

test








## Librairies/Dependencies loaded for Notifs

pip install pymongo --> notifs
docker run -d --hostname esd-rabbit --name rabbitmq-mgmt -p 5672:5672 -p 15672:15672 rabbitmq:3-management --> to run docker fo r


python -m pip install pika
pip3 install twilio --upgrade OR easy_install twilio
pip install python-dotenv

#to install the virtual environemnt

pip install --user virtualenv
python -m virtualenv venv

#to run the virtual environment 
venv\Scripts\activate

reference links: https://www.youtube.com/watch?v=Svl_W81wUYU&t=526s 
https://stackoverflow.com/questions/48911582/virtualenv-to-path-on-windows-10 
https://stackoverflow.com/questions/49924636/twilio-the-requested-resource-was-not-found 
https://stackoverflow.com/questions/44194427/virtualenv-activate-does-not-work


## Librairies/Dependencies loaded for SellerView UI
npm install --save axios sweetalert --> for sellerView UI


pip install dnspython 
**python -m pip install requests**

**python -m pip install flask_cors**
npm install -g nodemon



docker-compose up