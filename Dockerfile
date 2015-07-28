FROM python:2.7-onbuild

CMD ["router.py"]

RUN python setup.py install
