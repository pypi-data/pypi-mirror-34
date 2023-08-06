import setuptools

setuptools.setup(
    name="qeGraphMaker",
    version="1.0.5",
    author="Kevin Postlethwait",
    author_email="kpostlet@redhat.com",
    description="Create PDF Graphs from Google Sheets Data",
    url="https://github.com/KPostOffice/QETool_pip",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
      "requests",
      "matplotlib",
    ],
    entry_points = {
        "console_scripts": [
            "fileMaker=qeGraphMaker.createFile:main",
            "graphGen=qeGraphMaker.xeqt:main"
        ]
    },
)
