from setuptools import setup


SHORT_DESCRIPTION = 'Version bumper for Foliant projects.'

try:
    with open('README.md', encoding='utf8') as readme:
        LONG_DESCRIPTION = readme.read()

except FileNotFoundError:
    LONG_DESCRIPTION = SHORT_DESCRIPTION


setup(
    name='foliantcontrib.bump',
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    version='1.0.2',
    author='Konstantin Molchanov',
    author_email='moigagoo@live.com',
    url='https://github.com/foliant-docs/foliantcontrib.bump',
    packages=['foliant.cli'],
    license='MIT',
    platforms='any',
    install_requires=[
        'foliant>=1.0.4',
        'semver'
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Utilities",
    ]
)
