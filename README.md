# conan-libzippp

Conan package for [libzippp](https://github.com/ctabin/libzippp)

The packages generated with this **conanfile** can be found on [here](https://bintray.com/zimmerk/conan).

## Package Status

| Bintray | Travis | Appveyor |
|---------|--------|----------|
|[ ![Download](https://api.bintray.com/packages/zimmerk/conan/libzippp%3Azimmerk/images/download.svg) ](https://bintray.com/zimmerk/conan/libzippp%3Azimmerk/_latestVersion)|[![Build Status](https://travis-ci.org/AtaLuZiK/conan-libzippp.svg?branch=release%2F2.1)](https://travis-ci.org/AtaLuZiK/conan-libzippp)|[![Build status](https://ci.appveyor.com/api/projects/status/8hxvvi6590l23s0i/branch/release/2.1?svg=true)](https://ci.appveyor.com/project/AtaLuZiK/conan-libzippp/branch/release/2.1)|

## Reuse the packages

### Basic setup

```
conan install libzippp/2.1@zimmerk/stable
```

### Project setup

```
[requires]
libzippp/2.1@zimmerk/stable

[options]
# Take a look for all avaliable options in conanfile.py

[generators]
cmake
```

Complete the installitation of requirements for your project running:

```
conan install .
```

Project setup installs the library (and all his dependencies) and generates the files conanbuildinfo.txt and conanbuildinfo.cmake with all the paths and variables that you need to link with your dependencies.

Follow the Conan getting started: http://docs.conan.io
