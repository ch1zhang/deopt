# Bugs found by Deopt

## Datalog engines building

Corresponding commit version of Datalog engines for each bug:

| #     | Datalog Engine | commit version |
| ----- | -------------- | --------------- |
| bug1  | Souffle        | `3cd802d`     |
| bug2  | Souffle        | `3cd802d`     |
| bug3  | Souffle        | `29c5921`     |
| bug4  | Souffle        | `29c5921`     |
| bug5  | Souffle        | `29c5921`     |
| bug6  | Souffle        | `29c5921`     |
| bug7  | Souffle        | `29c5921`     |
| bug8  | Souffle        | `3cd802d`     |
| bug9  | Souffle        | `29c5921`     |
| bug10 | μZ            | `cbc5b1f`     |
| bug11 | μZ            | `cbc5b1f`     |

The [Dockerfile](../../Dockerfile) in the root directory of deopt contains all source code of Souffle, Z3 (μZ), and DDlog. Build the docker image first.

For bugs of Souffle (bug1 - bug9), enter the root directory of Souffle (/tmp/souffle in docker) and check out to the corresponding commit version, compile Souffle with command shown in [here](https://souffle-lang.github.io/build), or follow the command shown in [Dockerfile](../../Dockerfile).

For bugs of μZ (bug10 and bug11), enter the root dictory of Z3 (/tmp/z3 in docker) and checkout to the corresponding commit version, compile z3 with command shown in [here](https://github.com/Z3Prover/z3#build-status), or follow the command shown in [Dockerfile](../../Dockerfile).

## Bug reproduce

For bug1-6, 9-11, in each directory of these bugs, there is a bug-inducing test case named `bug.dl`, and corresponding reference programs `prefn.dl` and optimized programs `poptn.dl`, `n` indicates the iteration of test case generation. You can directly execute these files with `souffle -D- file_name.dl` for Souffle bugs (`-D-` means to print the output to the command line.) or `z3 file_name.dl` for μZ bugs. All of these bugs don't need additional execution options.

For bug7 and bug8, there is only `bug.dl` in their directory, as these two bugs were triggered by different execution options. Bug7 only occurred in synthesizer mode, which need `-c` in execution options. The execution will produce different result when remove `-c` option. Bug8 needs `-t none --disable-transformers=ExpandEqrelsTransformer`, and can produce different result when remove `-t none`.
