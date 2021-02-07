# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os
import platform
import shutil
import tempfile

import pytest
from pkg_resources import parse_version


def pytest_addoption(parser):
    parser.addoption("--lint-code", action="store_true", help="To run linter.")


def pytest_configure(config):
    config.addinivalue_line("markers", "linter: mark test lint code.")


def pytest_runtest_setup(item):
    envnames = [mark for mark in item.iter_markers(name="linter")]
    if envnames:
        if parse_version(platform.python_version()) < parse_version("3.6"):
            pytest.skip("lint code requires python3.6 or higher.")

        if not item.config.getoption("--lint-code"):
            pytest.skip("skip lint code.")


@pytest.fixture()
def root_path():
    _here = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(_here)


@pytest.fixture(scope="module")
def make_clean():
    from make_clean import make_clean

    return make_clean


@pytest.fixture(scope="function")
def tmp_dir(monkeypatch):
    """manage create and delete temporary directory

    I need real directory, so I can't use tmpdir...
    (or directory basename)
    """
    try:
        tmp_dir = tempfile.mkdtemp()
        yield tmp_dir
    finally:
        # tmp_dir を削除するためにカレントディレクトリを移動
        monkeypatch.chdir(os.path.dirname(tmp_dir))
        shutil.rmtree(tmp_dir)
