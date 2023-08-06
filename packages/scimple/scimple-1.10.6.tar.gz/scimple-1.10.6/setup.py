from setuptools import setup

setup(
    name='scimple',
    version='1.10.6',
    #py_modules=['scimple'],
    install_requires=['matplotlib', 'numpy', 'pandas', 'pyspark', 'pyarrow'],
    packages=['scimple/scimple_data', 'scimple'],
    package_data={'scimple/scimple_data': ['*']},
    url='http://github.com/EnzoBnl/Scimple',
    license='',  # MIT
    author='Enzo Bonnal',
    author_email='enzobonnal@gmail.com',
    description='Plot your data scimply in 1 line'
)
