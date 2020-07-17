# How to run Bank Note Authentication with Docker

- First of all Pull this whole Repository to your local system.
- Install Docker from [this link](https://docs.docker.com/get-docker/). (Make sure to read system requirements before proceeding to installation)
- Open Docker Quickstart Terminal.
- Navigate to directory of this repository path.
- Build Docker Image with command below. (Where 'money_api' is image name and '.' is current path.)

```bash
docker build -t money_api .
```
- Now to run the image use following code.
```bash
docker run -p 8000:8000 money_api
```
- To use the web application, open the browser of your choice and browse to 
```bash
http://[app_ip_address]:8000/apidocs
```
In my case address is 
```bash
http://192.168.99.100:8000/apidocs/
```
