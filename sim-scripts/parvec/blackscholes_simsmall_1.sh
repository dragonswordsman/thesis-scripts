#!/bin/bash

BENCH_DIR="/root/benchmarks"
PARSEC_DIR="$BENCH_DIR/parvec"
cd $PARSEC_DIR
pwd

source ./env.sh
parsecmgmt -a run -p parsec.simd.blackscholes -c gcc-hooks -i simsmall -n 1
m5 exit
