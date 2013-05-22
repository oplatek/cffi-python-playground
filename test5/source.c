#include <string.h>
# include <stdio.h>

typedef char mychar;
typedef unsigned long mysize;

void save_to_DoubleBuffer(double ** buff, mysize * size, char * msg) {
    printf("save_to_DoubleBuffer %s\n", msg);
    *size = 30;
    *buff = (double*) malloc(sizeof(double) * *size);
    mysize i;
    double pi = 3.14;
    for (i = 0; i < *size; ++i) {
       /* *buff[i] = pi * i;  */
    }
}


void save_to_buffer(mychar ** buff, mysize * size, char * msg) {
    printf("save_to_buffer %s\n", msg);
    *buff = (char*) malloc(sizeof(char) * *size);
    char *tmp = "Ahoj ";
    *size = strlen(tmp) + strlen(msg);
    strcpy(*buff, tmp);
    strcat(*buff, msg);
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
