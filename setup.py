from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding = "utf-8") as f:
	long_description = f.read()

setup(
	name = "tinfoildb",
	version = "1.0.0",
	description = "Fast, secure database interface intended for use as a password manager",
	long_description = long_description,
	url = "https://github.com/samrankin1/tinfoildb",
	author = "Sam Rankin",
	author_email = "sam.rankin@me.com",
	license = "GPLv3",
	classifiers = [
		"Development Status :: 4 - Beta",
		"Intended Audience :: End Users/Desktop",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Natural Language :: English",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3",
		"Topic :: Database",
		"Topic :: Utilities",
	],
	keywords = "encryption passwordmanager aes scrypt clipboard",
	packages = ["tinfoil"],
	install_requires = ["scrypt", "cryptography", "pyperclip"],
	entry_points = {
		"console_scripts": [
			"tinfoil = tinfoil.tinfoilcli:main",
			"tinfoil-spd = tinfoil.speedtest:main",
		]
    }
)
