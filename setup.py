from setuptools import setup

test_deps = [
    'coverage',
    'pytest-cov',
    'pytest',
    'mock;python_version<"3.3"'
]

extras = {
    'testing': test_deps,
}

setup(
    name='mozreport',
    version='201809.dev0',
    description='CLI for generating experiment reports',
    author='Tim D. Smith',
    author_email='tdsmith@mozilla.com',
    url='https://github.com/tdsmith/mozreport',
    packages=["mozreport"],
    include_package_data=True,
    install_requires=[
        "attrs",
        "click",
        "requests",
    ],
    tests_require=test_deps,
    extras_require=extras,
    entry_points={
        "console_scripts": [
            "mozreport=mozreport.cli:cli",
        ]
    },
)
