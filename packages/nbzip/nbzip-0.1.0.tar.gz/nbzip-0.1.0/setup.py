import setuptools

setuptools.setup(
    name="nbzip",
    version='0.1.0',
    url="https://github.com/data-8/nbzip",
    author="Data 8 @ UC Berkeley",
    author_email="peterkangveerman@berkeley.edu",
    description="Compresses and downloads all files in any of the user's directories.",
    packages=setuptools.find_packages(),
    install_requires=[
        'notebook', 'pytest'
    ],
    package_data={'nbzip': ['static/*']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Jupyter',
    ]
)

