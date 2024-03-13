from setuptools import setup, find_packages

setup(
    name='jeo',
    version='0.0.1',
    description='PYPI tutorial package creation written by jeo',
    author='hwanghj09',
    author_email='hwanghj09@naver.com',
    url='https://github.com/hwanghj09/jeo',
    install_requires=['tqdm', 'pandas', 'scikit-learn',],
    packages=find_packages(exclude=[]),
    keywords=['jeo', 'hwanghj09', 'python datasets', 'python tutorial', 'pypi'],
    python_requires='>=3.6',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
