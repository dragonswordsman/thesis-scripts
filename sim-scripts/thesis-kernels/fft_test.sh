#!/bin/bash               
                          
BENCH_DIR="/root/benchmarks"            
KERNEL_DIR="$BENCH_DIR/thesis-kernels"
cd $KERNEL_DIR            
pwd                       
ls                        
                          
./build/fft 4096 ./data/normal_mu0_0_s45_0_n17000000_seed25981.csv 1000
m5 exit                     