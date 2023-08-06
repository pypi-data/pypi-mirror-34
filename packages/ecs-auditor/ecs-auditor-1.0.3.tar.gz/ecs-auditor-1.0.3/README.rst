ecs-auditor
===============

:code:`ecs-auditor` handles auditing ECS cluster and services. It also compares SSM param versions against for the same application in different regions.

Installation
--------------

Option 1: :code:`pip install ecs-auditor`
Option 2: See `setup.py Usage`_ above for how to use this within setup.py.

Usage from sphinx
-----------------
Run the following command, and pass in any of the :code:`cli parameters` from below:

:code:`ecs-auditor --config config.yml ...`

CLI Parameters
------------------------

The currently supported cli params are:

:--config:
    Specify location of the config file. Must be full location path (use :code:`pwd`)

:--region:
    AWS region to get data for. [default: all, options: [us-east-1, eu-central-1, eu-west-1, all] ]

:--env:
    AWS environment to get data for. :code:`preprod,prod,production, etc`

:--output:
    How to display the results. [default: pretty, options: [pretty, json, compare] ]

:--ignore-author:
    Only show the results that do not include this SMS Param author specified

:--services:
    Specify a list of service names in the cluster, separated with a comma. [default: None, options: string']

:--show-differences-only:
    Show only the results where there is a difference either the same application in different regions
