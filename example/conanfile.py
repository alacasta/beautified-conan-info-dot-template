from conans import ConanFile, CMake

class MyPkg(ConanFile):
    name = "mypkg"
    version = "1.2.3-rc1"
        
    def requirements(self):
        self.requires("openexr/2.4.0")
        self.requires("libjpeg/9d")
        self.requires("leptonica/1.78.0")
        self.requires("openssl/1.1.1f")
        self.requires("zlib/1.2.11")
        self.requires("libtiff/4.1.0")
        self.requires("cimg/2.8.3")
        self.requires("folly/2019.10.21.00")
        self.requires("zstd/1.4.3")
        self.requires("opencv/4.1.1@conan/stable")  # 'build' context (protoc.exe will be available)
        
    def build_requirements(self):
        self.build_requires("nasm/2.14")
        self.build_requires("gtest/1.8.1", force_host_context=True)  # 'host' context (our library will link with it
	