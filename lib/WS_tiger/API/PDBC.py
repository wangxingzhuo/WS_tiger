import ctypes

lib_handle = ctypes.CDLL('.libfun.so')

test = lib_handle.test
print test(5)