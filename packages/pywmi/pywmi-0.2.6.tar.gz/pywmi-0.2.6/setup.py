from setuptools import setup

# Distribute: python setup.py sdist upload

setup(
    name='pywmi',
    version='0.2.6',
    description='Essential tools and interfaces for WMI',
    url='http://github.com/samuelkolb/pywmi',
    author='Samuel Kolb',
    author_email='samuel.kolb@me.com',
    license='MIT',
    packages=['pywmi'],
    zip_safe=False,
    install_requires=['pysmt', 'numpy', 'future'],
    setup_requires=['pytest-runner'],
    tests_require=["pytest"],
)
