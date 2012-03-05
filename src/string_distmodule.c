#include <Python.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX(a,b) ((a) > (b) ? a : b)
#define MIN(a,b) ((a) < (b) ? a : b)

int levenshteinDist(const char* a,const char* b){
    int m = strlen(a)+1;
    int n = strlen(b)+1;

    if( m==0 || n==0 ){
        return MAX(m,n);
    }

    int* d = malloc(m*n*sizeof(int));
    
    int i,j;
    
    for(i=0;i<m;i++){
        d[i*n] = i;
    }
    
    for(j=0;j<n;j++){
        d[j] = j;
    }
    for(j=1;j<n;j++){
        for(i=1;i<m;i++){
            if(a[i-1] == b[j-1]){
                d[i*n+j] = d[(i-1)*n+j-1];
            }else{
                d[i*n+j] = MIN(d[(i-1)*n+j]+1,MIN(d[(i*n)+j-1]+1,d[(i-1)*n+j-1]+1));
            }        
        }
    }
    int ret = d[m*n-1];
    free(d);
    return ret;
}

static PyObject *
string_dist_leven(PyObject *self, PyObject *args)
{
    const char *a;
    const char *b;
    int ret;

    if (!PyArg_ParseTuple(args, "ss", &a, &b))
        return NULL;
    ret = levenshteinDist(a,b);
    return PyLong_FromLong(ret);
}

static PyMethodDef StringDistMethods[] = {
    {"levenshteinDist",  string_dist_leven, METH_VARARGS,"Compute Levenshtein string distance."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef strmodule = {
   PyModuleDef_HEAD_INIT,
   "cstring_dist",   /* name of module */
   NULL, /* module documentation, may be NULL */
   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   StringDistMethods
};

PyMODINIT_FUNC
PyInit_cstring_dist(void)
{
    return PyModule_Create(&strmodule);
}
