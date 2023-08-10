__DOC__=\
"""
python setup.py bdist_wheel
python -m twine upload --repository pypi dist/*
"""
import os
import sys
import pdb
import shutil
from setuptools import setup,find_packages

cleanup_only=sys.argv[1]=='cleanup'

#Move some stuff around.
thefile="pybrick.py"
work_dir=os.path.abspath(".")
target_dir=os.path.join(work_dir,'pybrick')
fq_orig=os.path.join(work_dir,thefile)

#Remove old artifacts.
print("Cleaning up old stuff...")
for sub in ['pybrick.egg-info','build','dist','pybrick','__pycache__']:
    shutil.rmtree(os.path.join(work_dir,sub),ignore_errors=True)

if cleanup_only:
    print("No build.")
    sys.exit(0)


import pybrick
version=pybrick.__version__
print("work_dir is",work_dir)
print("pybrick version is",version)

#Move the required files into position.  I'm pretty sure I've
#set the project up wrong or am using setup.py wrong... This
#can't be anything close to a good way of doing it.
srces=['__init__.py','pybrick.py','ptest.csv']
os.makedirs(target_dir,exist_ok=True)
for src in srces:
    shutil.copy(os.path.join(work_dir,src),
                os.path.join(target_dir,src))
                

setup(
    name = 'pybrick',
    version=version,
    long_description="""An interface for Yellowbrick data warehouse, written with the data analyst in mind.""",
    long_description_content_type='text/markdown',
    install_requires=[
          'pandas',
          'psycopg2',
          'sqlalchemy',
      ],
    packages=find_packages("."),
    include_package_data=True,
    package_data={'': ['*.csv']}
)
