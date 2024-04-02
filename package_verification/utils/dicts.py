def check_if_dict_in_list(lst):
    for i in lst:
        if isinstance(i, dict):
            return i
    return None

def format_dependencies(dependencies: list):
    dependencies_dict = {}
    for dependency in dependencies:
        if "=" in dependency:
            name, version = dependency.split("=")[:2]
            dependencies_dict[name] = version
    return dependencies_dict

x = ['_libgcc_mutex=0.1=main', '_openmp_mutex=5.1=1_gnu', 'ca-certificates=2024.2.2=hbcca054_0', 'ld_impl_linux-64=2.38=h1181459_1', 'libffi=3.4.4=h6a678d5_0', 'libgcc-ng=11.2.0=h1234567_1', 'libgomp=11.2.0=h1234567_1', 'libstdcxx-ng=11.2.0=h1234567_1', 'loguru=0.5.3=py39h06a4308_4', 'ncurses=6.4=h6a678d5_0', 'openssl=3.0.3=h166bdaf_0', 'pip=23.3.1=py39h06a4308_0', 'python=3.9.7=hf930737_3_cpython', 'pyyaml=6.0.1=py39h5eee18b_0', 'readline=8.2=h5eee18b_0', 'setuptools=68.2.2=py39h06a4308_0', 'sqlite=3.41.2=h5eee18b_0', 'tk=8.6.12=h1ccaba5_0', 'tzdata=2024a=h04d1e81_0', 'wheel=0.41.2=py39h06a4308_0', 'xz=5.4.6=h5eee18b_0', 'yaml=0.2.5=h7b6447c_0', 'zlib=1.2.13=h5eee18b_0', {'pip': ['fire==0.6.0', 'six==1.16.0', 'termcolor==2.4.0']}]

print(format_dependencies(x))