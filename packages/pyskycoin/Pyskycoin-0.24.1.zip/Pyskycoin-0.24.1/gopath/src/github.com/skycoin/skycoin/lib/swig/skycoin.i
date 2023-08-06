%module skycoin
%include "typemaps.i"
%{
	#define SWIG_FILE_WITH_INIT
	#include "libskycoin.h"
	#include "swig.h"
%}


//Apply typemaps for Python for now
//It can be applied to other languages that fit in
//Not languages can't return multiple values
#if defined(SWIGPYTHON)
%include "golang.cgo.i"
%include "skycoin.mem.i"
%include "structs_typemaps.i"
#endif

//Apply strictly to python
//Not for other languages
#if defined(SWIGPYTHON)
%include "python_skycoin.cipher.crypto.i"
%include "python_skycoin.coin.i"
#else
%include "skycoin.cipher.crypto.i"
%include "skycoin.coin.i"
#endif

%include "swig.h"
/* Find the modified copy of libskycoin */
%include "libskycoin.h"
%include "structs.i"
