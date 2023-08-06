# cython-manager
Console util for cython.

## Getting started

Create a project folder:
```sh
mkdir myAwesomeLib
```

Create two files (.c and .h) with these functions:
```sh
touch test.c
touch test.h
```

`test.c`
```c
#include "test.h"

int sum(int first_num, int second_num) {
        return first_num+second_num;
}

void hello(){
        printf("Hello world!");
}

int mul(int first_num, int second_num) {
        return first_num * second_num;
}
```

`test.h`
```c
#ifndef TEST_
#define TEST_

int C_sum(int first_num, int second_num);
int C_mul(int first_num, int second_num);
void C_hello();

#endif // TEST_
```

Then you need to build it via `cython-manager`:
```sh
cython-manager build test.c test.h myAwesomeLib
```

Now you need to build your Library for python:
```sh
python setup.py build_ext -i
```

So, you can use your C-functions in python:
```python
import myAwesomeLib

myAwesomeLib.hello()
print(myAwesomeLib.sum(1, 2))
print(myAwesomeLib.mul(2, 2))
```

Enjoy!
