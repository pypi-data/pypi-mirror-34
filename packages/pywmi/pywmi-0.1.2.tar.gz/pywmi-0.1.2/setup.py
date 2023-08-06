from setuptools import setup

setup(
    name='pywmi',
    version='0.1.2',
    description='Essential tools and interfaces for WMI',
    url='http://github.com/samuelkolb/pywmi',
    author='Samuel Kolb',
    author_email='samuel.kolb@me.com',
    license='MIT',
    packages=['pywmi'],
    zip_safe=False,
    install_requires=['pysmt', 'numpy']
)
