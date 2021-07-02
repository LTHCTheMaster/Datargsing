from setuptools import find_packages, setup
setup(
    name='Datargsing',
    packages=find_packages(include=['datargsing'], exclude=['tests']),
    version='0.1.0',
    description='A Data management and manipulation library',
    author='LTHC (Lucas CHOSSY)',
    license='',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
