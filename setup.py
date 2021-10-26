from pip.req import parse_requirements


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements("requirements.txt")

reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='tcg_secrets',
    version='1.0.0',   # needs to be updated before every version /tag release
    description='Internal Collinson ',
    author='Puneet Jain',
    author_email='puneet.jain@collinsongroup.com',
    license='http://www.apache.org/licenses/LICENSE-2.0',
    package_dir = 'core',

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