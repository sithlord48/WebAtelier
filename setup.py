from setuptools import setup, find_packages

setup(
    name='atelier',
    version='0.1',
    description='Atelier website',
    url='https://github.com/lays147/webatelier',
    author='Lays Rodrigues',
    author_email='laysrodriguessilva@gmail.com',
    license='GPLV3',
    packages=find_packages(exclude=('tests')),
    include_package_data=True,
    install_requires=[
        'Flask==0.12.1',
        # 'gunicorn==19.6.0',
    ],
)
