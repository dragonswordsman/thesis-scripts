#!/bin/bash               
                          
BENCH_DIR="/root/benchmarks"            
KERNEL_DIR="$BENCH_DIR/thesis-kernels"
cd $KERNEL_DIR            
pwd                       
ls                        
                          
./build/ger 1024 1024 ./data/lognormal_mu5_0_s3_5_n100000000_seed152168.csv                     
m5 exit                     