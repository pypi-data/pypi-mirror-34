from distutils.core import setup

setup(
    # Application name:
    name = "Indian_Speech_Lib",

    # Version number (initial):
    version = "1.0.0",

    # Application author details:
    author= "Mohd Wasih",
    author_email = "wasih.mohd@gmail.com",

    # Packages
    packages = ["Indian_Speech_Lib"],

    # Include additional files into the package
    include_package_data = True,

    # Details
    url="http://pypi.python.org/pypi/Indian_Speech_Lib_v010/",

    #
    # license="LICENSE.txt",
    description = "Useful speech recognition and transcription related library for Indian languages.",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
		"tensorflow",
		"pydub",
		"numpy",
		"sklearn",
		"keras",
		"soundfile",
		"pyAudioAnalysis",
		"statistics",
    ],
)
