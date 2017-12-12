# Udacity Category Project

## Requirements 
- [Vagrant](https://www.vagrantup.com/)
- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Node.js](https://nodejs.org/en/download/)
- [Angular CLI](https://github.com/angular/angular-cli)

## Installation 
- install Node.js and Angular Cli
- install Vagrant and VirtualBox
- clone the Vagrantfile from the Udacity Repo
- clone this repo into the `vagrant/` folder
- run `vagrant up` to run the virtual machine, then `vagrant ssh` to login to the VM
- from the backend folder run `sudo pip install -r requirements`
- run the application with `python application.py` from within its folder
- from the frontend folder run `npm install` to install the node modules
- run `ng serve` to start the webserver for the Angular4 application
- go to `http://localhost:4200` to launch the application

## REST Endpoints
*GET* http://localhost:8000/categories - Returns all Categories

*POST* http://localhost:8000/categories - Adds a Category
{
  "name": "Name of Category"
}

*PUT* http://localhost:8000/category/{categoryName} - Edit a Category
{
  "name": "New name of Category"
}

*DELETE* http://localhost:8000/category/{categoryName} - Delete a Category


*GET* http://localhost:8000/category/{categoryName}/items- Returns all items for this category

*POST* http://localhost:8000/category/{categoryName}/items - Adds an item
{
    "name": "Name of Item,
    "description": "Description of Item"
}

*PUT* http://localhost:8000/category/{categoryName}/items - Edit a specific item
{
    "name": "Name of Item,
    "description": "Description of Item",
    "id": 9
}

*DELETE* http://localhost:8000/category/{categoryName}/items/{itemName} - Delete an Item



## Login


A Login is possible via the Google Login Button on the top right.


## Bugs ##

- there is no refresh after the initial Login, so the Logout Button does not sure immediately
- in my vagrant machine, some GET requests took forever. I am absolutely clueless, what might cause this. As soon as you restart the webserver it works just fine.
- the Shared Folder does not work on every `vagrant up`
