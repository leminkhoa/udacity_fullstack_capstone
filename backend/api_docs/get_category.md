# Get Transactions

**Description** : Endpoint to handle GET requests for categories.

**URL** : `/categories`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : `get:category`

**Data constraints** : `{}`

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
        },
        "2": {
            "transaction_type": "Cash Out",
            "transaction_type_id": "1",
            "type": "Health"
        },
        ...
    },
    "success": true,
    "total_categories": 7
}
```