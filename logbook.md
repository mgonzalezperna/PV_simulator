##Logbook

### Bare minimum

* producer and consumer must wait that rabbitmq is stable.
* docker-compose v3 doesnt support depends_on: condition to wait for a healthcheck.
* dockerize could be the workaround to jump this issue.
* but wait-for-it bash script seems like a more suitable solution.

### Create a service to send and receive messages

* to give cohesion to the solution, i decided to wrap the interface with the brocker in a service class.
* all the rabbitmq config will be contained inside this module.
* so, in case that i dont want to use pika anymore, i can change it from there.
