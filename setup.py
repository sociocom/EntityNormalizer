from setuptools import find_packages, setup
setup(
    name='EntityNormalizer',
    packages=find_packages(),
    version='0.2.0',
    description='Library for normalizing entities based on a dictionary',
    author='Gabriel Herman Bernardim Andrade',
    license='MIT',
    readme='README.md',
    url='https://github.com/sociocom/EntityNormalizer',
    download_url='https://github.com/sociocom/EntityNormalizer/archive/refs/tags/0.2.0.tar.gz',
    include_package_data=True,
    py_modules=['EntityNormalizer'],
    install_requires=['pandas', 'rapidfuzz', 'mojimoji'],
)