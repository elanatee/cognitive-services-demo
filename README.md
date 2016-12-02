## cognitive services demo

this project demonstrates how to use the [Microsoft Cognitive Services](https://www.microsoft.com/cognitive-services/) [Computer Vision API](https://www.microsoft.com/cognitive-services/en-us/computer-vision-api) in a simple Flask web app. 

### prerequisites 
- a text editor of your choice (sublime text, atom, xcode, etc.)
- [Python](https://www.python.org/downloads/)
- pip package installer (`sudo easy_install pip`)
- [Microsoft Azure](https://azure.microsoft.com) subscription 

### setup 
1. open terminal or command prompt
2. clone this repository (or download it to your desktop):
```bash
git clone https://github.com/elanatee/cognitive-services-demo.git
```
3. navigate to the directory: 
```bash
cd /path/to/cognitive-services-demo-master
```
4. set up a virtual environment
   1. [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) is used to create isolated Python environments - using virtualenv makes it so that the dependencies of your different projects are maintained in different places. install virtualenv on your machine:
```bash
pip install virtualenv
```
   2. in the project directory, create and activate the virtual environment for your project
```bash
virtualenv venv
 . venv/bin/activate
```
   use `deactivate` to exit the virtual environment
5. install the required Python packages for this [Flask](http://flask.pocoo.org/docs/0.11/) project:
```bash
pip install -r requirements.txt
``` 
6. tell your terminal which application to work with by setting the FLASK_APP environment variable:
   - on MacOS/Linux: `export FLASK_APP=app.py`
   - on Windows: `set FLASK_APP=app.py`
7. set up the project to work with your API key
   1. get your Computer Vision API subscription key [here](https://www.microsoft.com/cognitive-services/en-US/subscriptions)
   2. open the file `keys.py` in a text editor
   3. copy/paste your key into the single quotes 
   4. save the file
8. now you can open terminal or command prompt, run the basic flask app, and navigate to http://127.0.0.1:5000/ to see it live! it should look like this: 
```bash
$ flask run
\* Serving Flask app "app"
\* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### resources & further reading 
- [Computer Vision API Documentation](https://www.microsoft.com/cognitive-services/en-us/computer-vision-api/documentation)
...- [How to Call Computer Vision API](https://www.microsoft.com/cognitive-services/en-us/Computer-Vision-API/documentation/vision-api-how-to-topics/HowToCallVisionAPI) 
- [Computer Vision API Reference](https://dev.projectoxford.ai/docs/services/56f91f2d778daf23d8ec6739/operations/56f91f2e778daf14a499e1fa) 
- [A Beginners Guide to Cognitive Services](https://www.linkedin.com/pulse/idiots-guide-cognitive-services-nigel-willson) by Nige Willson
- [Getting to Know the Command Line](https://www.davidbaumgold.com/tutorials/command-line/) by David Baumgold

### thanks for reading!
feedback and pull requests are warmly welcomed and encouraged! feel free to tweet me [@elanatee](https://twitter.com/elanatee) or email me at etee (at) fordham (dot) edu if you have any questions!