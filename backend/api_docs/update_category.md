# Create A Category

**Description** : Endpoint to UPDATE a category.

**URL** : `/categories/<category-id>`

**Method** : `PATCH`

**Auth required** : YES

**Permissions required** : `update:category`

**Data constraints** : 
Provide transaction type id and category name.

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
    "transaction_type_id": "1",
    "type": "something"
}
```

## Success Responses

**Code** : `200 OK`

**Content** : 

```json
{
    "category": {
        "id": "1",
        "transaction_type_id": "1",
        "type": "something"
    },
    "success": true
}
```
