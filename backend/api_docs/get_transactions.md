# Get Transactions

**Description** : Endpoint to handle GET requests for transactions.

**URL** : `/transactions`

**Method** : `GET`

**Query Params**: 
- page: Page number to be shown (Default: 1)

**Pagination**: 10 items per page

**Auth required** : YES

**Permissions required** : `get:transaction`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : 

```json
{
    "success": true,
    "total_transactions": 6,
    "transactions": [
        {
            "amount": 10.0,
            "category_id": "1",
            "currency": "$",
            "date": "2022-02-15 22:30:00+07:00",
            "id": "4",
            "note": "dummy note"
        },
        {
            ...
        }
}
```