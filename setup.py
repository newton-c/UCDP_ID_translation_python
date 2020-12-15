from setuptools import find_packages, setup

setup(
    name='UCDP_ID_translation',
    packages=find_packages(include=['UCDP_ID_translation']),
    version='0.1.0',
    description='Package to translate between new and old UCDP IDs',
    author='Chris Newton',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    test_suite='tests',
)