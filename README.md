# Stock System

This is a simple CRUD that simulates a inventory/stock management system. There are three classes of products at the moment, but you can improve it and create as many as you need.
You can save, edit, delete items. It's also possible to import and 
export a large amount of data at once, like spreadsheets or .csv files. 

It's a very powerful tool for clone and start learning Django.

## Getting Started

These instructions will get you a copy of the project up and running on 
your local machine for development and testing purposes or anything 
else you can imagine. See deployment for notes on how to deploy the 
project on a live system.

### Prerequisites

What things you need to install the software and how to install them:

* I recommend you use PyCharm.
* OS: Debian Buster 64x.
* Python, Anaconda or pip.

### Installing

A step by step series of examples that tell you how to get a development env running:

Clone this repository.
```
git clone https://github.com/NicacioSilva/StockSys.git
```
Go to the project directory.
```
cd StockSys
```
You can use conda or pip to to install virtualenv.
```
conda install -c anaconda virtualenv
``````
Create a virtualenv with Python 3.7
``````
conda create -n venv python=3.7 anaconda
``````
Activate virtualenv.
```
conda activate venv
```
Install the dependencies.
```
pip install -r requirements.txt
```
Run the server.
```
python manage.py runserver
```
Now some kind of link must jump from your prompt. Copy it, past in your browser and rave fun!

##
## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

