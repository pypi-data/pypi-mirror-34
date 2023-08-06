# Install script for directory: /home/max/Schreibtisch/PyIGA/applications/isogeometric_application/tests

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_knot_array_1d" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_knot_array_1d")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_knot_array_1d"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/libs" TYPE EXECUTABLE FILES "/home/max/Schreibtisch/PyIGA/applications/isogeometric_application/tests/test_knot_array_1d")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_knot_array_1d" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_knot_array_1d")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_knot_array_1d"
         OLD_RPATH "/opt/boost_1_64_0/lib:/usr/lib/x86_64-linux-gnu/libpython2.7.so:/home/max/Schreibtisch/PyIGA/applications/isogeometric_application:/home/max/Schreibtisch/PyIGA/kratos:/home/max/Schreibtisch/PyIGA/external_libraries/zlib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_knot_array_1d")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_knot_array_1d_test_2" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_knot_array_1d_test_2")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_knot_array_1d_test_2"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/libs" TYPE EXECUTABLE FILES "/home/max/Schreibtisch/PyIGA/applications/isogeometric_application/tests/test_knot_array_1d_test_2")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_knot_array_1d_test_2" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_knot_array_1d_test_2")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_knot_array_1d_test_2"
         OLD_RPATH "/opt/boost_1_64_0/lib:/usr/lib/x86_64-linux-gnu/libpython2.7.so:/home/max/Schreibtisch/PyIGA/applications/isogeometric_application:/home/max/Schreibtisch/PyIGA/kratos:/home/max/Schreibtisch/PyIGA/external_libraries/zlib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_knot_array_1d_test_2")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_tsplines_1" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_tsplines_1")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_tsplines_1"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/libs" TYPE EXECUTABLE FILES "/home/max/Schreibtisch/PyIGA/applications/isogeometric_application/tests/test_tsplines_1")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_tsplines_1" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_tsplines_1")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_tsplines_1"
         OLD_RPATH "/opt/boost_1_64_0/lib:/usr/lib/x86_64-linux-gnu/libpython2.7.so:/home/max/Schreibtisch/PyIGA/applications/isogeometric_application:/home/max/Schreibtisch/PyIGA/kratos:/home/max/Schreibtisch/PyIGA/external_libraries/zlib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_tsplines_1")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_1d" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_1d")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_1d"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/libs" TYPE EXECUTABLE FILES "/home/max/Schreibtisch/PyIGA/applications/isogeometric_application/tests/test_bezier_extraction_1d")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_1d" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_1d")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_1d"
         OLD_RPATH "/opt/boost_1_64_0/lib:/usr/lib/x86_64-linux-gnu/libpython2.7.so:/home/max/Schreibtisch/PyIGA/applications/isogeometric_application:/home/max/Schreibtisch/PyIGA/kratos:/home/max/Schreibtisch/PyIGA/external_libraries/zlib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_1d")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_1d_test_2" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_1d_test_2")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_1d_test_2"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/libs" TYPE EXECUTABLE FILES "/home/max/Schreibtisch/PyIGA/applications/isogeometric_application/tests/test_bezier_extraction_1d_test_2")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_1d_test_2" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_1d_test_2")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_1d_test_2"
         OLD_RPATH "/opt/boost_1_64_0/lib:/usr/lib/x86_64-linux-gnu/libpython2.7.so:/home/max/Schreibtisch/PyIGA/applications/isogeometric_application:/home/max/Schreibtisch/PyIGA/kratos:/home/max/Schreibtisch/PyIGA/external_libraries/zlib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_1d_test_2")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_2d" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_2d")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_2d"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/libs" TYPE EXECUTABLE FILES "/home/max/Schreibtisch/PyIGA/applications/isogeometric_application/tests/test_bezier_extraction_2d")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_2d" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_2d")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_2d"
         OLD_RPATH "/opt/boost_1_64_0/lib:/usr/lib/x86_64-linux-gnu/libpython2.7.so:/home/max/Schreibtisch/PyIGA/applications/isogeometric_application:/home/max/Schreibtisch/PyIGA/kratos:/home/max/Schreibtisch/PyIGA/external_libraries/zlib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_2d")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_2d_test_2" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_2d_test_2")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_2d_test_2"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/libs" TYPE EXECUTABLE FILES "/home/max/Schreibtisch/PyIGA/applications/isogeometric_application/tests/test_bezier_extraction_2d_test_2")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_2d_test_2" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_2d_test_2")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_2d_test_2"
         OLD_RPATH "/opt/boost_1_64_0/lib:/usr/lib/x86_64-linux-gnu/libpython2.7.so:/home/max/Schreibtisch/PyIGA/applications/isogeometric_application:/home/max/Schreibtisch/PyIGA/kratos:/home/max/Schreibtisch/PyIGA/external_libraries/zlib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_2d_test_2")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_3d" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_3d")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_3d"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/libs" TYPE EXECUTABLE FILES "/home/max/Schreibtisch/PyIGA/applications/isogeometric_application/tests/test_bezier_extraction_3d")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_3d" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_3d")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_3d"
         OLD_RPATH "/opt/boost_1_64_0/lib:/usr/lib/x86_64-linux-gnu/libpython2.7.so:/home/max/Schreibtisch/PyIGA/applications/isogeometric_application:/home/max/Schreibtisch/PyIGA/kratos:/home/max/Schreibtisch/PyIGA/external_libraries/zlib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_3d")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_local_1d" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_local_1d")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_local_1d"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/libs" TYPE EXECUTABLE FILES "/home/max/Schreibtisch/PyIGA/applications/isogeometric_application/tests/test_bezier_extraction_local_1d")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_local_1d" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_local_1d")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_local_1d"
         OLD_RPATH "/opt/boost_1_64_0/lib:/usr/lib/x86_64-linux-gnu/libpython2.7.so:/home/max/Schreibtisch/PyIGA/applications/isogeometric_application:/home/max/Schreibtisch/PyIGA/kratos:/home/max/Schreibtisch/PyIGA/external_libraries/zlib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_bezier_extraction_local_1d")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_findspan_local_knots" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_findspan_local_knots")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_findspan_local_knots"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/libs" TYPE EXECUTABLE FILES "/home/max/Schreibtisch/PyIGA/applications/isogeometric_application/tests/test_findspan_local_knots")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_findspan_local_knots" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_findspan_local_knots")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_findspan_local_knots"
         OLD_RPATH "/opt/boost_1_64_0/lib:/usr/lib/x86_64-linux-gnu/libpython2.7.so:/home/max/Schreibtisch/PyIGA/applications/isogeometric_application:/home/max/Schreibtisch/PyIGA/kratos:/home/max/Schreibtisch/PyIGA/external_libraries/zlib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_findspan_local_knots")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_CreateRectangularControlPointGrid" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_CreateRectangularControlPointGrid")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_CreateRectangularControlPointGrid"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/libs" TYPE EXECUTABLE FILES "/home/max/Schreibtisch/PyIGA/applications/isogeometric_application/tests/test_CreateRectangularControlPointGrid")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_CreateRectangularControlPointGrid" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_CreateRectangularControlPointGrid")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_CreateRectangularControlPointGrid"
         OLD_RPATH "/opt/boost_1_64_0/lib:/usr/lib/x86_64-linux-gnu/libpython2.7.so:/home/max/Schreibtisch/PyIGA/applications/isogeometric_application:/home/max/Schreibtisch/PyIGA/kratos:/home/max/Schreibtisch/PyIGA/external_libraries/zlib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/libs/test_CreateRectangularControlPointGrid")
    endif()
  endif()
endif()

