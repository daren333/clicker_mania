# clicker_mania

create conda env:
```
conda env create -f environment.yml
conda activate clickermania
```

### Running app locally:

spin up local database via docker
```
docker run -d --name mysql-container -e MYSQL_ROOT_PASSWORD=example -p 3306:3306 -v src/utils/mysql_init.sql:/docker-entrypoint-initdb.d mysql:latest 
```

Run app locally in development mode:
```
FLASK_APP=src.app FLASK_CONFIG=development flask run
```

### Running app via docker-compose
Start docker containers
```
docker-compose up --build -d
```

Ensure containers are running
```
docker ps
```

Exec into the application container:
```
docker exec -it clicker_mania-clicker_mania-1 bash
```

Try hitting localhost:
```
curl localhost:5000/users/health
```