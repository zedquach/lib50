from setuptools import setup

setup(
    author="CS50",
    author_email="sysadmins@cs50.harvard.edu",
    classifiers=[
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
        "Topic :: Utilities"
    ],
    cmdclass=cmdclass,
    message_extractors = {
        'push50': [('**.py', 'python', None),],
    },
    license="GPLv3",
    description="This is push50, CS50's internal library for using GitHub as data storage.",
    install_requires=["attrs", "pexpect", "pyyaml", "requests", "termcolor"],
    keywords=["push50"],
    name="push50",
    python_requires=">= 3.6",
    packages=["push50"],
    url="https://github.com/cs50/push50",
    version="1.0.0",
    package_data={'': ['locale/*/*/*.mo', 'locale/*/*/*.po']},
    include_package_data=True
)
