install:
	python -m pip install --upgrade pip &&\
		python -m pip install -r requirements.txt

install-aws:
	python -m pip install --upgrade pip &&\
		python -m pip install -r requireemnts-aws.txt

lint:
	pylint --disable=R,C hash_func.py

format:
	black *.py

test:
	python -m pytest -vv --cov=hello test_hash.py