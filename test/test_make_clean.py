import os


def test_remove_file(make_clean, tmp_dir):
    dir_name = os.path.basename(tmp_dir)
    os.chdir(os.path.dirname(tmp_dir))

    target_file = os.path.join(tmp_dir, 'example.txt')
    open(target_file, 'w').close()

    assert os.path.exists(target_file)
    make_clean(dir_name, [])
    assert not os.path.exists(target_file)


def test_remove_empty_dir(make_clean, tmp_dir):
    dir_name = os.path.basename(tmp_dir)
    os.chdir(os.path.dirname(tmp_dir))

    target_dir = os.path.join(tmp_dir, 'example')
    os.mkdir(target_dir)

    assert os.path.exists(target_dir)
    make_clean(dir_name, [])
    assert not os.path.exists(target_dir)


def test_not_remove_not_empty_dir(make_clean, tmp_dir):
    dir_name = os.path.basename(tmp_dir)
    os.chdir(os.path.dirname(tmp_dir))

    target_dir = os.path.join(tmp_dir, 'example')
    os.mkdir(target_dir)
    target_file = os.path.join(target_dir, 'example.txt')
    open(target_file, 'w').close()

    assert os.path.exists(target_dir)
    make_clean(dir_name, [os.path.join(dir_name, 'example', 'example.txt')])
    assert os.path.exists(target_dir)


def test_not_remove_exclude_file(make_clean, tmp_dir):
    dir_name = os.path.basename(tmp_dir)
    os.chdir(os.path.dirname(tmp_dir))

    target_dir = os.path.join(tmp_dir, 'example')
    os.mkdir(target_dir)
    target_file = os.path.join(target_dir, 'example.txt')
    open(target_file, 'w').close()

    assert os.path.exists(target_dir)
    make_clean(dir_name, [os.path.join(dir_name, 'example', 'example.txt')])
    assert os.path.exists(target_dir)


def test_not_remove_exclude_dir(make_clean, tmp_dir):
    dir_name = os.path.basename(tmp_dir)
    os.chdir(os.path.dirname(tmp_dir))

    target_dir = os.path.join(tmp_dir, 'example')
    os.mkdir(target_dir)

    assert os.path.exists(target_dir)
    make_clean(dir_name, [os.path.join(dir_name, 'example')])
    assert os.path.exists(target_dir)
