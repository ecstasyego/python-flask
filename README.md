# python-flask
`flask`
```python
from flask import Flask, request, redirect, url_for, render_template, session, flash, jsonify, g, abort, make_response
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from flask_wtf import FlaskForm
from flask_migrate import Migrate
from flask_mail import Mail, Message
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
```

`fastapi`
```python
from fastapi import FastAPI
```

`sqlalchemy`
```python
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship, backref
```

`dash`
```python
import dash
from dash import dcc, html
```

`wtforms`
```python
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length
```

`authlib`
```python
from authlib.integrations.flask_client import OAuth
```



<hr>

`Server`
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # header = request.headers
    # body = request.get_json()

    print(f"Received request: {request.method} {request.path}")
    print(f"Headers: {request.headers}")

    return jsonify(["Hello, World!"])

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
```
`Client`
```bash
$ curl http://127.0.0.1:5000
```

<br><br><br>

## Information Provider(IP)
- IANA (Internet Assigned Numbers Authority)
    - RIRs (Regional Internet Registries)
        - ISP (Internet Service Provider)

**RIRs (Regional Internet Registries)**
- ARIN (American Registry for Internet Numbers)
- RIPE NCC (Réseaux IP Européens Network Coordination Centre)
- APNIC (Asia-Pacific Network Information Centre)
- LACNIC (Latin America and Caribbean Network Information Centre)
- AFRINIC (African Network Information Centre)


<br>

### IP
`IP`
```bash
# on Linux
$ ifconfig # Private IP
$ hostname -I # Private IP
$ curl ifconfig.me # Public IP
$ whois [Public IP]
```
```dos
# on Windows
> ipconfig # Private IP
> curl ifconfig.me # Public IP
```

### Subnet Mask
```
[NETWORK].[HOST]/[SUBNETMASK]
```


<br><br><br>

## Protocols
### HTTP: HyperText Transfer Protocol
#### REQUEST
`Method`
```
GET
The GET method requests that the target resource transfer a representation of its state. GET requests should only retrieve data and should have no other effect. (This is also true of some other HTTP methods.) For retrieving resources without making changes, GET is preferred over POST, as they can be addressed through a URL. This enables bookmarking and sharing and makes GET responses eligible for caching, which can save bandwidth. The W3C has published guidance principles on this distinction, saying, "Web application design should be informed by the above principles, but also by the relevant limitations."See safe methods below.

HEAD
The HEAD method requests that the target resource transfer a representation of its state, as for a GET request, but without the representation data enclosed in the response body. This is useful for retrieving the representation metadata in the response header, without having to transfer the entire representation. Uses include checking whether a page is available through the status code and quickly finding the size of a file (Content-Length).

POST
The POST method requests that the target resource process the representation enclosed in the request according to the semantics of the target resource. For example, it is used for posting a message to an Internet forum, subscribing to a mailing list, or completing an online shopping transaction.

PUT
The PUT method requests that the target resource create or update its state with the state defined by the representation enclosed in the request. A distinction from POST is that the client specifies the target location on the server.

DELETE
The DELETE method requests that the target resource delete its state.

CONNECT
The CONNECT method requests that the intermediary establish a TCP/IP tunnel to the origin server identified by the request target. It is often used to secure connections through one or more HTTP proxies with TLS. See HTTP CONNECT method.

OPTIONS
The OPTIONS method requests that the target resource transfer the HTTP methods that it supports. This can be used to check the functionality of a web server by requesting '*' instead of a specific resource.

TRACE
The TRACE method requests that the target resource transfer the received request in the response body. That way a client can see what (if any) changes or additions have been made by intermediaries.

