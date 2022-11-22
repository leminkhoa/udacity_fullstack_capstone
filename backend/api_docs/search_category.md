# Search Transactions

**Description** : Endpoint to get filtered categories based on search term.


**URL** : `/categories/search`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : `get:category`


**Data constraints** : 
Provide `start_date` and `end_date`
```
{
    "searchTerm": <str: Category name to filter results>,
}
```

**Data Example** :
```json
{
    "searchTerm": "Food"
}
```

## Success Responses

**Code** : `200 OK`

**Content** : 

```json
{
    "categories": {
        "1": {
            "transaction_type": "Cash Out",
            "transaction_type_id": "1",
            "type": "Food"
        }
    },
    "success": true,
    "total_categories": 1
}
```
