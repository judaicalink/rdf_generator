from setuptools import setup, find_packages

setup(
    name='rdf-generator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'rdflib',
        'pandas',
        'beautifulsoup4',
        'pymysql',
        'PyPDF2'
    ],
    entry_points={
        'console_scripts': [
            'rdfgen=rdf_generator.cli:main',
        ],
    },
    author="Benjamin Schnabel",
    author_email="b.schnabel@hs-mannheim.de",
    description="A library for generating RDF datasets from various data sources",
    long_description=open('README.md').read(),
    url="https://github.com/judaicalink/rdf-generator",
)
