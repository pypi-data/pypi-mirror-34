import os

from setuptools import setup


def __path(filename):
    return os.path.join(os.path.dirname(__file__), filename)

build = str(int(os.environ['PIP_BUILD']) + 300)
keywords = os.environ['PIP_KEYWORDS']

version = '0.{}'.format(build)

with open('missinglink_kernel/inplace_version.py', 'w') as f:
    f.write("# coding=utf-8\n\n__inplace_version__ = '%s'\n" % version)

with open('requirements.txt') as f:
    install_requires = f.readlines()

install_requires = [package_name.strip() for package_name in install_requires if len(package_name.strip()) > 0]

setup(
    name='missinglink-kernel',
    version=version,
    description='Kernel SDK for streaming realtime metrics to https://missinglink.ai',
    author='MissingLink.ai',
    author_email='support+sdk@missinglink.ai',
    platforms=['any'],
    license='mit',
    packages=[
        'missinglink_kernel',
        'missinglink_kernel.callback',
        'missinglink_kernel.data_management',
        'missinglink_kernel.data_management.legit',
        'missinglink_kernel.data_management.legit.data_volume',
        'missinglink_kernel.data_management.legit.db',
        'missinglink_kernel.data_management.legit.db_index',
        'missinglink_kernel.data_management.legit.dulwich',
        'missinglink_kernel.data_management.legit.metadata_db',
        'missinglink_kernel.data_management.legit.object_store',
        'missinglink_kernel.data_management.legit.object_store.gcs',
        'missinglink_kernel.data_management.legit.ref_container',
        'missinglink_kernel.data_management.legit.scam',
        'missinglink_kernel.data_management.legit.scam.luqum',
        'missinglink_kernel.data_management.legit.utils',
        'missinglink_kernel.callback.dispatchers',
        'missinglink_kernel.callback.utilities',
        'missinglink_kernel.callback.vis'
    ],
    keywords=keywords,
    install_requires=install_requires,
    data_files=[('', ['pip_build.info'])]
)
