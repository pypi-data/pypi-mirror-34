try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='helper_zlib',
    version='0.0.2',
    url='https://github.com/shuge/helper_zlib',
    license='MIT License',
    author='Shuge Lee',
    author_email='shuge.lee@gmail.com',
    description='Helper zlib',
    long_description="zlib gzdeflate, gzinflate, gzcompress and gzuncompress functions in pure Python.",
    packages = [
        "helper_zlib",
    ],
    #test_suite ="helper_zlib.tests",
)
