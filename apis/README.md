# API Fundamentals

## What are APIs? How are they used and why are they so popular?

* Application Programming Interface
* Provides a service that can...
   * gives access to data, images, video, webpages
   * allow you to take a certain action
* API is build to represent certain resources

From API provider perspective:
* Provide a service which is easy to implement, maintain, extend and scale

Why might DevOps/Support Engineers need to use APIs?
* Automate interactions with cloud services, esp for config/admin
* Simulate user actions pr workflows to try and reproduce + test issues
* access data to help troubleshooting/diagnosis
* Retrieve and manipulate data from external systems and services

## Create a diagram to showcase the data transfer process in API communication.

* Often uses JSON:


## What is a REST API? What makes an API RESTful? What are the REST guidelines?

* REST 
   * Representational State Transfer
   * Type of architecture used for the api
   * primarily used to web services that are lightweight, maintainable, scalable
   * also called a restful service
   * uses HTTP as its protocol
* If RESTful must have these properties:
  * Representation and data flow
  * Messages
  * URL / Naming resources
  * Stateless
  * Caching


## What is HTTP? (what does it stand for and what is it used for? What is HTTPS?)

* HTTP is the protocol of internet communication
* HTTPS is the secure/encrypted version
* Request / response system

## Explain HTTP request structure using the diagrams provided, or your own.

## Explain HTTP response structure using the diagram provided, or your own.

## What are the 5 HTTP verbs and what do they do?

GET → read
POST → create
PUT → update (replace)
PATCH → update (partial)
DELETE → delete

# URIs and naming resources

Example
http://oursservice/customer/1

OR

http://oursservice/customer?id=1


## What is statelessness? Show examples of “stateless” and stateful http requests.



## What is caching?

* storing results to speed up  similar/identical requests in the future
* can be stored on the client, server, or any other component between them (such as proxy server)
* 

