#!/bin/bash               
                          
BENCH_DIR="/root/benchmarks"            
KERNEL_DIR="$BENCH_DIR/thesis-kernels"
cd $KERNEL_DIR            
pwd                       
ls                        
                          
./build/gemm 1048 1048 256 ./data/lognormal_mu4_0_s2_2_n17000000_seed853852.csv 5                     
m5 exit                     