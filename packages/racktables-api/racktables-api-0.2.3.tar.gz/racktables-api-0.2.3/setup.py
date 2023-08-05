from setuptools import setup
setup(
    name="racktables-api",
    version="0.2.3",
    packages=["rtapi"],
    license="GPLv2",
    description="Simple racktables API",
    url="https://github.com/rvojcik/rtapi",
    author="Robert Vojcik",
    author_email="robert@vojcik.net",
    keywords=['rtapi', 'racktables', 'racktables api', 'racktables-api','racktables cli','racktables-cli'],
    classifiers=[
            "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
            "Operating System :: POSIX",
            "Operating System :: Unix",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.7",
    ],
    install_requires = [ "ipaddr" ],
)

