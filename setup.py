

try:
    from setuptools import setup,find_packages
except ImportError:
    from distutils.core import setup,find_packages

try: # for pip >= 10
    from pip._internal.req import parse_requirements
    install_reqs = parse_requirements("requirements.txt",session = 'hack')
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements
    install_reqs = parse_requirements("requirements.txt")
# parse_requirements() returns generator of pip.req.InstallRequirement objects

with open("requirements.txt", "r") as f:
    install_requires = f.read().splitlines()

setup(
    name='tcgsecrets',
    version='1.0.1',   # needs to be updated before every version /tag release
    description='Internal Collinson ',
    author='Puneet Jain',
    author_email='puneet.jain@collinsongroup.com',
    license='http://www.apache.org/licenses/LICENSE-2.0',
    # package_dir = 'core',
    install_requires=install_requires,
    packages = find_packages(exclude=['test']),
    long_description=open('README.md').read(),
    classifiers =[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    url='https://github.com/iclp-ds/tcg_package',
)