# Blog
This is a blog with Django


## Use database Postgresql with docker

```docker
docker run --name blog-postgres -p 5432:5432 -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=postgres -d postgres:alpine

docker exec blog-postgres env  -> show env of container

docker exec -it blog-postgres psql -U user -W postgres -> -U [POSTGRES_USER] -W [POSTGRES_DB]

then enter the password and run these command

CREATE EXTENSION pg_trgm;
```