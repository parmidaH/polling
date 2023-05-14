# polling
This is a polling app with python and html

# Run the project with docker by the command below
$ docker build -t polling-app .

$ docker run -p 5000:5000 polling-app
# Run the project with kubernetes and helm by the command below
$ helm package polling-app

$ helm install polling-app ./polling-app-0.1.0.tgz
