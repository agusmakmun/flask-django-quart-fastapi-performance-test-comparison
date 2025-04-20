#!/bin/bash

# We're using Vegeta to perform the HTTP load testing tool and library.
# https://github.com/tsenart/vegeta

# brew update && brew install vegeta
# brew install rs/tap/jaggr
# brew install rs/tap/jplot

# chmod +x test-performance.sh
# ./test-performance.sh


echo 'GET http://127.0.0.1:8000/api/dummy' | \
    vegeta attack -rate=1000/s -duration 10m | vegeta encode | \
    jaggr @count=rps \
          hist\[100,200,300,400,500\]:code \
          p25,p50,p95:latency \
          sum:bytes_in \
          sum:bytes_out | \
    jplot rps+code.hist.100+code.hist.200+code.hist.300+code.hist.400+code.hist.500 \
          latency.p95+latency.p50+latency.p25 \
          bytes_in.sum+bytes_out.sum
