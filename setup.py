from setuptools import setup, find_packages

setup(
    name='datalib',
    version='1.0.0',
    description='A Python library for data manipulation and analysis',
    author='Kais Hajri',
    author_email='kais.hajri01@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas', 'numpy', 'matplotlib', 'scikit-learn', 'seaborn'
    ],
    python_requires='>=3.7',
)
