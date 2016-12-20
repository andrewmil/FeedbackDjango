Steps to run feedback form locally:

1. Create virtual enviroment:
	python3 -m venv <virtual env name>
2. Clone the git repository:
	git clone https://github.com/andrewmil/FeedbackDjango.git
3. Activate virtual environment:
	source <virtual env name>/bin/activate
4. Install dependencies:
	cd FeedbackDjango 
	pip install -r requirements.txt
5. Run the web application:
	python3 manage.py runserver
6. Access the feedback form in your browser:
	go to localhost:8000/polls:
	

Setting up alternate database host ip: 

Navigate to “settings.py” file which is in the “mysite” folder in your git respository clone.
In ‘DATABASES’ change the ‘HOST’ attribute to the alternate host IP address. 
