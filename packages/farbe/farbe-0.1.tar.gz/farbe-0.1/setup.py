from setuptools import setup

setup(
    name='farbe',
    version="0.1",
    description="farbe lets you use colorized outputs in Python.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Shinya Fujino',
    author_email='shf0811@gmail.com',
    license='MIT',
    url='https://github.com/morinokami/farbe',
    py_modules=['farbe'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
    ]
)
