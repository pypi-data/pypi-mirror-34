from setuptools import setup

def readme():
    with open('README.rst') as file:
        return file.read()

setup(name='bubbly',
      version='1.0.2',
      description='A module for plotting interactive and animated bubble charts using Plotly',
      long_description=readme(),
      url='https://github.com/AashitaK/bubbly',
      keywords=['Plotly', 'bubble charts', 'animated graphs', 'interactive graphs'],
      author='Aashita Kesarwani',
      author_email='kesar01@gmail.com',
      license='MIT',
      packages=['bubbly'],
      install_requires=[
          'plotly',
          'pandas',
      ],
      zip_safe=False)
