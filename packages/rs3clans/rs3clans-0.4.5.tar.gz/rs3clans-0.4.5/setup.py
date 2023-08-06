import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rs3clans",
    description='A Python 3 module wrapper for RuneScape 3 Clan\'s API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.4.5',
    author='John Victor',
    author_email='johnvictorfs@gmail.com',
    license='MIT',
    packages=setuptools.find_packages(),
    zip_safe=False,
    url='https://github.com/johnvictorfs/rs3clans.py',
    classifiers = (
        "Programming Language :: Python :: 3"
    )
)
