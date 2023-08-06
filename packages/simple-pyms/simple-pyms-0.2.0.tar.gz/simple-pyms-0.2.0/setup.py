from setuptools import setup, Command
import codecs
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()

# Generated from the requirements file created by executing
# pipenv lock -r | sed 's/==/>=/g' | egrep -v simple
required = [
    "attrs>=18.1.0",
    "autobahn>=18.7.1",
    "automat>=0.7.0",
    "constantly>=15.1.0",
    "hyperlink>=18.0.0",
    "idna>=2.7",
    "incremental>=17.5.0",
    "psutil>=5.4.6",
    "pyhamcrest>=1.9.0",
    "pywin32>=223; sys_platform == 'win32'",
    "six>=1.11.0",
    "twisted>=18.7.0",
    "txaio>=18.7.1",
    "zope.interface>=4.5.0; python_version != '3.1.*'"
]


class GenerateRequirements(Command):
    """Generate requirements.txt from pipenv"""
    description = "Generate requirements.txt"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    @staticmethod
    def run():
        # https://github.com/pypa/pipenv/issues/1593
        import json
        from pipenv.utils import convert_deps_to_pip
        with open('Pipfile.lock') as f:
            deps = json.load(f)['default']
        # remove local project which wouldn't have a hash
        for k, v in list(deps.items()):
            if v.get('path') == '.':
                del (deps[k])
        path_to_requirements_file_with_hashes = convert_deps_to_pip(deps)
        with open('requirements.txt', 'w') as reqf, \
                open(path_to_requirements_file_with_hashes) as hashf:
            reqs = hashf.read()
            reqf.write(reqs)
        sys.exit()


setup(
    name='simple-pyms',
    version='0.2.0',
    description='Microservices Without Headaches',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jaime Wyant',
    author_email='programmer.py@gmail.com',
    packages=['simplepyms'],
    install_requires=[required],
    cmdclass={"makereq": GenerateRequirements},
)
