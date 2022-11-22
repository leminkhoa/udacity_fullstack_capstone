# Search Transactions

**Description** : Endpoint to get filtered transactions. It should return any transactions between provided start date and end date


**URL** : `/transactions/search`

**Method** : `POST`

**Query Params**: 
- page: Page number to be shown (Default: 1)

**Pagination**: 10 items per page

**Auth required** : YES

**Permissions required** : `get:transaction`


**Data constraints** : 
Provide `start_date` and `end_date`
```
{
    "start_date": <str: date in isoformat>,
    "end_date": <str: date in isoformat>,
}
```
*Note: results returned are filtered between [start_date, end_date).*

**Data Example** :
```json
{
    "start_date": "2022-01-30T22:30:00+07:00",
    "end_date": "2022-02-03T22:30:00+07:00"
}
```

## Success Responses

**Code** : `200 OK`

**Content** : 

```json
{
    "success": true,
    "total_transactions": 1,
    "transactions": [
        {
            "amount": 8000.0,
            "category_id": "5",
            "currency": "$",
            "date": "2022-01-30 22:30:00+07:00",
            "id": "3",
            "note": "dummy note"
        }
    ]
}
```
