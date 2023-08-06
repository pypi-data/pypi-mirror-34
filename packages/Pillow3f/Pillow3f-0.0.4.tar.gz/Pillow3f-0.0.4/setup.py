from setuptools import setup
with open('README.md') as yeet:
    long_description = yeet.read()
    
setup(
   name='Pillow3f',
   version='0.0.4',
   description='3D graphics library using Pillow',
   author='Robert Bassett',
   author_email='bassett.w.robert@gmail.com',
   packages=['Pillow3f'],
   install_requires=['pillow', 'numpy'],
   classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
   long_description = long_description
)