PATCH
The PATCH method requests that the target resource modify its state according to the partial update defined in the representation enclosed in the request. This can save bandwidth by updating a part of a file or document without having to transfer it entirely.
```
```bash
$ curl 127.0.0.1:5000 # [body]
$ curl -i 127.0.0.1:5000 # --include # [header&body]
$ curl -I 127.0.0.1:5000 # --head # [header]
$ curl -s 127.0.0.1:5000 # --silent # [body]
$ curl -L 127.0.0.1:5000 # --location # [redirection]
```
```bash
$ curl 127.0.0.1:5000 # [GET|BODY]
$ curl -I 127.0.0.1:5000 # [GET|HEADER]
$ curl -X GET 127.0.0.1:5000 # [GET|BODY]
$ curl -X GET 127.0.0.1:5000?Key=Value # [GET]: Read
$ curl -X POST -d "Key=Value" 127.0.0.1:5000 # [POST]: Create, Append
$ curl -X PUT -d '{"Key":"Value"}' 127.0.0.1:5000 # [PUT]: Update All
$ curl -X PATCH -d '{"Key":"Value"}' 127.0.0.1:5000 # [PATCH]: Update Partial
$ curl -X DELETE 127.0.0.1:5000 # [DELETE]: Delete
$ curl -X OPTIONS 127.0.0.1:5000 # [OPTIONS]
```

##### Query String
```bash
$ curl [URL(Uniform Resource Locator)]
$ curl [Scheme://User@Host:Port/Path?Query#Fragment]
$ curl [Scheme://User@Host:Port/Path?Key1=Value1#Fragment]
$ curl [Scheme://User@Host:Port/Path?Key1=Value1&Key2=Value2#Fragment]
$ curl -G -d "Key1=Value1" -d "Key2=Value2" [Scheme://User@Host:Port/Path#Fragment]
$ curl -X POST -d "Key1=Value1&Key2=Value2" [Scheme://User@Host:Port/Path#Fragment]
```


#### RESPONSE: Header & Body
```
1XX (informational)
The request was received, continuing process.

2XX (successful)
The request was successfully received, understood, and accepted.

3XX (redirection)
Further action needs to be taken in order to complete the request.

4XX (client error)
The request contains bad syntax or cannot be fulfilled.

5XX (server error)
The server failed to fulfill an apparently valid request.
```


### HTTPS: Hypertext Transfer Protocol over Secure Sockets Layer
#### Let’s Encrypt
```
```


<br><br><br>

### Examples

#### bash-curl
```bash
```


#### bash-wget
```bash
```

#### python-requests
```python
import requests

requests.get("http://localhost:5000").json()
requests.get("http://localhost:5000", params={"Key": "Name"}).json() # Query String
requests.post("http://localhost:5000", data={"Key01": "Value01", "Key02": "Value02"}).json()
requests.put("http://localhost:5000", json={"Key01": "Value01", "Key02": "Value02"}).json()
requests.patch("http://localhost:5000", json={"Key01": "Value01", "Key02": "Value02"}).json()
requests.delete("http://localhost:5000").json()
```

#### kotlin-retrofit2
##### server
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(['Hello, World!'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

##### on emulator
`file system`
```
.Project
├── app
│   ├── src
│   │   └── main
│   │       ├── java/com/example/myapplication/MainActivity.kt
│   │       ├── res/xml/network_security_config.xml
│   │       └── AndroidManifest.xml
│   └── build.gradle.kts # APP-LEVEL
└── build.gradle.kts # PROJECT-LEVEL
```

`AndroidManifest.xml`
```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">

    <uses-permission android:name="android.permission.INTERNET"/>
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>

    <application
        android:networkSecurityConfig="@xml/network_security_config"
    </application>

</manifest>
```

`network_security_config.xml`
```xml
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <domain-config cleartextTrafficPermitted="true">
        <domain includeSubdomains="true">10.0.2.2</domain>
    </domain-config>
</network-security-config>
```


`MainActivity.kt`
```kotlin
package com.example.myapplication

import android.os.Bundle
import android.util.Log
import android.widget.TextView
import androidx.activity.ComponentActivity
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.GET

interface ApiService {
    @GET("/")
    fun getData(): Call<List<String>>
}

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val textView = TextView(this)
        setContentView(textView)

        val retrofit = Retrofit.Builder()
            .baseUrl("http://10.0.2.2:5000/")
            .addConverterFactory(GsonConverterFactory.create())
            .build()

        val apiService = retrofit.create(ApiService::class.java)
        apiService.getData().enqueue(object : Callback<List<String>> {
            override fun onResponse(call: Call<List<String>>, response: Response<List<String>>) {
                if (response.isSuccessful) {
                    textView.text = response.body().toString()
                    Log.d("Retrofit", "Response Success")
                } else {
                    Log.e("Retrofit", "Response Error: ${response.code()} - ${response.message()}")
                }

            }

            override fun onFailure(call: Call<List<String>>, t: Throwable) {
                Log.e("Retrofit", "API Request Failure: ${t.message}")
            }
        })

    }
}
```

`build.gradle.kts(APP-LEVEL)`
```kotlin
dependencies {
    implementation("com.squareup.retrofit2:retrofit:2.9.0")
    implementation("com.squareup.retrofit2:converter-gson:2.9.0")
    implementation("com.squareup.retrofit2:converter-scalars:2.9.0")
    implementation("com.squareup.okhttp3:okhttp:4.9.3")
}
```


<br><br><br>

# SERVER

## Application

- WSGI(Web Server Gateway Interface)
    - Flask(API)
    - Flask(API) + Gunicorn(Mutli-Threading)
    - Flask(API) + Gunicorn(Mutli-Threading) + Nginx(Reverse Proxy; SSL)
    - Flask(API) + Gunicorn(Mutli-Threading) + Nginx(Reverse Proxy; SSL) + CDN(Clouded Cache)
    - Flask(API) + Gunicorn(Mutli-Threading) + Nginx(Reverse Proxy; SSL) + CDN(Clouded Cache) + OpenVPN(Security)
- ASGI(Asynchronous Server Gateway Interface)
    - FastAPI + [Uvicorn|Hypercorn|Daphne]
    - FastAPI + [Uvicorn|Hypercorn|Daphne] + Gunicorn(Mutli-Threading)
    - FastAPI + [Uvicorn|Hypercorn|Daphne] + Gunicorn(Mutli-Threading) + Nginx(Reverse Proxy)
    - FastAPI + [Uvicorn|Hypercorn|Daphne] + Gunicorn(Mutli-Threading) + Nginx(Reverse Proxy) + CDN(Clouded Cache)
    - FastAPI + [Uvicorn|Hypercorn|Daphne] + Gunicorn(Mutli-Threading) + Nginx(Reverse Proxy) + CDN(Clouded Cache) + OpenVPN(Security)

### Automation: systemd


#### Flask
`script.py`
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Flask!'

if __name__ == "__main__":
    app.run(debug=True)
```

- **Server: Development**
```bash
$ python script.py
```

- **Server: Production**
```bash
$ gunicorn script:app
$ gunicorn script:app -b 0.0.0.0:8050
$ gunicorn script:app -b 0.0.0.0:8050 -w 4
$ gunicorn script:app --bind 0.0.0.0:8050 --workers 4
```


<br>


#### Dash

`script.py`
```python
import dash
from dash import dcc, html

app = dash.Dash(__name__)
app.title = "APP PAGE TITLE"
app.layout = html.Div("Hello, world!")

server = app.server # Gunicorn

if __name__ == '__main__':
    app.run(debug=True)
```

- **Server: Development**
```bash
$ python script.py
```

- **Server: Production**
```bash
$ gunicorn script:server
$ gunicorn script:server -b 0.0.0.0:8000
$ gunicorn script:server -b 0.0.0.0:8000 -w 4
```

<br>

#### FastAPI

`script.py`
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, FastAPI!"}
```

- **Server: Development**
```bash
$ uvicorn script:app --reload
```

- **Server: Production**
```bash
$ uvicorn script:app
$ uvicorn script:app --host 0.0.0.0 --port 8000
$ uvicorn script:app --host 0.0.0.0 --port 8000 --workers 4
```
```bash
$ gunicorn -k uvicorn.workers.UvicornWorker script:app
```

<br>

#### Flask + Dash

`script.py`
```python
from dash import Dash, html
from flask import Flask


# Flask Application
flask_app = Flask(__name__)

@flask_app.route('/')
def hello():
    return 'Hello from Flask!'

# Dash Application
dash_app = Dash(__name__, server=flask_app, url_base_pathname="/dash/")
dash_app.layout = html.Div([
    html.H1("Hello from Dash!"),
    html.P("This is a Dash app running under Flask.")
]) # Integration: dash_app + flask_app


if __name__ == "__main__":
    flask_app.run(debug=True)
```

- **Server: Development**
```bash
$ python script.py
```

- **Server: Production**
```bash
$ gunicorn script:flask_app
$ gunicorn script:flask_app -b 0.0.0.0:5000
$ gunicorn script:flask_app -b 0.0.0.0:5000 -w 4
```

<br>

#### Flask + FastAPI

`script.py`
```python
from fastapi import FastAPI
from flask import Flask
from asgiref.wsgi import WsgiToAsgi
from starlette.middleware.wsgi import WSGIMiddleware



# Flask Application
flask_app = Flask(__name__)

@flask_app.route("/")
def flaskAPI():
    return "Hello from Flask!"



# FastAPI Application
fastapi_app = FastAPI()

@fastapi_app.get("/fastapi")
def fastapiAPI():
    return {"message": "Hello from FastAPI"}



# Integration: fastapi_app + flask_app
fastapi_app.mount("/", WSGIMiddleware(flask_app))

# Main Application
app = fastapi_app
```

- **Server: Development**
```bash
$ uvicorn sciprt:app --reload
```

- **Server: Production**
```bash
$ uvicorn script:app
```
```bash
$ gunicorn -k uvicorn.workers.UvicornWorker script:app
$ PYTHONPATH=/~/~/~/lib/python3.12/site-packages gunicorn -k uvicorn.workers.UvicornWorker script:app
```


<br>


#### Flask + Dash + FastAPI

`script.py`
```python
from dash import Dash, html
from fastapi import FastAPI
from flask import Flask
from asgiref.wsgi import WsgiToAsgi
from starlette.middleware.wsgi import WSGIMiddleware



# Flask Application
flask_app = Flask(__name__)

@flask_app.route("/")
def flaskAPI():
    return "Hello from Flask!"



# Dash Application
dash_app = Dash(__name__, server=flask_app, url_base_pathname="/dash/")
dash_app.layout = html.Div([
    html.H1("Hello from Dash!"),
    html.P("This is a Dash app running under Flask.")
]) # Integration: dash_app + flask_app



# FastAPI Application
fastapi_app = FastAPI()

@fastapi_app.get("/fastapi")
def fastapiAPI():
    return {"message": "Hello from FastAPI"}



# Integration: fastapi_app + flask_app
fastapi_app.mount("/", WSGIMiddleware(flask_app))

# Main Application
app = fastapi_app
```

- **Server: Development**
```bash
$ uvicorn sciprt:app --reload
```

- **Server: Production**
```bash
$ uvicorn script:app
```
```bash
$ gunicorn -k uvicorn.workers.UvicornWorker script:app
$ PYTHONPATH=/~/~/~/lib/python3.12/site-packages gunicorn -k uvicorn.workers.UvicornWorker script:app
```



<br><br><br>


## Network
- Private IP / Public IP
    - Redirection / Proxy

### Proxy  
#### Nginx Forward Proxy: Inside to Outside 
#### Nginx Reverse Proxy: Outside to Inside 

### HTTPs 
#### Certbot

### CDN(Clouded Cache)
#### varnish

### Virtual Private Network(VPN)
#### WireGuard
#### OpenVPN


