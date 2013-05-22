#include <string.h>

typedef char mychar;
typedef unsigned long mysize;
void save_to_buffer(mychar ** buff, mysize * size, char * msg) {
    *size = 5;
    *buff = (char*) malloc(sizeof(char) * *size);
    strcpy(*buff, "Ahoj");
}

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
