# legislators-bill-analises

## Requirements
This project uses Python 3.9.
The only non-standard library we are using is [pytest](https://docs.pytest.org/en/7.4.x/).

## How to run:
Create a virtual environment and install the requirements

```
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install requirements.txt
```

Then you are ready to run the reports generators:
```
$ python main.py
```

### Tests
The teste are in two file test_legislator_count.py and test_bill_count.py.
To run the tests execute
```
$ pytest <file_name>
```