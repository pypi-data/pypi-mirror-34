# -*- coding: utf-8 -*-

import os
import sys
import asyncio
import pytest

sys.path.append(
    os.path.abspath(os.path.join(os.getcwd(), "pymarketcap"))
)

tests_cache_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "cache")
if not os.path.exists(tests_cache_dir):
    os.mkdir(tests_cache_dir)

def pytest_addoption(parser):
    parser.addoption("--end2end", action="store_true",
                     default=False, help="Run slower tests.")

def pytest_collection_modifyitems(config, items):
    if not config.getoption("--end2end"):
        # Run end2end tests
        
        skip_end2end = pytest.mark.skip(reason="Need --end2end option to run")
        for item in items:
            if "end2end" in item.keywords:
                item.add_marker(skip_end2end)
    if sys.version_info < (3, 6,):
        skip_py36 = pytest.mark.skip(reason="Need Python v3.6 to run asynchronous tests.")
        for item in items:
            if "py36" in item.keywords:
                item.add_marker(skip_py36)

@pytest.yield_fixture()
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    #loop.close()
    pass


