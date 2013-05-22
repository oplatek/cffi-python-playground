#include <string.h>

int testInt(void) {
    return 3;
}

void testInt2(int * x) {
    *x = -6;
}


int testArray(int * x) {
    /* free(x); */
    int d = 8; 
    /* x = (int *) malloc(d * sizeof(int)); */
    x[3] = 33;
    /* } */
    return d;
}

/* char * fillString(int * x) { */
/*     char * tmp = "Ahoj jak se vede"; */
/*     *x = strlen(tmp); */
/*     return tmp; */
/* } */
