#!/usr/bin/env python
"""
A performance benchmark using the official test suite.

This benchmarks jsonschema using every valid example in the
JSON-Schema-Test-Suite. It will take some time to complete.
"""
from perf import Runner

from jsonschema_extended.tests._suite import Suite


if __name__ == "__main__":
    Suite().benchmark(runner=Runner())
