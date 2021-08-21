# EstudiApp

[![Build Status](https://gitlab.com/ds4a_team81/saber_pro_front/badges/master/pipeline.svg)](https://gitlab.com/ds4a_team81/saber_pro_front)

[EstudiApp](http://ds4a-2020-1183523121.us-east-1.elb.amazonaws.com "EstudiApp Frontend") is a Data Science powered tool that let the Colombian education community to find risks and improvement opportunities against the Sber Pro tests.

![image info](./assets/FrontendView.png)

## Folder structure

```
project_root/
│
├── assets/               # Project assets and styles (css)
├── data/                 # Data connectors, queries and DAO
├── graphs/               # Functions to create some figures
├── html_objects/         # HTML layouts for each page
├── app.py                # Main Dash file / Callbacks
├── Dockerfile            # Docker instructions to build the project
├── requirements.txt      # Requirements for the Dash app
```

## Installation

To manually install the Dash app you need to execute

```sh
cd saber_pro_front
pip install -r requirements
python app.py
```

Make sure you have your environment variables setted

## Environment variables

In order to connect to the database and to upload the client's custom csv files, the project needs the following environmet variables at the moment of run the app

| Environment Variable | Description |
| ------ | ------ |
| AWS_ACCESS_KEY_ID | The AWS key to access S3 upload services |
| AWS_DEFAULT_REGION | Default Region where the AWS client will connect to |
| AWS_SECRET_ACCESS_KEY | Secret provided with the AWS Key Id |
| DB_HOST | Database url |
| DB_NAME | Database name |
| DB_PASS | Database password |
| DB_PORT | Database port |
| DB_USER | Database username |
| DEBUG | Boolean value to de/activate the Debug mode of Dash |

## Docker

EstudiApp is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8050, so change this within the Dockerfile if necessary. When ready, simply use the Dockerfile to build the image.

```sh
cd saber_pro_front
docker build -t estudiapp .
```

This will create the EstudiApp image and pull in the necessary dependencies.

Once done, run the Docker image and map the port to whatever you wish on your host. In this example, we simply map port 8000 of the host to port 8050 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8050 estudiapp
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```

### Todos

- To make EstudiApp the next Skynet
- Add Light Mode

License

----

MIT
