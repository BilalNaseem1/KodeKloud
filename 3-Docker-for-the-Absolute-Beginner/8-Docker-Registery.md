# Docker Registery
If containers are the rain, then docker registery would be the cloud. Images are stored in docker registery. It is the central repository of all docker images.

### Docker Image naming convention
Naming convention
```bash
library/nginx
```
- The library prefix is used when no specific account or repo is provided indicating an official docker hub image.
- If we were to create our own account or repo.

### From where are the images pulled from?
- If we dont specify the location from where the images are to be pulled, then It is assumed to be on docker's default registery docker hub.
- The DNS name for the registry is `docker.io`, It is where all the images are stored. Whenever we create a new image or update an existing image, it is pushed to the registry. And whenever we deploy an application, it is pulled from the registry.
- For in-house applicaions, we host an internal private registry. Many AWS cloud providers provide a private registry by default when we open an account.

## Private Registry
To run a container using an image from a private registry, we login to the private registry using the docker login command.

```bash
docker login private-registry.io

# Running app
docker run private-registry.io/apps/internal-app
```

## Deploying a private Registry
If we are running our application on premise and dont have a private registry, how do we deploy our own private registry within our organization? The docker registry is another application - and is available as a docker image. The name of the image is registry and it exposes the API on port 5000.

After we have the custom registry running at port 5000 on this docker host, how do we push our own image to it?


```bash
docker run -d -p 5000:5000 --name registry registry:2

docker image tag my-image localhost:5000/my-image
```

## Questions
Let practice deploying a registry server on our own.
Run a registry server with name equals to my-registry using registry:2 image with host port set to 5000, and restart policy set to always.

Note: Registry server is exposed on port 5000 in the image.

Here we are hosting our own registry using the open source Docker Registry.

```
docker run -d -p 5000:5000 --restart=always --name my-registry registry:2
```