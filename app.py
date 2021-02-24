#!/usr/bin/env python3

from aws_cdk import core

from mldiscovery_app.mldiscovery_app_stack import MldiscoveryAppStack


app = core.App()
MldiscoveryAppStack(app, "mldiscovery-app", env={'region': 'sa-east-1'})

app.synth()
