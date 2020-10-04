from setuptools import setup, find_packages

def read(filename):
    return [
        req.split() 
        for req 
        in open(filename).readlines()
        ]

setup(
    name="siscomsoc",
    version="0.1.0", #[major(0), minor(1), patch(0)] https://semver.org/
    description="qqr",
    package=find_packages(),
    include_package_data=True,
    install_requires=[read("requirements.txt")],
    extras_requires={
        "dev": read("requirements-dev.txt")
    }
)

#pip install -e .