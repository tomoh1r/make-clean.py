# -*- coding: utf-8 -*-
from __future__ import absolute_import

import tempfile
import shutil

import pytest


@pytest.fixture(scope='module')
def make_clean():
    from make_clean import make_clean
    return make_clean


@pytest.fixture(scope='function')
def tmp_dir():
    '''manage create and delete temporary directory

    I need real directory, so I can't use tmpdir...
    (or directory basename)
    '''
    try:
        tmp_dir = tempfile.mkdtemp()
        yield tmp_dir
    finally:
        shutil.rmtree(tmp_dir)
