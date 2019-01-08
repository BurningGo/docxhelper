from setuptools import setup

setup(name='docxhelper',
      version='0.11',
      description='Some additional helper functions for using docx',
      url='http://github.com/storborg/funniest',
      author='burninggo ',
      author_email='kojae1978@gmail.com',
      license='MIT',
      packages=['docxhelper'],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",],
      install_requires=['python-docx',],
      zip_safe=False)

