#!/usr/bin/env python3

from aws_cdk import core

from pipelines_webinar.pipeline_stack import PipelineStack

app = core.App()
PipelineStack(app, 'PipelineStack')

app.synth()
