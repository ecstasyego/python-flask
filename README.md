# python-flask
`Server`
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
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
$ curl 127.0.0.1:5000 # [GET]
$ curl -I 127.0.0.1:5000 # [HEAD]
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

response = requests.get("http://127.0.0.1:5000")
response.json()
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

## Server
### Flask(API) + Gunicorn(Mutli-Threading) + Nginx(Proxy)


