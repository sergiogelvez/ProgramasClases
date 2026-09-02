#include <iostream>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int u = 3;
    int v;
    int *pu, *pv;

    pu = &u;
    v = *pu;
    pv = &v;

    printf("\nu = %d    &u = %X     pu = %X     &pu = %d", u, &u, pu, *pu);
    printf("\nv = %d    &v = %X     pv = %X     &pv = %d", v, &v, pv, *pv);
}