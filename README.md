
# NabShop ~ Experience the power of words!
![logo](./public/images/nabshop-dark.png)

# Introduction

## The Project
**NabShop** is an ecommerce website that allows people to purchase books. A user without an account can browse the catalogue of books available in the store, see the prices, view details of each book including the description and so on. They can search for a particular book by typing in the search bar in the navigation menu. While still not having registered to the website, they can add books in their cart, see what's in their cart, and when they are ready to make a purchase, they will be prompted to open an account, fill in payment details and place the orther.
The user that has an account can view their account details, their past orders.

## The Context
A webstack portfolio project is a requirement for completing the advanced curicullum of the ALX SE program. Having an affinity with literature and having published a few books, I decided to use the skills learned in the ALX SE program to build an ecommerce website to sell those books. We were able to choose our project partners and project topic, as long as we present a working program at the end of the two weeks of development. 
<!-- ## Story behind ARC
Since COVID-19, it has proven necessary to not only have in person  healthcare assistance services but also virtual health care services. With a healthcare website that intends to bridge the gap between time and a user's needs, lives could be saved and better.
Oftentimes when people get sick (nothing too serious but still need to see a doctor), they encounter several challenges trying to get treated as soon as possible. The hospital could be far away from them in the city, there could be a long queue there… This is why we wanted to build **“ARC”** (African Rapid Care).
We aim to use technology to propose sustainable solutions to the problems we face daily in the different aspects of our  lives, the health domain being one of the most important ones. We ceased this opportunity to propose something that has the potential of saving people's lives. -->

## Author
My name is Nabil. I am passionate about providing sustainable solutions to problems around us in order to make life easier and more beautiful for all.

[**Nabil Affo**](https://www.linkedin.com/in/thenabverse/) ([**@TheNabVerse**](https://www.twitter.com/thenabverse/))- Author, Poet, Artist , Content Creator, Telecoms & Software Engineer.


<!-- ## Blog posts
I wrote a blog post about my NabShop journey.

* Nabil's article: [ARC: Reflections on building a healthcare web app](https://medium.com/@nabilwrites/arc-reflections-on-building-a-healthcare-web-app-55ce5d8543a9) -->



<!-- ## Take a tour of the deployed version at [https://african-rapid-care.tk](https://african-rapid-care.tk) -->

# Features
![technology](/public/images/user-stories.png)


Here are some features of the ecommerce website based on the user stories defined in the initial phase of the conception of the project.

### *1- browse the catalogue of books*
Even without an account, the user can browse the catalogue of books available in the store

![catalogue](/public/images/catalogue.png)

### *2- view book details*
A click on buttons provided for each book in the store will take the user to the book detail page that gives more information about the book

![book-detail](/public/images/book-detail.png)

### *3- search for a book*
The user can type in the search box in the navigation menu key words of a book and find it

![search](/public/images/search.png)

### *4- add to cart*
The website gives the possibility to select a quantity for a book and add it to the cart that keeps a count of the number of items in it

### *5- see items in the cart*
When a user fills a cart with books, they can have the summary of the content of their cart displayed upon clicking the cart icon in the navigation bar

![sign-up](/public/images/see-cart.png)

### *6- checkout*
When the user is ready to order (having registered to the website), they can go to the checkout page, fill in the relevent information and proceed to payment

![ckeckout](/public/images/checkout.png)
![success](/public/images/success.png)


### *7- sign-up*
The user must sign up before placing an order

![sign-up](/public/images/sign-up.png)

### *8- log-in*
Once the user has opened an account, they can sign in, see their account details, their previous orders

![login](/public/images/login.png)

### *9- admin*
The admin users can manage the website in the admin panel, add-edit-update-delete books, see customers etc. depending on their privileges


![admin](/public/images/book-page.png)



[Click here to watch the video presenting the app](https://www.youtube.com/watch?v=3j6Yfl5uGZ4)

<!-- ## Known bugs
*  -->

## Future for the App
There are other functionalities to add to the website, like a part responsible for handling the shipping and tracking orders, the ability to browse the store by genre and much more. This would make the website a complete and functional ecommerce application


# Architecture & Technology
![architecture](/public/images/architecture.png)
![technology](/public/images/technology-architecture.png)
The website is a fullstack project involving the backend and the frontend

## Frontend App:
- **Vue.js:** *Vue.js* frontend framework was used to build the frontend app that will be requesting data from the backend via a REST API and will display that to the user. The frontend is served in production by *nginx*

## Backend & REST API
- **Django:** The backend is in python using the *django* framework 
- **REST API:** The back implements a REST API with CRUD operations (GET, POST...) provisioning different endpoints based on the needs of the frontend and the privileges of the user.
The backend is served by *gunicorn*

![api-root](/public/images/api-root.png)
![book-list](/public/images/book-list.png)


## Database
- **MySQL Relationational Database** to store data
- Handle database with **Django ORM**
![database](/public/images/data-model.png)


## Docker
**Docker compose** is used to dockerize the application. The network of apps comprises:
- backend-app container
- frontend-app container
- mysql database container

## Server/Deployment
- The deployment in production used an instance at digitalocean.com
- The app is deploy at [nabshop](http://143.110.230.206)

# Installation
**Requirements:**
- Docker (https://www.docker.com/)
- Docker compose
- Stripe key token for test (set an environment variable `VUE_APP_STRIPE_TOKEN`)

**Installation in local setup:**
- Navigate to the repository root folder
- Execute docker compose command
```shell
  docker compose up --build
  ```

  **Test:**

  When all containers are launched and connected:
  - type `http://localhost:8080/` in the browser for the frontend app and try it out
  - type `http://localhost:8000/` in the browser for the backend app (`http://localhost:8000/store/`) you can try the API endpoints and see the response returned. You can try admin operations in the admin panel (`http://localhost:8000/admin/`) with username `admin`  and password `admin` (this admin user is created when building the images and running the containers with the command `python manage.py nabshopdb`in the `nabshop/nabshopdjango/docker-entrypoint.sh` that populates the database) 
  - to add images to the preloaded books provided in the folder [/public/images/books/](/public/images/books/), log in as admin and edit the books
  
  
  <!-- create an admin user, navigate to the books page in the admin panel and add an image to a book:
  ```shell
  # list the running containers and note the ID of the backend container
  docker ps

  # enter the container in interactive mode and use the shell
  docker exec -ti [containerID] sh

  # create a superuser
  python manage.py createsuperuser

  ``` -->


# Acknowledegments

* **ALX staff** - For this amazing year full with emotions, learnings, growth, developement, discovery...

* **Cohort 5 and all ALX students** - For your friendship, support throughout the year

* **YOU, the reader** - For taking the time to go through my project!


# License
**MIT License**
<!-- 
_Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:_

_The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software._

_THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE._
-->
