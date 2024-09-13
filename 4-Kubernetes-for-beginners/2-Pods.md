## Pods
Kubernetes does not deploy containers directly on the worker nodes. The containers are encapsulated into a kubernetes object known as pods. A pod is a single instance of an application. A pod is the smallest object that you can create in kubernetes

Container instances are spinned up inside a new pod. Inside a single pod there is a single instance of the application running. Pods have a 1:1 relation with containers running the application. To scale up we create new pods and to scale down you delete pods. We donot add additional containers to existing pods to scale the application.