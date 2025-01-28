from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='rdf-generator',
    version='0.1.4',
    entry_points={
        'console_scripts': [
            'rdfgen=rdf_generator.cli:main',
        ],
    },
    author="Benjamin Schnabel",
    author_email="b.schnabel@hs-mannheim.de",
    description="A library for generating RDF datasets from various data sources",
    long_description=long_description,  # Load the README as the long description
    long_description_content_type="text/markdown",  # Specify Markdown format
    url="https://github.com/judaicalink/rdf_generator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "rdflib",
        "pandas",
        "requests",
        "beautifulsoup4",
        "PyPDF2",
        "mysql-connector-python",
        "psycopg2",
    ],
)
