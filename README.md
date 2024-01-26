<a name="readme-top"></a>



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
-->




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/FabienS2A/scrapy_app">
  </a>

<h3 align="center">Quote of the dayr</h3>

  <p align="center">
    A application to deliver quotes from various author.
    <br />
    <br />

  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#Trello link and Agile method">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This application is delayed to scrape data on the website "quotes.toscrape.com<br>
<br>
It's a Simplon school project on 5 days work. I made it carrefully.
Hope my product owners/teachers will be proud.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python-shield]][https://www.python.org]
* [![flask][flask-shield]][https://flask.palletsprojects.com/en/3.0.x/]
* [![mongodb][mongodb-shield]][https://www.mongodb.com]




<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these steps.
You'll need python to run this properly.

### Prerequisites

The app needs to install mongodb as a docker container. You can choose to use a docker container or from a local installation.
We used python 3.9 with a virtual environement.

### Installation


1. Clone the repo
   ```sh
   git clone https://github.com/FabienS2A/scrapy_app
   ```
2. Install required packages
   ```sh
   pip install -r requirements.txt
   ```

3. CD into your /scrapy_app/ directory, and prepare the python virtual environement.

On windows :
'''
python -m venv .venv 
'''
to activate :
'''
.venv/Scripts/activate
'''

On Linux or MacOS :
'''
python3 -m venv .venv 
'''
to activate :
'''
source .venv/bin/activate 
'''

4. To install dependencies, the packages required are specified in the requiments.txt file. Install it with :
'''
pip install -r requiments.txt
'''

5. You need a file to keep your environement variables. From the shell CD to the components folder :
'''
touch .env
'''
In .env, create some environement variable that you need.

app_pwd=<password>
mail=<email adress>

To set up a valid password for a gmail account, you may refer to this web page :
"https://support.google.com/accounts/answer/185833?hl=fr"

6. Now you can run the scraping from quotes to scrape website.
'''
flask --app api run
'''

7. Then try the search engine with the front end app named "application.py"
'''
streamlit -run application.py
'''

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Our front end application aims to try the search engine on the "9 mois à croquer data base".

Go to the URL provided by the shell terminal once you started the front end application, go to the [localhost](http://localhost:8501).

You can try to search in a selected table if you select one in the table list or on the full database if you don't.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- TRELLO LINK AND AGILE METHOD -->
## Trello link and Agile method

We did this job as Agile method experience. We first designed 'user stories' that you can overview at 'https://trello.com/b/lUrZxOwV/9mois-à-se-goinfrer'. Then, we discuss two times a day our progress on the project, requesting advices and help from the whole team on specific topic. We did our best to keep people in the team fully invested and to maintain a good organization.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Prototype
- [x] fetching data base
- [x] run api
- [X] link api to a basic front end
- [X] User experience
- [~] developing tests



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

We are up tu ear any suggestion, feel free to contribute !

Should the extrem necessity emerges, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".


1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
6. Leave Star on your way out !

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the Simplon students, we live in a free country ! 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Find us if you can.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Antony for the tortuous brief, and the helpful assistance !](https://github.com/DeVerMyst)
* [The whole group of Simplon Dev/IA group for discussion and exchange on the project]
* [The Simplon team, smiles and gentlyness !]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

