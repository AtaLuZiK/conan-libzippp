import os
import shutil

from conans import ConanFile, CMake, tools


class LibzipppConan(ConanFile):
    name = "libzippp"
    version = "2.1"
    libzip_version = "1.5.1"
    license = "https://github.com/ctabin/libzippp/blob/master/LICENCE"
    url = "https://github.com/AtaLuZiK/conan-libzippp"
    description = "C++ wrapper for libzip"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    requires = "libzip/%s@zimmerk/stable" % libzip_version
    exports_sources = "CMakeLists.txt"
    generators = "cmake"

    @property
    def zip_folder_name(self):
        return "libzippp-libzippp-v%s-%s" % (self.version, self.libzip_version)

    def source(self):
        zip_name = "libzippp-v%s-%s.tar.gz" % (self.version, self.libzip_version)
        tools.download("https://github.com/ctabin/libzippp/archive/" + zip_name, zip_name)
        tools.check_md5(zip_name, "f1ff080f075f89d7f00346b392393597")
        tools.unzip(zip_name)
        os.unlink(zip_name)

        shutil.copy("CMakeLists.txt", self.zip_folder_name)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.zip_folder_name)
        cmake.build()

    def package(self):
        self.copy("libzippp.h", dst="include", src=os.path.join(self.zip_folder_name, "src"))
        self.copy("**.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["libzippp"]

