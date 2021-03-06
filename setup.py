from setuptools import setup, find_packages

setup(
    name='celautframework',
    version='__dev__',

    url='https://github.com/jossemii/GRPCBigBuffer_Client.git',
    author='Josemi Avellana',
    author_email='josemi.bnf@gmail.com',

    py_modules=['iobigdata', 'celaut_pb2'],
    install_requires=[
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
)