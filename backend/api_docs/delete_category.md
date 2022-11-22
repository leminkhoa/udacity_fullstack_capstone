# Delete A Category

**Description** : Endpoint to DELETE a category.

**URL** : `/categories/<category-id>`

**Method** : `DELETE`

**Auth required** : YES

**Permissions required** : `delete:category`

**Data constraints** : `{}`


## Success Responses

**Code** : `200 OK`

**Content** : 

```json
{
    "deleted": "1337e1c2-6a58-11ed-a141-00155dc01804",
    "success": true
}
```
