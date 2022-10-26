import os
import shutil

from setuptools import setup, glob
from setuptools.command.install import install as _install


class install(_install):
    """Custom clean command to tidy up the project root."""

    CLEAN_FILES = './build ./dist ./*.pyc ./*.tgz ./*.egg-info ./orm/*.egg-info'.split(' ')

    def run(self):
        _install.run(self)
        here = os.path.abspath(os.path.dirname(__file__))

        for path_spec in self.CLEAN_FILES:
            abs_paths = glob.glob(os.path.normpath(os.path.join(here, path_spec)))
            for path in [str(p) for p in abs_paths]:
                if not path.startswith(here):
                    raise ValueError("%s is not a path inside %s" % (path, here))
                print('removing %s' % os.path.relpath(path))
                shutil.rmtree(path)
        print("You are ready to go!\nDo some magic by writing 'pyt' in the terminal!")


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyt-wizard",
    version="1.0.0",
    package_dir={"": "orm"},
    description="The Official Masonite ORM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NawrasBukhari/py-Template",
    author="Nawras Bukhari",
    author_email="nawrasbukhari@hotmail.com",
    license="MIT",
    include_package_data=True,
    package_data={'': ['*.stub']},
    install_requires=[
        "inflection>=0.3,<0.6",
        "faker>=4.1.0,<14.0",
        "cleo>=0.8.0,<0.9",
        "colorama==0.4.6",
        "customtkinter==4.6.3",
        "Pillow==9.2.0",
        "cleo~=0.8.1",
        "argon2-cffi~=21.3.0",
        "password-validator==1.0",
        "setuptools==65.5.0",
        "flake8==3.7.9",
        "black==19.3b0",
        "pymysql",
        "isort",
        "psycopg2-binary",
        "python-dotenv==0.14.0",
        "pyodbc",
        "pendulum>=2.1,<2.2",
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
        "commands.stubs",
        "connections",
        "expressions",
        "factories",
        "helpers",
        "migrations",
        "models",
        "observers",
        "pagination",
        "providers",
        "query",
        "query.grammars",
        "query.processors",
        "relationships",
        "schema",
        "schema.platforms",
        "scopes",
        "seeds",
        "testing",
    ],

    entry_points={
        "console_scripts": [
            "pyt = commands.Entry:application.run",
        ],
    },
    cmdclass={'install': install}
)
