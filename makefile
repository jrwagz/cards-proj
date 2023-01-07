create-venv:
	python3 -m venv .venv --prompt cards-proj
	. .venv/bin/activate && \
		pip3 install --upgrade pip wheel && \
		pip3 install -e .[test]

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name 'htmlcov' -exec rm -rf {} +
	find . -name '.coverage' -exec rm -f {} +
	find . -name 'coverage.xml' -exec rm -f {} +
	find . -name '.pytest_cache' -exec rm -rf {} +
	find . -name '.tox' -exec rm -rf {} +