# Helm Functions
Template and values.yaml file create a valid manifest file i.e. deployment.yaml file.

![alt text](image-17.png)

If the repository name is not set in the values.yaml file, then the manifest file would be created without the image name. We can use Helm functions to set default values on which they can fall back onto in case the users dont provide anything in their values.yaml file.

- Functions in helm help transform data from one format to another.

![alt text](image-19.png)

Setting default value if user does not specify a value:

![alt text](image-20.png)

## Using pipes

![alt text](image-21.png)

![alt text](image-22.png)

![alt text](image-23.png)