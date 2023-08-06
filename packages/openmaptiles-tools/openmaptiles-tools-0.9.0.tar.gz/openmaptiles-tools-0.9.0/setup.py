#from distutils.core import setup
import setuptools

setuptools.setup(
    name='openmaptiles-tools',
    version='0.9.0',
    packages=['openmaptiles'],
    license='MIT',
    scripts=[
        'bin/generate-doc',
        'bin/generate-diagram-pngs',
        'bin/generate-etlgraph',
        'bin/generate-imposm3',
        'bin/generate-mapping-graph',
        'bin/generate-metadata',
        'bin/generate-sql',
        'bin/generate-sqlquery',
        'bin/generate-tm2source',
    ],
    install_requires=[
        'docopt',
        'pyyaml',
        'graphviz',
    ],
)
