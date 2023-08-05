
# bottle-jsonschema

Bottle plugin for automatically validating JSON schemas for all relevant
requests.

## Installation

    pip install bottle_jsonschema

## Usage example

```python
import bottle
from bottle.ext.jsonschema import JSONSchemaPlugin, SchemaValidationError

bottle.install(JSONSchemaPlugin())

@bottle.error(400)
def handle_error_400(error):
    # This forwards the error directly to the user, which will display a nicely
    # formatted JSON object containing the validation errors.
    if isinstance(error, SchemaValidationError):
        return response

    # Handle other error situations...

    return json.dumps({"error": "invalid request"})
```

The error object contains a list of strings describing the validation errors.
You can easily customize how the errors are displayed, here's how you can
display them as a HTML list:

```python
@bottle.error(400)
def handle_error_400(error):
    if isinstance(error, SchemaValidationError):
        response.content_type = "text/html"

        error_list = "\n".join(
            "<li>{}</li>".format(x) for x in error.validation_errors
        )

        return """
            <h1>JSON schema validation failed</h1>
            <p>Errors:</p>
            <ul>{}</ul>
        """.format(error_list)

    return response
```

## Output samples

Here are some samples of the output of the plugin, given the following error
handler:

```python
@bottle_app.error(400)
def handle_error_400(error):
    if isinstance(error, SchemaValidationError):
        return response

    response.content_type = "application/json"
    return json.dumps({"error": error.body})
```

```
$ curl -s -X PUT "http://127.0.0.1:1300/login" | jq .
{
  "error": "content type application/json required"
}
```

```
$ curl -s -X PUT -H "Content-Type: application/json" "http://127.0.0.1:1300/login" | jq .
{
  "error": "json payload required"
}
```

```
$ curl -s -X PUT -H "Content-Type: application/json" -d '{}' "http://127.0.0.1:8080/login" | jq .
{
  "error": "payload failed json schema validation",
  "validation_errors": [
    "failed constraint: required: ['email', 'password']"
  ]
}
```

```
$ curl -s -X PUT -H "Content-Type: application/json" -d '{"email": "x", "password": "123"}' "http://127.0.0.1:1300/login" | jq .
{
  "error": "payload failed json schema validation",
  "validation_errors": [
    "failed constraint: properties.password.minLength: 8",
    "failed constraint: properties.email.minLength: 6"
  ]
}
```

```
$ curl -s -X PUT -H "Content-Type: application/json" -d '{"email": "hubro@example.net", "password": "12345678"}' "http://127.0.0.1:1300/login" | jq .
{
  "code": "success"
}
```

## More information

Here's basically everything the plugin does for every request:

1. Check the HTTP method of the request. If it's one of POST, PATCH or PUT, then
   continue. Otherwise stop.
1. Try to find a schema for the request. If a schema was found, continue,
   otherwise stop. The default logic for finding a schema is explained below,
   and can be overridden.
1. Check that the request content type is "application/json". If it's not, raise
   a 400 Bad Request error.
1. Check that the request contains a JSON parseable payload. If not, raise a 400
   Bad Request error.
1. Validate the payload using
   [jsonschema](https://github.com/Julian/jsonschema). If there were no errors,
   stop. Otherwise raise a 400 Bad Request error.

### How do I override which HTTP methods trigger schema validation?

```python
bottle.install(JSONSchemaPlugin(methods=("GET", "POST")))
```

### How does the plugin find schemas?

By default, the plugin finds schemas by checking your Bottle application's
resource manager for "schemas/&lt;name&gt;.json". The default strategy for converting
a route to a schema name is:

```
PUT /login                      -> schemas/login[.PUT].json
POST /admin/users               -> schemas/admin.users[.POST].json
PUT /admin/users/<id:int>       -> schemas/admin.users.id[.POST].json
PATCH /users/<name:re:\w(@\w)?> -> schemas/users.name[.PATCH].json
```

Basically, it replaces slashes with dots, replaces wildcards with the wildcard
name and strips leading and trailing slashes. The HTTP method is optional, as
signified by the square brackets.

You can override the naming strategy like this:

```python
def get_schema_name():
    # Generate one or more schema names for the current request.

    return ["list", "of", "names", "that", "will", "be", "tried", "in", "order"]

bottle.install(JSONSchemaPlugin(schema_name=get_schema_name))
```

Or you can override the whole schema lookup altogether:

```python
def find_schema():
    # Find the correct schema for the current request and return it as a dict.

    # Returning None will skip schema validation.
    return None

bottle.install(JSONSchemaPlugin(schema_lookup=find_schema))
```

### How do I set up the resource manager to work with this plugin?

Assuming you have a project folder layout like this:

```
.
├── assets
│   └── schemas
│       └── login.json
└── myapp.py
```

Then you just need this line:

```python
app.resources.add_path("assets/")
```

Or, if you're using the default app:

```python
bottle.default_app().resources.add_path("assets/")
```

Now JSONSchemaPlugin will validate requests against your schemas without any
further configuration. You can make it work with any project layout by
overriding the schema naming strategy as explained above, or you can skip the
resource manager altogether by overriding the schema lookup function.
