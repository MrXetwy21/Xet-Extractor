from setuptools import setup, find_packages
import os

if __name__ == '__main__':

    setup(
        name='Xet-Extractor',
        description='Capturador de strings que permite extraer textos que esten en medio de dos delimitadores',
        license='MIT',
        url='https://github.com/MrXetwy21/Xet-Extractor',
        version='0.1',
        author='MrXetwy21',
        author_email='Xetwy21@outlook.com',
        packages=find_packages(),
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        install_requires=[
        ],
    )


