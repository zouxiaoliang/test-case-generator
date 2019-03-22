from setuptools import setup, find_packages

setup(
    name='test-case-generator',
    version='1.0.0',
    packages=find_packages(),
    url='www.seele.link',
    license='free license',
    author='zouxiaoliang',
    author_email='295919168@qq.com',
    description='generator cppunit test case class',
    install_requires=[
        "jinja2>=2.10"
    ],
    entry_points={
        'console_scripts': [
            'cppunit-generator = cppunit.generator:_main',
        ]
    }
)
