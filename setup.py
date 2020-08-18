from setuptools import setup, find_packages

setup(name='elderberry',
      version='0.0.3',
      description='A framework for parsing data into graph elements.',
      url='https://github.com/kaiserpreusse/elderberry',
      author='Martin Preusse',
      author_email='martin.preusse@gmail.com',
      license='MIT License',
      packages=find_packages(),
      install_requires=['graphio'],
      keywords=['data'],
      zip_safe=False,
      classifiers=[
          'Programming Language :: Python',
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
      ],
      )
