__all__ = [
    'calc_py',
    'atoi',  # support for "from cypkgdemo import *; print(atoi.parse_charptr_to_py_int('4.33'))"
    # 'calc'
]

# support for "import cypkgdemo; print(cypkgdemo.atoi.parse_charptr_to_py_int('5.33'))";
# absolute import (required by python 3).
import cypkgdemo.atoi

# This will also support for "import cypkgdemo; print(cypkgdemo.atoi.parse_charptr_to_py_int('5.33'))"
# because calc cimported atoi
# import cypkgdemo.calc
