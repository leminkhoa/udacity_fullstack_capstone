from datetime import datetime, timezone
from money_app import create_app
from models.models import *

UTC = timezone.utc

#  Transaction Type
#  ----------------------------------------------------------------


transaction_type_1 = TransactionType(
    id = '1',
    type = 'Cash Out'
)

transaction_type_2 = TransactionType(
    id = '2',
    type = 'Cash In'
)

#  Category
#  ----------------------------------------------------------------


category_1 = Category(
    id = '1',
    transaction_type_id = '1',
    type = 'Food'
)

category_2 = Category(
    id = '2',
    transaction_type_id = '1',
    type = 'Health'
)

category_3 = Category(
    id = '3',
    transaction_type_id = '1',
    type = 'Transportation'
)

category_4 = Category(
    id = '4',
    transaction_type_id = '1',
    type = 'Apparel'
)

category_5 = Category(
    id = '5',
    transaction_type_id = '2',
    type = 'Salary'
)

category_6 = Category(
    id = '6',
    transaction_type_id = '2',
    type = 'Saving Interest'
)


#  User
#  ----------------------------------------------------------------

user_1 = User(
    id = '1',
    name = 'Test User 1'
)

user_2 = User(
    id = '2',
    name = 'Test User 2'
)


#  Transaction
#  ----------------------------------------------------------------

transaction_1 = Transaction(
    id = '1',
    user_id = '1',
    category_id = '2',
    date = datetime(2022, 1, 2, 3, 30, 0, tzinfo=UTC),
    amount = 100,
    currency = '$',
)

transaction_2 = Transaction(
    id = '2',
    user_id = '1',
    category_id = '4',
    date = datetime(2022, 1, 15, 0, 0, 0, tzinfo=UTC),
    amount = 250,
    currency = '$',
)

transaction_3 = Transaction(
    id = '3',
    user_id = '1',
    category_id = '5',
    date = datetime(2022, 1, 17, 0, 0, 0, tzinfo=UTC),
    amount = 8000,
    currency = '$',
)

transaction_4 = Transaction(
    id = '4',
    user_id = '2',
    category_id = '1',
    date = datetime(2022, 1, 15, 0, 0, 0, tzinfo=UTC),
    amount = 10,
    currency = '$',
)


# Set up
app = create_app()
# Load sample records
recs = [
    transaction_type_1, transaction_type_2,
    category_1, category_2, category_3, category_4, category_5, category_6,
    user_1, user_2,
    transaction_1, transaction_2, transaction_3, transaction_4
] 
db.session.bulk_save_objects(recs)
db.session.commit()
print("Sample records have been successfully added!")
