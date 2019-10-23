#!/bin/bash               
                          
BENCH_DIR="/root/benchmarks"            
KERNEL_DIR="$BENCH_DIR/thesis-kernels"
cd $KERNEL_DIR            
pwd                       
ls                        
                          
./build/gemm 1048 1048 1048 ./data/lognormal_mu5_0_s3_5_n17000000_seed1750.csv 10                     
m5 exit                     