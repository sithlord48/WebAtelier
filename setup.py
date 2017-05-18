from setuptools import setup

setup(
    name='Atelier',
    version='0.1',
    description='Atelier website',
    url='https://github.com/lays147/webatelier',
    author='Lays Rodrigues',
    author_email='laysrodriguessilva@gmail.com',
    license='GPLV3',
    packages=find_packages()
    install_requires=[
        'flask'
    ],
)
