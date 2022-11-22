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

#  Transaction
#  ----------------------------------------------------------------

transaction_1 = Transaction(
    id = '1',
    category_id = '2',
    date = '2022-01-02T5:00:00+00:00',
    amount = 100,
    currency = '$',
    note = 'dummy note',
)

transaction_2 = Transaction(
    id = '2',
    category_id = '4',
    date = '2022-01-03T6:30:00+07:00',
    amount = 250,
    currency = '$',
    note = 'dummy note',
)

transaction_3 = Transaction(
    id = '3',
    category_id = '5',
    date = '2022-01-30T15:30:00+00:00',
    amount = 8000,
    currency = '$',
    note = 'dummy note',
)

transaction_4 = Transaction(
    id = '4',
    category_id = '1',
    date = '2022-02-15T15:30:00+00:00',
    amount = 10,
    currency = '$',
    note = 'dummy note',
)

transaction_5 = Transaction(
    id = '5',
    category_id = '1',
    date = '2022-01-23T15:30:00+00:00',
    amount = 10,
    currency = '$',
    note = 'dummy note',
)


transaction_6 = Transaction(
    id = '6',
    category_id = '4',
    date = '2022-01-12T18:00:30+00:00',
    amount = 300,
    currency = '$',
    note = 'dummy note',
)

# Set up
app = create_app()
# Load sample records
recs = [
    transaction_type_1, transaction_type_2,
    category_1, category_2, category_3, category_4, category_5, category_6,
    transaction_1, transaction_2, transaction_3, transaction_4, transaction_5, transaction_6,
] 

try:
    db.session.bulk_save_objects(recs)
    db.session.commit()
    print("Sample records have been successfully added!")
except Exception:
    print("Sample records have already been loaded. Skip this step!")
