# Create A Category

**Description** : Endpoint to POST a new category.

**URL** : `/categories`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : `create:category`

**Data constraints** : 
Provide transaction type id and category name.
```
{
    "transaction_type_id": <str: Id of transaction type>,
    "type": <str: Category name>,
}
```

**Data Example** :
```json
{
    "transaction_type_id": "1",
    "type": "Utilities"
}
```

## Success Responses

**Code** : `200 OK`

**Content** : 

```json
{
    "created": "214f2a1e-6a5c-11ed-b0a5-00155dc01804",
    "success": true,
    "total_categories": 7
}
```
