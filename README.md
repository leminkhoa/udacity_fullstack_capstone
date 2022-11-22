# Udacity Capstone Project - Money App 

## Project Introduction

This project builds a backend Flask server for Personal Money App. This app helps user log transactions that they spend/receive as a specific category.

The application must:

- Allow users to get/create/edit/delete budget categories.
- Allow users to get/create/edit/delete transactions.
- Only ADMIN can create/edit/delete while a normal USER is limited to get only.

## Project Idea

Database used in this project includes three tables:
- `category`: Store all budget categories such as Health, Transacportation, Apparel, etc... that a transaction might belong to.
- `transaction_type`: Each category might be further classified as Income or Expense. By default, we only have 2 main categories for this app: 
    - `Cash In` for classifying categories as income
    - `Cash Out` for classifying categories as expense
- `transaction`: Store all transactions that a person might have.


## Project Structure

```
├── README.md                           
├── auth0                   \* AUTH0 SET UP INSTRUCTIONS *\       
│   ├── README.md
│   └── images
│       
├── backend                 \* BACKEND CODE *\      
│   ├── README.md
│   ├── api_docs                        \* API DOCUMENTATIONS *\      
│   │   ├── create_category.md
│   │   ├── create_transaction.md
│   │   ├── delete_category.md
│   │   ├── delete_transaction.md
│   │   ├── get_category.md
│   │   ├── get_transactions.md
│   │   ├── search_category.md
│   │   ├── search_transactions.md
│   │   ├── update_category.md
│   │   └── update_transaction.md
│   ├── auth                            \* Authentication module *\  
│   │   └── __init__.py
│   ├── config.py                       \* Flask App Config *\  
│   ├── load_sample.py                  \* File to load samples to database *\  
│   ├── models                          \* Flask models module *\  
│   │   ├── models.py                   
│   │   ├── request_schema.py
│   │   └── respond_schema.py
│   ├── money_app                       \* Flask App *\  
│   │   ├── __init__.py
│   │   ├── controllers                 \* All controllers file under this folder *\  
│   │   └── error_handler.py            \* Define app error handler *\ 
│   ├── requirements.txt                \* Python libraries used in this project *\
│   ├── run_test.sh                     \* Script to run backend test *\
│   ├── setup_db.sh                     \* Script to initialize database *\
│   ├── test_flask.py
│   └── utils.py                        \* Util functions used in this project *\
```

### Backend

The `./backend` directory contains a partially completed Flask server.

[View the README.md within ./backend for more details.](./backend/README.md)


### Authentication
This project uses [Auth0](https://auth0.com/) for Authentication purposes.

[View the README.md within ./auth0 for more details.](./auth0/README.md)

