find_path(LIBZIPPP_INCLUDE_DIR NAMES libzippp.h PATHS ${CONAN_INCLUDE_DIRS_LIBZIPPP})
find_library(LIBZIPPP_LIBRARY NAMES libzippp PATHS ${CONAN_LIB_DIRS_LIBZIPPP})

find_package(libzip REQUIRED)

add_library(libzippp INTERFACE IMPORTED)
target_include_directories(libzippp
  INTERFACE ${LIBZIPPP_INCLUDE_DIR}
  INTERFACE ${LIBZIP_INCLUDE_DIR}
)
target_link_libraries(libzippp
  INTERFACE ${LIBZIPPP_LIBRARY}
  INTERFACE ${LIBZIP_LIBRARY}
)

mark_as_advanced(LIBZIPPP_INCLUDE_DIR LIBZIPPP_LIBRARY_DIR LIBZIPPP_LIBRARY)

message("** libzippp found by Conan!")
set(LIBZIPPP_FOUND TRUE)
message("   - includes: ${LIBZIPPP_INCLUDE_DIR}")
message("   - libraries: ${LIBZIPPP_LIBRARY}")
