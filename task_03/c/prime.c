#include <stdbool.h>
#include <stdio.h>
int main() {
  int i, j, n;
  printf("enter a positive number: ");
  scanf("%d", &n);
  if (n < 0) {
    printf("not valid");
  } else {
    for (i = 2; i < n + 1; i++) {
      bool isprime = true;
      for (j = 2; j < i ; j++) {
        if (i % j == 0) {
          isprime = false;
          break;
        }
      }
      if (isprime == true) {
        printf("%d\n", i);
      }
    }
  }
}

