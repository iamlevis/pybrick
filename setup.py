__DOC__=
"""
python setup.py bdist_wheel
python -m twine upload --repository pypi dist/*
"""
import os
import pdb
import shutil
from setuptools import setup,find_packages

def getVersion(path):
    """ This is embarrassing. """
    with open(path,"r") as h:
        while line:=h.readline():
            if line.startswith("__version__"):
                v=line.split("=")[1]
                v=v.strip("\n\'\"")
                return v
    raise ValueError("Never found a version.")

#Move some stuff around.
thefile="pybrick.py"
work_dir=r"."
build_dir=r"."
fq_orig=os.path.join(work_dir,thefile)
fq_target=os.path.join(build_dir,"pybrick",thefile)
version=getVersion(fq_orig)

#Remove old artifacts.
try:
    os.remove(os.path.join(work_dir,f"dist\\pybrick-{version}-py3-none-any.whl"))
except:
    pass

try:
    os.remove(fq_target)
except:
    pass

shutil.copy(fq_orig,fq_target)


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
