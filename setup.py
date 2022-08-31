from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='Datargsing',
    packages=find_packages(include=['datargsing']),
    version='0.2.7',
    description='A Data management and manipulation library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='LTHC The Master (CHOSSY Lucas)',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.1.2'],
    url='https://github.com/LTHCTheMaster/Datargsing',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.10.0',
    test_suite='tests',
)
