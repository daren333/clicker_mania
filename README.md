# clicker_mania

create conda env:
```
conda env create -f environment.yml
conda activate clickermania
```

spin up local docker container
```
docker run -d --name mysql-container -e MYSQL_ROOT_PASSWORD=mysecretpassword -p 3306:3306 mysql:latest
```

Run app in development mode:
```
FLASK_APP=src.app FLASK_CONFIG=development flask run
```