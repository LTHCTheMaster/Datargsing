from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='Datargsing',
    packages=find_packages(include=['datargsing']),
    version='0.2.15',
    description='A Data management and manipulation library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='LTHC The Master (CHOSSY Lucas)',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner==6.0.0','setuptools>=68.0.0','wheel'],
    tests_require=['pytest==7.2.0'],
    url='https://github.com/LTHCTheMaster/Datargsing',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.11.1',
    test_suite='tests',
)
