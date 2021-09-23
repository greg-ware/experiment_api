# Documentation for FastAPI experimentation
Built following https://fastapi.tiangolo.com/#example


## pipenv setup
* Install pipenv in your Python: 'pip install pipenv'
* Create a pipenv env using `pipenv install`
* Select new env in VSCode (use `pipenv --venv` to find proper env folder)

## install run-time packages in pipenv
We will want to have the `fastapi` and `uvicorn` packages:
* `pipenv install fastapi`
* `pipenv install uvicorn`

## install dev-time packages in pipenv
We will need to install ``pytest`, `requests`, `pylint` as development dependencies in the new env:
* `pipenv install --dev pytest`
* `pipenv install --dev requests`
* `pipenv install --dev pylint`

## run using uvicorn
* From the environment's shell, use `uvicorn main:app`
* Note that somehow this method does not allow debugging breakpoints in VSCode
* Test using e.g. `curl http://127.0.0.1:8000`, or `curl http://127.0.0.1:8000/items/5?q=somequery`
* Or use the `uvicorn` launch config (cf https://www.tutlinks.com/debug-fastapi-in-vs-code-ide/#define-configuration-in-launchjson-to-debug-fastapi-in-vs-code-ide)