#!/bin/bash               
                          
BENCH_DIR="/root/benchmarks"            
KERNEL_DIR="$BENCH_DIR/thesis-kernels"
cd $KERNEL_DIR            
pwd                       
ls                        
                          
./build/gemv 512 4096 ./data/lognormal_mu4_0_s2_2_n17000000_seed50444.csv 200                     
m5 exit                     