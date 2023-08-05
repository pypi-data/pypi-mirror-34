import setuptools


setuptools.setup(
    name='cloneholio',
    version='0.1.0',
    description='I am cloneholio! I need syncing of my repos.',
    license='MIT',
    author='Andrew Rabert',
    author_email='ar@nullsum.net',
    url='https://gitlab.com/nvllsvm/cloneholio',
    py_modules=['cloneholio'],
    entry_points={'console_scripts': ['cloneholio=cloneholio:main']},
    install_requires=[
        'consumers',
        'gitpython',
        'pygithub',
        'python-gitlab'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only'
    ]
)
