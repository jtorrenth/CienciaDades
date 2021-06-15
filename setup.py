from setuptools import setup
with open("README.txt", 'r') as f:
    long_description = f.read()

setup(
    name='pythonProject',
    url='https://github.com/jtorrenth/CienciaDades',
    version='1.0',
    long_description=long_description,
    packages=['Excercici1Package', 'Excercici2Package', 'Excercici3Package', 'Excercici4Package'],
    license='MIT License',
    author='datasci',
    author_email='jtorrenth@uoc.edu',
    description='Projecte Final Programació per a la Ciència de Dades'
)
