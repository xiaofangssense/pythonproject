https://medium.com/@shivama205/dependency-injection-python-cb2b5f336dce
## Dependency Injection
[Dependency injection](https://en.wikipedia.org/wiki/Dependency_injection) is a software design pattern that implements [Inversion of control](https://en.wikipedia.org/wiki/Inversion_of_control) to resolve dependencies. Formally, if object A depends on object B, object A must not create or import object B directly. Instead of this object A must provide a way to inject object B. The responsibilities of objects creation and dependency injection are delegated to external code - the dependency injector.

Popular terminology of the dependency injection pattern:

- Object A, which depends on object B, is often called - the client.

- Object B, which is depended on, is often called - the service.

- External code that is responsible for creation of objects and injection of dependencies is often called - the dependency injector.

There are several ways to inject a service into a client:

- by passing it as an __init__ argument (constructor / initializer injection)

- by setting it as an attribute's value (attribute injection)

- by passing it as a method's argument (method injection)

The dependency injection pattern has few strict rules that should be followed:

- The client delegates to the dependency injector the responsibility of injecting its dependencies - the service(s).

- The client doesn’t know how to create the service, it knows only the interface of the service. The service doesn’t know that it is used by the client.

- The dependency injector knows how to create the client and the service. It also knows that the client depends on the service, and knows how to inject the service into the client.

- The client and the service know nothing about the dependency injector.

Python has micro framework library for DI, called [Dependency Injector](https://github.com/ets-labs/python-dependency-injector)

https://pypi.org/project/dependency-injector/