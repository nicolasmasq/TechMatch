from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='techmatch',
      description="techmatch Model (train_at_scale)",
      install_requires=requirements,
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False)
