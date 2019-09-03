#!/bin/bash               
                          
BENCH_DIR="/root/benchmarks"            
KERNEL_DIR="$BENCH_DIR/thesis-kernels"
cd $KERNEL_DIR            
pwd                       
ls                        
                          
./build/asum_cols 2048 2048 ./data/lognormal_mu5_0_s3_5_n100000000_seed152168.csv                     
m5 exit                     