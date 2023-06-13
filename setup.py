from setuptools import find_packages, setup
setup(
    name='EntityNormalizer',
    packages=find_packages(),
    version='0.1.0',
    description='Library for normalizing entities based on a dictionary',
    author='Gabriel Herman Bernardim Andrade',
    license='MIT',
    py_modules=['EntityNormalizer'],
    install_requires=['pandas', 'rapidfuzz', 'mojimoji'],
)