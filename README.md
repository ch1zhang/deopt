# DEOpt

Datalog Engines Optimization Tester.

# Installation

## Docker

Build the docker file and run in docker

```
cd deopt
docker build -t deopt ./
docker run --rm -it -v $PWD:/tmp deopt /bin/bash
```

# Usage

## Testing `Soufflé`

You can immediately start testing `Soufflé` by just typing the following command:

```
python3 deopt/__main__.py
```

The deopt docker file has installed the latest revision of `Soufflé`.

If you want to test a different version of `Soufflé`, please build and install that version
and paste the path to `Soufflé` executable in the `path_to_souffle_engine` field in file
`/path/to/deopt/params.json`.

## Testing CozoDB, DDlog and μZ

The deopt docker file has installed the latest revision of `CozoDB`,  `DDlog `and `z3`.

For `CozoDB`, you can execute the following command:

```
python3 deopt/__main__.py --engine=cozodb
```

For `DDlog`, you can execute the following command:

```
python3 deopt/__main__.py --engine=ddlog
```

For `μZ`, you can execute the following command:

```
python3 deopt/__main__.py --engine=z3
```

# File structure

```

.
├── Dockerfile
├── README.md
├── supplementary_material.pdf # More detailed information about bugs found by deopt and queryFuzz.
├── deopt
│   ├── __init__.py
│   ├── __main__.py
│   ├── datalog               # Basic class for Datalog engines, including the basic algorithm
│   ├── default_params.json   # Default parameters for deopt
│   ├── engines               # Rules generator for different engines
│   │   ├── __init__.py
│   │   ├── cozodb
│   │   ├── ddlog
│   │   ├── souffle
│   │   └── z3
│   ├── home.py
│   ├── parsers
│   ├── runner                # Files used to execute the Datalog program for engines
│   └── utils
└── evaluation
    ├── Q1                    # Contains reference and optimized programs for bugs found by deopt 
    ├── Q2                    # Contains reference and optimized programs for bugs found by queryFuzz
    └── Q3                    # Contains the configuration file and results for Q3 in evaluation
```



# Reproduce the sensitivity analysis
You can copy the `params.json` file from each experiment located in the `./evaluation/Q3/results` folder to the current directory. Then execute the command that corresponds to the Datalog engine you target at.

