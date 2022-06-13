#include <Python.h>
#include <string.h>

static PyObject* spam_startStr(PyObject* self) {
	char* startStr = "-first index-";		
	return Py_BuildValue("s", startStr);
}static PyObject* spam_endStr(PyObject* self, PyObject* args) {	
	char* endStr = "-last index-";	
	return Py_BuildValue("s", endStr);
}static PyMethodDef SpamMethods[] = {
	{"start", spam_startStr, METH_VARARGS, "startStr"},
	{"end", spam_endStr, METH_VARARGS, "startStr"},
	{NULL, NULL, 0, NULL} // <- 배열 끝 표시. 
};

static PyModuleDef spammodule = { //2. 생성할 모듈 정보를 담는 구조체
	PyModuleDef_HEAD_INIT,
	"spam",
	"index module",
	-1, SpamMethods //3. SpamMethods 배열 참조
};
//1. 파이썬 인터프리터에서 import할 때 실행 (PyInit_<module> 함수)

PyMODINIT_FUNC PyInit_spam(void) {
	return PyModule_Create(&spammodule); //2. spammodule 구조체참조
}

