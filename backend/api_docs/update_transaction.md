# Create A Transaction

**Description** : Endpoint to UPDATE a transaction.

**URL** : `/transactions/<transaction-id>`

**Method** : `PATCH`

**Auth required** : YES

**Permissions required** : `update:transaction`

**Data constraints** : 
Provide category id, date, amount, currency and note for updating a new transaction
```
{
    "category_id": <str: Category id>,
    "date": <str: Datetime with timezone in isoformat>,
    "amount": <int: Amount of money>,
    "currency": <str: Currency>
    "note": <str (Optional): Note for this transaction>
}
```

**Data Example** :
```json
{
    "category_id": "1",
    "date": "2022-03-03T15:00:00Z",
    "amount": 7,
    "currency": "$",
    "note": "dummy note"
}
```

## Success Responses

**Code** : `200 OK`

**Content** : 

```json
{
    "created": "1337e1c2-6a58-11ed-a141-00155dc01804",
    "success": true
}
```
