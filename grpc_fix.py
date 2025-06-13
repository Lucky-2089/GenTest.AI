# grpc_fix.py
import os
os.environ['GRPC_PYTHON_BUILD_SYSTEM_OPENSSL'] = '1'
os.environ['GRPC_PYTHON_BUILD_SYSTEM_ZLIB'] = '1'

# Additional gRPC configuration
os.environ['GRPC_PYTHON_DISABLE_LIBC_COMPATIBILITY'] = '1'