# Label Microservice

## Build

Create a virtual environment

```
python -m venv myvenv
myvenv/Scripts/activate
```

Install flask
```
pip install flask
```

Install from requirements:
```
pip install -r requirements.txt
```

freeze packages:
```
pip freeze > requirements.txt
```


## Run

```
python ./src/app.py
```

To test, visit 

http://127.0.0.1:7000/
http://127.0.0.1:7000/details/<tag>
