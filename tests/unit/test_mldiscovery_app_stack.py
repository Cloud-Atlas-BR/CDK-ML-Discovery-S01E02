import json
import pytest

from aws_cdk import core
from mldiscovery-app.mldiscovery_app_stack import MldiscoveryAppStack


def get_template():
    app = core.App()
    MldiscoveryAppStack(app, "mldiscovery-app")
    return json.dumps(app.synth().get_stack("mldiscovery-app").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
