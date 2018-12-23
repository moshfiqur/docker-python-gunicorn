# This is very important. If you set the binding 
# address to 127.0.0.1 like in non-container way,
# then it will only receive request from localhost
# which is the docker container itself. That means,
# gunicorn won't be reachable outside of the container.
bind = '0.0.0.0:10080'

workers = 2