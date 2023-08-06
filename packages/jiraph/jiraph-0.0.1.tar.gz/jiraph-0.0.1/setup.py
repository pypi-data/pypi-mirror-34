import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
      name='jiraph',
      version='0.0.1',
      description='JIRA python helper',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/ramonfm/jiraph',
      author='Ramón Fernández',
      author_email='ramon@nospam.com',
      license='MIT',
      packages=['jiraph'],
      #packages=setuptools.find_packages(),
      classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
      ),
      zip_safe=False
)
