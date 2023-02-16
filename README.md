# Personal Portfolio Website
![](https://img.shields.io/badge/Django-v4.1.5-blue?logo=Django&logoColor=white)
![](https://img.shields.io/badge/Python->=v3.8-blue?logo=python&logoColor=white)
![](https://img.shields.io/badge/Database-SQLite-blue?logo=SQLite&logoColor=white)
![](https://img.shields.io/badge/Bootstrap-v5.3.0-blue?logo=Bootstrap&logoColor=white)
![](https://img.shields.io/badge/Media%20Files-AWS%20S3-blue?logo=Amazon%20AWS&logoColor=white)
![](https://img.shields.io/badge/Hosting-PythonAnywhere-blue?)
[![](https://img.shields.io/badge/License-MIT-blue?/)](https://www.gnu.org/licenses/MIT)

A portfolio website is a must-have for any person who wants to showcase their skills, experience, and projects to the world, especially software developers. This project is created with a simple and professional-looking design suited for a personal portfolio website, showcasing some of the projects that I have done, and some that are in progress.

## Access

The project is currently hosted on pythonanywhere.com and can be accessed with the following link:

http://msrezaie.pythonanywhere.com/


## Features

- A beautiful and responsive design
- A profile section to view my information, including name, short bio, location, and social media links
- A projects section to display my projects with images, descriptions, and links to demo and source code
- An about section to provide more information about me and and my skills


## Technologies
This project uses the following technologies:

- **HTML** for markup structure of the webpages
- **CSS** and **JavaScript** for styling
- **Bootstrap** used as the front-end framework in order to implement responsiveness
- **Django** as the web framework, used for managing the urls and connection with database models of the project
- **SQLite** is used for storing the and dynamically accessing the data used throughout the webpages
- **Python** is used as the programming language in order to connect the front-end templates to the back-end and provide functionality


## Implementation
This portfolio project is built using Django web framework and is hosted on PythonAnywhere. The media files, such as images and documents, are stored in an AWS S3 bucket. The database models are stored in SQLite.

### Packages Used
- **WhiteNoise**: is used to serve static files (CSS & JavaScript) in my Django project.
- **Pillow**: is implemented to provide support for working with images
- **django-widget-tweaks**: provides a set of template tags which I used to add custom attributes to my contact form.
- **django-storages**: is a package that provides support for working with various cloud-based storage solutions, including AWS S3.
- **boto3**: is used to provide support for working with AWS services from within my Python web application.

## Projects

### Textual Cryptography App (CryptoDen)
Named ‘Cryptoden’, a cryptography app that allows users to encrypt and decrypt text using various encryption algorithms. It uses a modular design that enables the addition of new ciphers with ease.

### Created Using:
- **Django**: The web app is currently integerated as an 'app' to my personal portfolio Django project.
- **Python**: The ciphers are implemented with Python.
- **JavaScript**: is used for managing inputs, compiling the input into JSON and sending to the backend for encryption.
- **Bootstrap**: is used as the front-end framework for structuring the design elements of the page.

### Screenshots:
Options section where users can choose their desired method of encryption/decryption and cipher

<img width="800" src="https://github.com/msrezaie/personal_portfolio/blob/main/cryptoden/screenshots/cryptoden1.jpg"/>


Based on the selected method and cipher, a brief description about the operation and selected cipher is presented to the user

<img width="800" src="https://github.com/msrezaie/personal_portfolio/blob/main/cryptoden/screenshots/cryptoden2.jpg"/>
