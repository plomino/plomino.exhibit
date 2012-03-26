from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='plomino.exhibit',
      version=version,
      description="Exhibit/Plomino integration",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='Plomino,exhibit,eea.daviz',
      author='Eric BREHAULT',
      author_email='eric.brehault@makina-corpus.org',
      url='https://github.com/plomino/plomino.exhibit',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plomino'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFPlomino',
          'eea.daviz',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
