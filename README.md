# polling
This is a polling app with python and html

# If You want to run this project by docker run the command below
$ docker build -t polling-app .

$ docker run -p 5000:5000 polling-app
# If you want to run this project by kubernetes and helm run the command below
$ helm package polling-app

$ helm install polling-app ./polling-app-0.1.0.tgz
