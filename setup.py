from setuptools import setup, find_packages

setup(
    name='Cat Pointer Game',
    version='1.0',
    author='Santos Gallegos',
    author_email='santos_g@outlook.com',
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
)
