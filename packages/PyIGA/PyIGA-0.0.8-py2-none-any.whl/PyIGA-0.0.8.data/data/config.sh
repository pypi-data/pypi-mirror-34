reset

cmake ./ \
-DCMAKE_C_COMPILER=gcc \
-DCMAKE_CXX_COMPILER=g++ \
-DCMAKE_FORTRAN_COMPILER=gfortran \
-DCMAKE_CXX_FLAGS="${CMAKE_CXX_FLAGS} --std=c++11" \
-DCMAKE_BUILD_TYPE=Release \
-DISOGEOMETRIC_APPLICATION=ON \
-DPYTHON_INCLUDE_DIR="/usr/include/python2.7" \
-DPYTHON_LIBRARY="/usr/lib/x86_64-linux-gnu/libpython2.7.so" \
-DPYTHON_EXECUTABLE="/usr/bin/python2.7" \

make install

