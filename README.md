## PV Simulator

This is a simulated producer -> consumer model using a broker as link between both.
The Producer emulates the regular power consumption of a house.
The Consumer mocks a PV generator output and adds the Producer output consumption with the energy produced by the generator.
After that, it generates a .csv file with the date of the register, the power consumed, the pv output and the total calculated output.

### How to run it

Inside the directory

`PV_simulator/pv_simulator`

run

`docker-compose up`

The .csv output will be generated at

`PV_simulator/pv_simulator`

## Logbook

### Proto - Bare minimum.

* Producer and consumer must wait for rabbitmq to be stable.
* Docker-compose v3 doesn’t support depends_on: condition to wait for a health check.
* Dockerize could be the workaround to jump this issue, but wait-for-it bash script seems like a more suitable solution.

### Create a service to send and receive messages.

* To give cohesion to the solution, I decided to wrap the interface with the broker in a service class.
* All the rabbitmq config will be contained inside this module.
* So, in the case  don’t want to use pika anymore, I can change it from there.

### Poetry.

* Decided to use Poetry to handle the project and its dependencies and, later on, added scripts to run the entry points.

### Meter (alpha).

* Started to design the meter as daemon thread launcher.
* By doing this, I could launch other tasks as the measurements are sent.
* I thought this could be useful if this was running in a remote place, but for this case, it’s overkill.
* So, for a beta version, this will only be a simple for loop.

### Documentation.

* I reviewed the documentation several times, adjusting it from time to time to match the new design of the solution.
* That’s why several commits are focused on fixing and adding Docstrings.

### Messenger and Meter refactor.

* Almost the entire Messenger class was revisited. Sending kargs instead of globals to set up the service is a smarter solution.
* Also, Meter beta now sends measurements in a configurable loop, not using threads.

### PV generator (alpha).

* At first I thought that I could use historic data of solar irradiation to get physics parameters and mock the curve of a fixed PV panel.
* But after a few minutes of research, I decided that it wasn’t worth it right now.
* Finally, I decided to mock the PV generator as a function defined by segments.
* The curve seems like a positive linear function to some point around 8, then a parabola from 8 to 20 and then, a linear function with a negative slope.

### Rename the whole project.

* For some reason, I named the project as *emulator* instead of *simulator*
* Decided to refactor the project and fixed this.

### PV generator (beta).

* I reviewed the coefficients of the functions. Also, I decided to model the general functions from outside of the head-main-tail structure.
* Also, defined a callback function to process the json payloads.
* This function unwraps the values, structures it as a dictionary and then persists them into a .csv.
* The callback writes a new row for each measurement.
* The class that processes the measurements doesn’t maintain the values in memory, because no other method or module needs them.
* Also, later I’ll add noise to the measurements to emulate spikes in PV panel efficiency.

### Dockerfile and docker-compose.

* Because of Poetry, installing the project dependencies is so much easier.
* Also, using the scripts as entrypoints, I could use the same Dockerfile to build each service.
* Producer and consumer must wait for the rabbit-mq broker to be online and healthy to start sending and consuming and not failing.
* As I’m using docker-compose 3, I needed to use the recommended workaround and use a wait-for-it bash script.
* Curl-ing the script and later running it from command at the docker-compose solves the issue.

### Testing and refactors.

* At testing I realized that the class constructors were heavily coupled with the service messenger.
* This is a bad thing because only a few methods of those classes needed a broker, not all of them. So, the class could still 'do things' without the broker.
* The solution was to refactor the classes and add a 'set up broker' method outside of the constructors.
* After that, I could test the business logic rules and add the tests to the repo.

## What i would like to improve.

* I would love to add a graphic interface to check at realtim
