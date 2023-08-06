# ClusterAPI
Build ClusterAPI using Flask and Flask-restful, with token based authentication.

## Install
Install and configure HA cluster firstly,
Then
```
pip3 install -r requirements.txt
python3 api.py
```

## Register
```
curl http://server:5000/api/v1/register -d "username=name&password=xxxx" -X POST
```

## Cluster api
```
curl http://server:5000/api/v1/cluster -H "Authenticate: Token token_string"
```

## Node api
```
curl http://server:5000/api/v1/nodes -H "Authenticate: Token token_string"
curl http://server:5000/api/v1/nodes/nodename -H "Authenticate: Token token_string"
```

## Resource api
```
curl http://server:5000/api/v1/resources -H "Authenticate: Token token_string"
```
