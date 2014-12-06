eviaas
======

environment variables injector as a service

About
-----

This service allows easily exposing external services to tsuru applications. It works simply by injecting some predefined environment variables in the application after binding.


Example
-------

Let's assume you have an external logging service running at `udp://my.log.service:9976` and you want to expose this value to applications without hardcoding it in them.

First you will have to create the eviaas service application and add it to tsuru:
```
$ git clone https://github.com/tsuru/eviaas.git

$ cd eviaas

$ tsuru app-create my-log-service-api python

$ tsuru env-set -a my-log-service-api EVI_ENVIRONS='{"MYLOG_PROTOCOL": "udp", "MYLOG_ADDRESS": "my.log.service:9976"}'

$ git push git@192.168.50.4:my-log-service-api.git master

$ cat >service_descriptor.yaml <<EOF
> id: my-log-service
> password: 1234
> endpoint:
>   production: http://my-log-service-api.192.168.50.4.nip.io
> EOF

$ crane create service_descriptor.yaml
```

Now your tsuru has a new service called `my-log-service` 
and you can create instances:

```
$ tsuru service-add my-log-service my-log-instance

$ tsuru service-list
+----------------+-----------------+
| Services       | Instances       |
+----------------+-----------------+
| my-log-service | my-log-instance |
+----------------+-----------------+
```

And bind apps to it:

```
$ tsuru service-bind my-log-instance -a my-app
Instance "my-log-instance" is now bound to the app "my-app".

The following environment variables are now available for use in your app:

- MYLOG_PROTOCOL
- MYLOG_ADDRESS

```

For info about what happens when you bind a service to an application,
see http://docs.tsuru.io/en/latest/services/api.html#binding-an-app-to-a-service-instance
