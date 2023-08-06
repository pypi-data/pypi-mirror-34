# wavefront_dispatch

This package contains Wavefront python wrapper for Dispatch to send metrics directly to wavefront.

## Requirements
Python 2.7 or 3.6

## Install
Install from PyPi
```
pip install wavefront_dispatch
```
More package [details](https://pypi.org/project/wavefront-dispatch/) on PyPi.

## Required Secrets

* wavefront_sever_url = https://<INSTANCE>.wavefront.com
* wavefront_auth_token = Wavefront API token with Direct Data Ingestion permission

These secrets must be present in Dispatch functions' secrets of context.

## Usage

Decorate Dispatch handler function with @wavefront_dispatch.wrapper.

```Python
import wavefront_dispatch

@wavefront_dispatch.wrapper
def handle(ctx, payload):
    # codes

```
And add `wavefront_dispatch` package as runtime dependency druing Dispatch python image creation.

## Standard Metrics reported by Wavefront Dispatch wrapper

Following metrics will be reported by wrapper:
|Metric Name                             |Type           |Description                                       |
|----------------------------------------|---------------|--------------------------------------------------|
|dispatch.function.wf.invocations.count  |Delta Counter  |Count of Dispatch function invocations            |
|dispatch.function.wf.errors.count       |Delta Counter  |Count of Dispatch function executions with error  |
|dispatch.function.wf.duration.value     |Gauge          |Execution time of Dispatch function in ms.        |


## Custom Dispatch Function Metrics
Custom metrics powered by [pyformance plugin](https://github.com/wavefrontHQ/python-client/tree/master/wavefront_pyformance).

Please refer to following [example](https://github.com/dispatchframework/wavefront-dispatch-python/blob/master/example.py):

```Python
import wavefront_dispatch
import random

@wavefront_dispatch.wrapper
def handle(ctx, payload):

    # Customized metrics
    registry = wavefront_dispatch.get_registry()

    # Report Gauge
    gauge_val = registry.gauge("dispatch.function.wf.testgauge")
    gauge_val.set_value(200)

    # Report Counter
    counter = registry.counter("dispatch.function.wf.testcounter")
    counter.inc()

    ...
```