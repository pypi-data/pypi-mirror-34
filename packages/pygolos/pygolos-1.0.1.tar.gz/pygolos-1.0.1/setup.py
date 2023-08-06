from setuptools import setup


setup(name="pygolos",
      packages=["pygolos"],
      version = "1.0.1",
      description="Golos classes library",
      author="kozakovi4 & fake364",
      author_email="kozakovi4@gmail.com",
      url="https://github.com/kozakovi4/pygolos",
      keywords=["golos", "blockchain", "classes"],
      classifiers=["Programming Language :: Python",
                   "Programming Language :: Python :: 3",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
                   "Operating System :: OS Independent",
                   "Topic :: Software Development :: Libraries :: Python Modules"], requires=['ecdsa'])
