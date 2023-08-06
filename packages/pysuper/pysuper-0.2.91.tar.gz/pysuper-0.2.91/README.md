[![Donate](https://liberapay.com/assets/widgets/donate.svg)](https://liberapay.com/JamesCollier/donate) to me on Liberapay.

**Master:** [![build status](https://gitlab.com/structural-fragment-search/super/badges/master/build.svg)](https://gitlab.com/structural-fragment-search/super/commits/master)
[![coverage report](https://gitlab.com/structural-fragment-search/super/badges/master/coverage.svg)](https://gitlab.com/structural-fragment-search/super/commits/master)

**Latest 0.2 release:** [![build status](https://gitlab.com/structural-fragment-search/super/badges/0.2_series/build.svg)](https://gitlab.com/structural-fragment-search/super/commits/0.2_series)
[![coverage report](https://gitlab.com/structural-fragment-search/super/badges/0.2_series/coverage.svg)](https://gitlab.com/structural-fragment-search/super/commits/0.2_series)

# Super -- Information for users and developers
*Super* is able to rapidly search of 3D structural databases. Given a query fragment, *Super* searches through a database of 3D structures for the query
within a tolerence threshold (measured by RMSD).

## Releases
* [Current stable version: 0.2](https://gitlab.com/structural-fragment-search/super/tags/v0.2)
* [Curret development version: 0.3]()

## Dependencies
There are a few dependencies required to build and run Super:
1. python2 (https://www.python.org/) script is used to pre-process PDB text datafiles into an efficient binary database format
2. prody (http://prody.csb.pitt.edu/) is used to parse PDB files
3. check (https://libcheck.github.io/check/) is used for unit testing and can be disabled by passing --disable-check to the configure script.
4. lcov is used for code coverage. It is not necessary by default, but passing --enable-code-coverage to the configure script will search for the lcov program.

## Compile
```bash
./configure --prefix=${HOME}/some/install/path
```
I say ${HOME} so that I don't have to install as superuser. I often use --prefix=${HOME}/install

```bash
make && make install
```

## Running Super
in ${prefix}/bin directory:
$ LD_LIBRARY_PATH=../lib ./super [OPTIONS...] ${pdb_path}/pdb.db

```
Options listing from ./super --help:
Usage: super [OPTION...] DATABASE
super -- A 3D protein pattern search program.

  -c, --thread-count=COUNT   Concurrently process the database with COUNT
                             threads of control
  -d, --defaults             Keep default arguments.
  -g, --disable-gershgorin   Disable use of gershgorin circles for Jacobi
                             diagonalisation
  -l, --lowerbounds=BOUNDS   Comma separated list of lower bound checks to use
  -n, --disable-rmsd         Disable the full (Kearsley) RMSD calculation, just
                             use the LB
  -o, --output=OUTPUT        Output to OUTPUT instead of stdout
      --quiet                Produce no output
  -q, --query=QUERY          Query database
  -r, --disable-mmap         Disable use of memory mapped databases to speed up
                             calculations
  -t, --threshold=THRESHOLD  Pattern matching threshold measured in Angstrom
  -?, --help                 Give this help list
      --usage                Give a short usage message
  -V, --version              Print program version

Mandatory or optional arguments to long options are also mandatory or optional
for any corresponding short options.
```

I usually run with:
```bash
LD_LIBRARY_PATH=${HOME}/install/lib ./super --lowerbounds=arithmetic --threshold=1.0 --query=qry.db pdb.db
```

OR ON Mac OSX:
```bash
DYLD_LIBRARY_PATH=${HOME}/install/lib ./super -t 1.0 -q qry.db pdb.db
```

## Databases
An up-to-date pre-processed version of the entire PDB is available for download from http://lcb.infotech.monash.edu.au/super/pdb.db

To generate a query:
```bash
python pdb_pp.py --query [YOUR PDB FRAGMENT FILE].pdb --output myquery.qry
```

To generate a searchable database from a directory containing PDB files (pdb/):
```bash
python pdb_pp.py -o pdb.db pdb/
```