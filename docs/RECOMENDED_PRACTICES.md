# Python Recommended Practices
## [Python Standard](https://github.com/Groupe-Atallah/development-standards/wiki/python):
- Use latest official Python version ([3.7.4](https://www.python.org/downloads/))
- Use PIP3 to manage the package.
- Follow [PEP8](https://pip.pypa.io/en/stable/) (When do reformat in JetBrains IDE like PyCharm, could be done automatically)
- Use Flask & Flask RESTFUL API or Falcon Framework to build API([comparison](https://medium.com/idealo-tech-blog/falcon-vs-flask-which-one-to-pick-to-create-a-scalable-deep-learning-rest-api-adef647ebdec), [more](https://stackshare.io/stackups/falcon-vs-flask))
- Use [unittest](https://docs.python.org/3.7/library/unittest.html) or [Pytest](https://docs.pytest.org/en/latest/) framework (comparison)
- Implement SonarQube and code coverage should be more than 95%
- Linting ([PEP8](https://www.python.org/dev/peps/pep-0008/), [pycodestyle](https://github.com/PyCQA/pycodestyle)) 
- [Typing](https://docs.python.org/3/library/typing.html): Typing is mandatory
- [Exception](https://docs.python.org/3.3/tutorial/errors.html): Never use catch-all except: statements
- [Docstrings](http://queirozf.com/entries/python-docstrings-reference-examples): Include Python Docstrings for every methods.
- [OpenAPI](https://readthedocs.ssense.com/standards/documentation/api/#openapi-tools): [OpenAPI Tools](https://openapi.tools/) (Recommendation:  [openapi-spec-validator](https://github.com/p1c2u/openapi-spec-validator))
