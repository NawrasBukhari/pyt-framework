#!/usr/bin/env python
import os.path
from shutil import rmtree, copyfile
from setuptools import setup, glob
from setuptools.command.install import install as _install
from colorama import Fore, Style


class Install(_install):
    """Custom clean command to tidy up the project root."""

    CLEAN_FILES = './build ./dist ./*.pyc ./*.tgz ./*.egg-info ./orm/*.egg-info'.split(' ')
    ENV_FILENAME_OLD = ".env.example"
    ENV_FILENAME_NEW = ".env"
    ENV_FILE_LOCATION = os.path.abspath(os.path.dirname(__file__))
    CURRENT_LOCATION = os.path.abspath(os.path.dirname(__file__))
    CURRENT_PYTHON_VERSION = (3, 9)

    if os.sys.version_info < CURRENT_PYTHON_VERSION:
        print(Fore.RED + "Python version must be greater than 3.9" + Style.RESET_ALL)
        os.sys.exit(1)
    else:

        def run(self):
            _install.run(self)
            for path_spec in self.CLEAN_FILES:
                abs_paths = glob.glob(os.path.normpath(os.path.join(self.CURRENT_LOCATION, path_spec)))
                for path in [str(p) for p in abs_paths]:
                    if not path.startswith(self.CURRENT_LOCATION):
                        raise ValueError(
                            Fore.LIGHTRED_EX + "%s is not a path inside %s" % (path, self.CURRENT_LOCATION))
                    print(Fore.LIGHTGREEN_EX + 'removing %s' % os.path.relpath(path))
                    rmtree(path)

            env_file = os.path.join(self.ENV_FILE_LOCATION, self.ENV_FILENAME_OLD)
            env_file_new = os.path.join(self.ENV_FILE_LOCATION, self.ENV_FILENAME_NEW)
            copyfile(env_file, env_file_new)
            print(Fore.LIGHTGREEN_EX + f"Environment file [{self.ENV_FILENAME_OLD}] "
                                       f"file copied to [{self.ENV_FILENAME_NEW}] successfully!")
            os.system("pyt key:generate")
            print(Fore.LIGHTGREEN_EX + "Installation completed successfully!" + Style.RESET_ALL)
            print(Fore.LIGHTGREEN_EX + "You are ready to go! write [pyt] in the terminal!" + Style.RESET_ALL)


with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="pyt-wizard",
    version="1.0.0",
    python_requires=">=3.9",
    package_dir={"": "orm"},
    description="The Official Masonite ORM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NawrasBukhari/py-Template",
    author="Nawras Bukhari",
    author_email="nawrasbukhari@hotmail.com",
    license="MIT",
    include_package_data=True,
    package_data={"": ["*.stub", "*.html"]},
    install_requires=[
        "inflection>=0.3,<0.6",
        "faker==15.2.0",
        "cleo>=0.8.0,<0.9",
        "colorama==0.4.6",
        "customtkinter==4.6.3",
        "Pillow==9.3.0",
        "argon2-cffi~=21.3.0",
        "password-validator==1.0",
        "setuptools==65.5.1",
        "flake8==5.0.4",
        "black==22.10.0",
        "pymysql",
        "isort",
        "psycopg2-binary",
        "python-dotenv==0.21.0",
        "pyodbc",
        "pendulum>=2.1,<2.2",
        "fastapi==0.86.0",
        "uvicorn==0.19.0",
        "PyJWT~=2.6.0,>=2.6.0"
    ],

    classifiers=[
        "Development Status :: 5 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Environment :: Desktop Application Environment",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],

    keywords="PY-Template, Python, ORM",

    packages=[
        "collection",
        "commands",
        "connections",
        "expressions",
        "factories",
        "helpers",
        "migrations",
        "models",
        "observers",
        "pagination",
        "query",
        "query.grammars",
        "query.processors",
        "relationships",
        "schema",
        "schema.platforms",
        "scopes",
        "seeds",
    ],

    entry_points={
        "console_scripts": [
            "pyt = commands.Entry:application.run",
        ],
    },
    cmdclass={'install': Install}
)
