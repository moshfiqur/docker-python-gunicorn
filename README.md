# A boilerplate docker container for python-gunicorn

A simple boilerplate to quickly start with python webapp and gunicorn wsgi server, in docker way.

## CAUTION:
In `gunicorn.config.py`, set the binding address as `0.0.0.0:PORT_YOU_WISH`. This is very important. If you set the binding address to `127.0.0.1` like in non-container way, then it will only receive request from localhost which is the docker container itself. That means, gunicorn won't be reachable outside of the container.

For example, I used this following binding address:

```python
bind = '0.0.0.0:10080'
```
