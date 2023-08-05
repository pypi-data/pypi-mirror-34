==============
baguette-build
==============

Git hook that will build and deploy the docker.

Configuration
=============

Define the **/etc/farine.ini** or override the path using the environment variable **FARINE_INI**:

::

    [DEFAULT]
    amqp_uri=amqp://127.0.0.1:5672/amqp
    db_connector=postgres
    db_name=cuisson
    db_user=jambon
    db_password=beurre
    db_host=127.0.0.1

    [cuisson]
    git=/home/git/repositories/{0}.{1}.git
    tmp=/tmp/
    api_namespace=http://127.0.0.1/api/0.1/vpcs/
    api_token=<token>
    domain_name=projects.baguette.io
    registry_domain=https://<account>.dkr.ecr.<region>.amazonaws.com/
    aws_account_id=<account>
    aws_ecr_region=<region>
