"""
Generate a webfaction helper fabfile in the current directory.
$ python -m wf_helpers.makefab

"""
import os
import shutil



FABFILE = 'fabfile.py'


def save_to_fabfile():
    package_fabfile = os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)
        ),
        FABFILE
    )
    shutil.copyfile(package_fabfile, FABFILE)


def generate():
    if os.path.exists(FABFILE):
        raise ValueError(f'{FABFILE} exists.')
    else:
        save_to_fabfile()


if __name__=='__main__':
    generate()
