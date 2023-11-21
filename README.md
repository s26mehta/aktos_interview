# aktos_interview

This project run a simple django application where the backend has a consumers endpoint under the geo_json_generator app.

Steps to run:
- python3 -m venv django_env
- source django_env/bin/activate
- pip install -r requirements.txt
- python manage.py runserver

Once you have the server running locally, navigate to the following url to perform a get request to the endpoint:
- http://127.0.0.1:8000/geo_json_generator/consumers

The url can be changed to provide params as such:
- http://127.0.0.1:8000/geo_json_generator/consumers/min_previous_jobs_count=1
- http://127.0.0.1:8000/geo_json_generator/consumers/min_previous_jobs_count=1&max_previous_jobs_count=3
- http://127.0.0.1:8000/geo_json_generator/consumers/min_previous_jobs_count=1&max_previous_jobs_count=3&status=collected
- http://127.0.0.1:8000/geo_json_generator/consumers/max_previous_jobs_count=3&status=collected
- http://127.0.0.1:8000/geo_json_generator/consumers/status=collected

Improvements:
- The endpoint currently adds the data from a csv file to the data store at each call to ensure data consistency. The ideal scenario would be to add a separate endpoint where you can supply the URL of a csv file or load from a specific file locally.
- Testing should be added for each scenario
- Pagination should be added on endpoint
