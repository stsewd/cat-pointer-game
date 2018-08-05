from setuptools import setup, find_packages

setup(
    name='pyxel-catpointer',
    version='0.1.0',
    author='Santos Gallegos',
    author_email='santos_g@outlook.com',
    license='MIT',
    url='https://github.com/stsewd/cat-pointer-game',
    packages=find_packages(),
    package_data={
        '': ['game/assets/'],
    },
    install_requires=['pyxel<1'],
    entry_points={
        'console_scripts': [
            'catpointer = catpointer.game:App',
        ],
    },
    python_requires='>=3.7',
    classifiers=[
        'Topic :: Games/Entertainment :: Arcade',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ]
)
