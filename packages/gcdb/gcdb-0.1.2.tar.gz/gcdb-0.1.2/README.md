# Generate Compilation Database

GCDB is a tool to wrap your ordinary build system by overriding `CC` and `CXX`
to allow it to introspect the build process to be able to generate a JSON
Compilation Database which can be used with other tools like `clang-tidy`.

## Installation

```shell
$ pip install gcdb
```

## Usage

Run `gcdb` passing in the commands to build your code. You want to ensure the
entire sources are built so its important to clear any prior caches. For
example, if you use `make` to build your code:

```shell
$ gcdb 'make clean && make'
```

NOTE: Currently the passed command cannot run concurrently, so you cannot pass
`-j` to `make or similiar tools.
