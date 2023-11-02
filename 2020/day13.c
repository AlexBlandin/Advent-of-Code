#include <stdint.h>
#include <stdio.h>

int main(int argc, char const *argv[]) {
  uint64_t n = 999999999999222;
  for (; n > 99999999999999; n -= 859)
    if ((n%19 == 0) && (n%41 == 32) && (n%859 == 840) && (n%23 == 19) && (n%13 == 7) && (n%17 == 15) && (n%29 == 10) && (n%373 == 323) && (n%37 == 24)) break;
  printf("%lu\n", n); // 905694340256752
  return 0; // in 1m44.871s
}
