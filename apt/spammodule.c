#include <Python.h>
#include <string.h>


	char* startStr = "-first index-";		
	return Py_BuildValue("s", startStr);
}
	char* endStr = "-last index-";	
	return Py_BuildValue("s", endStr);
}
	{"start", spam_startStr, METH_VARARGS, "startStr"},
	{"end", spam_endStr, METH_VARARGS, "startStr"},
	{NULL, NULL, 0, NULL} // <- �迭 �� ǥ��. 
};

static PyModuleDef spammodule = { //2. ������ ��� ������ ��� ����ü
	PyModuleDef_HEAD_INIT,
	"spam",
	"index module",
	-1, SpamMethods //3. SpamMethods �迭 ����
};
//1. ���̽� ���������Ϳ��� import�� �� ���� (PyInit_<module> �Լ�)

PyMODINIT_FUNC PyInit_spam(void) {
	return PyModule_Create(&spammodule); //2. spammodule ����ü����
}
