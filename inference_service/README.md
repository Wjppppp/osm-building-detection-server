# Label Microservice

## Build

Docker

```
docker build -t inference-service:<TAG> .
```

```shell
docker run --name inference inference-service:<TAG>
# bind mount
docker run -it --gpus all --name inference -p 8888:8888 -p 6006:6006 --mount type=bind,source="$(pwd)",target=/app inference-service:<TAG>
```

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
