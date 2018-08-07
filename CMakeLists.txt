CMAKE_MINIMUM_REQUIRED(VERSION 3.9.5)

PROJECT(libzippp)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

SET(PACKAGE "libzippp")
SET(VERSION "0.2")

find_package(libzip REQUIRED)
include_directories(${LIBZIP_INCLUDE_DIR})

add_definitions(-DLIBZIPPP_EXPORTS)
add_library(libzippp "src/libzippp.cpp")
target_link_libraries(libzippp
  ${ZLIB_LIBRARY}
  ${LIBZIP_LIBRARY}
)
