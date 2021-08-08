# actions_pytest
Actions GitHub en Gitpod y Docker 

## Docker image
docker build -t python_pytest:v1 .

## Container
docker run -it -v /workspace/actions_pytest/pruebas:/pruebas -p 8080 --name python -h python python_pytest:v1