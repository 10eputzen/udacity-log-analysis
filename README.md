# Udacity Log Analysis

## Requirements 
- [Vagrant](https://www.vagrantup.com/)
- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## Installation 
- install Vagrant and VirtualBox
- clone the Vagrantfile from the Udacity Repo
- clone this repo into the `vagrant/` folder
- get the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
- run `vagrant up` to run the virtual machine, then `vagrant ssh` to login to the VM

## Data Load 
- to load the data, cd into the vagrant directory and run `psql -d news -f newsdata.sql`
- running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data

## Run
- run the application with `python application.py` from within its folder to see the output of the queries
