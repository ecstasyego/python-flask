# python-flask
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
```


## HTTP
### bash-curl
```bash
$ curl -X GET 127.0.0.1:5000
```

### python-requests
```python
import requests

response = requests.get("http://127.0.0.1:5000")
response.json()
```

### kotlin-retrofit2
```kotlin
```
