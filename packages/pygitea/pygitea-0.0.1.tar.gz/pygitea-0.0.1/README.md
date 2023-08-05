# Pygitea
[Gitea API](https://try.gitea.io/api/swagger) wrapper for Python (3 only).


## Install
```bash
pip install pygitea
```


## Basic usage
```python
import pygitea

api = pygitea.API('http://192.168.100.10:3000')
api.get('/version')
api.get('/orgs/an-organisation/members')
```

### Authentification token
Setup authentification token:

```python
import pygitea
api = pygitea.API('http://192.168.100.10:3000', token="AUTH-TOKEN")
api.delete('/admin/users/arount')
```

### Main API methods
```python
api.get('route')   # Send GET query to route
api.post('route')  # Send POST query to route
api.patch('route') # Send PATCH query to route
api.put('route')   # Send PUT query to route
```

### Alternative API method
```python
# Send GET query to route with parameters
api.call('route', method='get', params={"body": "Egg, bacon, sausages and SPAM")
```

## Exceptions


Exceptions are raised before sending query. If API respond error message no exception will be raised (for the moment, at least)


### Authentification token


If auth token is not set when you are trying to access to a protected resource:

```python
api = pygitea.API('http://192.168.100.10:3000')
api.delete('/admin/users/arount')
```


```
pygitea.PygiteaRequestException: Resource '/admin/users/{username}' require an authentification token.
```


### Resource do not exists


```python
api.get('/fake/route')
```


```
pygitea.PygiteaRequestException: Path '/fake/route' did not match with any resource
```


### Method do not exists for resource


```python
api.delete('/markdown')
```


```
pygitea.PygiteaRequestException: Resource '/markdown' did not expect method DELETE
```

