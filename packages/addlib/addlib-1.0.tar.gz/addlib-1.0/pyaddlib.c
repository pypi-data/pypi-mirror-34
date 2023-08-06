#include "/home/webedit/BIN/Python3/include/python3.6m/Python.h"
#include "py_methods.h"

#define Py_LIMITED_API


static PyObject *
province_codes(PyObject *self, PyObject *args)
{
    GoSlice res = ProvinceCodes();
    PyObject *PyList  = PyList_New(10);
    int i=0;
    for(i = 0; i < 10; i++) {
        PyList_SetItem(PyList, i, res.data+i);
    }
    return PyList;
}

static PyMethodDef AddlibMethods[] = {
    {"province_codes", province_codes, METH_VARARGS, "returns a list of province codes"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef addlibmodule = {
   PyModuleDef_HEAD_INIT, "addlib", NULL, -1, AddlibMethods
};

PyMODINIT_FUNC
PyInit_addlib(void)
{
    return PyModule_Create(&addlibmodule);
}
