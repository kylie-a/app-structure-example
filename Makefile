createdb: venv
	./venv/bin/python ./create_db.py

freeze:
	./venv/bin/pip-chill > requirements.txt

venv:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

run:
	./run.py

shell:
	./venv/bin/flask shell

routes:
	./venv/bin/flask routes
