#include "s.h"
#define SIMDE_ENABLE_OPENMP
#define SIMDE_ENABLE_NATIVE_ALIASES
#include "simde/simde/x86/sse4.2.h"

int main(int argc, char const *argv[]) {
  u64 n = 999999999999222;
  for (; n > 99999999999999; n -= 859)
    if ((n%19 == 0) && (n%41 == 32) && (n%859 == 840) && (n%23 == 19) && (n%13 == 7) && (n%17 == 15) && (n%29 == 10) && (n%373 == 323) && (n%37 == 24)) break;
  printf("%"LU"\n",n); // 905694340256752
  return 0; // in 1m44.871s
}
