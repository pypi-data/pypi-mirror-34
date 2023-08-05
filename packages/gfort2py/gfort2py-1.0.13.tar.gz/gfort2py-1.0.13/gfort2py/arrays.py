from __future__ import print_function
import ctypes
import sys
from .var import fVar, fParam
import numpy as np
from .utils import *
from .fnumpy import *
from .errors import *

_index_t = ctypes.c_int64
_size_t = ctypes.c_int64

# Pre generate alloc array descriptors
class _bounds(ctypes.Structure):
    _fields_=[("stride",_index_t),
              ("lbound",_index_t),
              ("ubound",_index_t)]

def _make_fAlloc(ndims):
    class _fAllocArray(ctypes.Structure):
        _fields_=[('base_addr',ctypes.c_void_p), 
                ('offset',_size_t), 
                ('dtype',_index_t),
                ('dims',_bounds*ndims)
                ]
    return _fAllocArray
    


# None is in there so we can do 1 based indexing
_listFAllocArrays=[None] + [_make_fAlloc(i) for i in range(1,8)] 


if sys.byteorder is 'little':
    _byte_order=">"
else:
    _byte_order="<"
    
class BadFortranArray(Exception):
    pass
    

class fExplicitArray(fVar):

    def __init__(self, lib, obj):
        self.__dict__.update(obj)
        self._lib = lib
        self._array = True
        
        if 'array' in self.var:
          self.__dict__.update(obj['var'])
        
        self._pytype = np.array
        self.ctype = self.var['array']['ctype']

        if self.pytype is 'bool':
            self.ctype='c_int32'
            self.pytype='int'
        
        self._ctype = self.ctype_def()
        
        self.ndims = int(self.array['ndim'])
        #self._ctype_f = self.ctype_def_func()

        self._dtype=self.pytype+str(8*ctypes.sizeof(self._ctype))

        #Store the ref to the lib object
        try:   
            self._ref = self._get_from_lib()
        except NotInLib:
            self._ref = None

    def ctype_to_py(self, value):
        """
        Pass in a ctype value returns the python representation of it
        """
        if self._dt_arg:
            offset = 4
        else:
            offset = 0
        
        v = np.array(self._get_var_by_iter(value, size=self._array_size(),offset=offset))
        arr = v.reshape(self._make_array_shape())
        
        return arr
        
    def py_to_ctype(self, value):
        """
        Pass in a python value returns the ctype representation of it
        
        """        
        self._data = np.asfortranarray(value.T.astype(self._dtype))

        # if '_dt_arg' in self.__dict__:
            # if self._dt_arg:
                # ct = getattr(ctypes, self.ctype)
                # addr = self._data.ctypes.get_data()
                # t = ctypes.POINTER(ct)
                # return ctypes.cast(addr,t)

        return self._data
        
    def py_to_ctype_f(self, value):
        """
        Pass in a python value returns the ctype representation of it, 
        suitable for a function
        
        Second return value is anything that needs to go at the end of the
        arg list, like a string len
        """
        self._data = np.asfortranarray(value.T.astype(self._dtype))

        return self._data,None
        
    def ctype_to_py_f(self, value):
        """
        Pass in a ctype value returns the python representation of it,
        as returned by a function (may be a pointer)
        """
        self._value = np.asfortranarray(value,dtype=self._dtype)
        return self._value

    def pytype_def(self):
        return self._pytype

    def ctype_def(self):
        """
        The ctype type of this object
        """
        if '_cached_ctype' not in self.__dict__:
            self._cached_ctype = getattr(ctypes, self.ctype)
        
        if '_dt_arg' in self.__dict__:
            if self._dt_arg:
                self._cached_ctype = ctypes.POINTER(getattr(ctypes, self.ctype))
        
        return self._cached_ctype

    def ctype_def_func(self,pointer=False,intent=''):
        """
        The ctype type of a value suitable for use as an argument of a function

        May just call ctype_def
        
        Second return value is anythng that needs to go at the end of the
        arg list, like a string len
        """
        if pointer:
            raise ValueError("Can't have explicit array as a pointer")
        
        x=np.ctypeslib.ndpointer(dtype=self._dtype,ndim=self.ndims,
                                shape=tuple(self._make_array_shape()),
                                flags='F_CONTIGUOUS')
        y=None
        return x,y        
        
    def set_mod(self, value):
        """
        Set a module level variable
        """
        v = value.flatten(order='C')
        self._set_var_from_iter(self._ref, v, self._array_size())
        
    def get(self,copy=True):
        """
        Get a module level variable
        """
        s = self.ctype_to_py(self._ref)
        shape = self._make_array_shape()
        return np.reshape(s, shape)

    def _make_array_shape(self,bounds=None):
        if bounds is None:
            bounds = self.array['shape']
        
        shape = []
        for i, j in zip(bounds[0::2], bounds[1::2]):
            shape.append(j - i + 1)
        return shape

    def _array_size(self,bounds=None):
        return np.product(self._make_array_shape(bounds))
       
    def py_to_ctype_p(self,value):
        """
        The ctype representation suitable for function arguments wanting a pointer
        """
        return np.ctypeslib.as_ctypes(value)



class fDummyArray(fVar):
    _GFC_MAX_DIMENSIONS = 7

    _GFC_DTYPE_RANK_MASK = 0x07
    _GFC_DTYPE_TYPE_SHIFT = 3
    _GFC_DTYPE_TYPE_MASK = 0x38
    _GFC_DTYPE_SIZE_SHIFT = 6

    _BT_UNKNOWN = 0
    _BT_INTEGER = _BT_UNKNOWN + 1
    _BT_LOGICAL = _BT_INTEGER + 1
    _BT_REAL = _BT_LOGICAL + 1
    _BT_COMPLEX = _BT_REAL + 1
    _BT_DERIVED = _BT_COMPLEX + 1
    _BT_CHARACTER = _BT_DERIVED + 1
    _BT_CLASS = _BT_CHARACTER + 1
    _BT_PROCEDURE = _BT_CLASS + 1
    _BT_HOLLERITH = _BT_PROCEDURE + 1
    _BT_VOID = _BT_HOLLERITH + 1
    _BT_ASSUMED = _BT_VOID + 1
    
    _BT_TYPESPEC = {_BT_UNKNOWN:'v',_BT_INTEGER:'i',_BT_LOGICAL:'b',
                    _BT_REAL:'f',_BT_COMPLEX:'c',_BT_DERIVED:'v',
                    _BT_CHARACTER:'v',_BT_CLASS:'v',_BT_PROCEDURE:'v',
                    _BT_HOLLERITH:'v',_BT_VOID:'v',_BT_ASSUMED:'v'}
                    
    _PY_TO_BT = {'int':_BT_INTEGER,'float':_BT_REAL,'bool':_BT_LOGICAL,
                'str':_BT_CHARACTER,'bytes':_BT_CHARACTER}


    def __init__(self, lib, obj):
        self.__dict__.update(obj)
        self._lib = lib
        self._array = True

        if 'array' in self.var:
          self.__dict__.update(obj['var'])

        self.ndim = int(self.array['ndim'])
        self._lib = lib
        
        if self.pytype is 'bool':
            self.ctype='c_int32'
            self.pytype='int'
        
        
        self._desc = self._setup_desc()
        self._ctype_single = getattr(ctypes,self.ctype)
        #self._ctype = getattr(ctypes,self.ctype)
        self._ctype = self._desc
        self._ctype_desc = ctypes.POINTER(self._desc)
        self.npdtype=self.pytype+str(8*ctypes.sizeof(self._ctype_single))

    def _setup_desc(self):
        return _listFAllocArrays[self.ndim]

    def _get_pointer(self):
        return self._ctype_desc.from_address(ctypes.addressof(getattr(self._lib,self.mangled_name)))

    def set_mod(self, value):
        """
        Set a module level variable
        """
        
        if not self.ndim == value.ndim:
            raise ValueError("Array size mismatch "+str(self.ndim)+' '+str(value.ndim))
        
        
        self._value = value.astype(self.npdtype)
        
        #Did we make a copy?
        # if self._id(self._value)==self._id(value):
            # remove_ownership(value)
        remove_ownership(self._value)
        
        p = self._get_pointer()
        if p:
            self._set_to_pointer(self._value,p.contents)
        
        return 
        
    def set_func_arg(self,value):
        #Create an allocatable array
        self._value_array = self._desc()

        self._value = np.asfortranarray(value).astype(self.npdtype)
        self._set_to_pointer(self._value,self._value_array)
        
        
    def _set_to_pointer(self,value,p):
        if value.ndim > self._GFC_MAX_DIMENSIONS:
            raise ValueError("Array too big")
        
        p.base_addr = value.ctypes.get_data()
        p.offset = _size_t(-1)
        
        p.dtype = self._get_dtype()
        
        for i in range(self.ndim):
            p.dims[i].stride = _index_t(value.strides[i]//ctypes.sizeof(self._ctype_single))
            p.dims[i].lbound = _index_t(1)
            p.dims[i].ubound = _index_t(value.shape[i])
            
        return

    def get(self,copy=False):
        """
        Get a module level variable
        """
        if self._dt_arg:
            return self._value
           
        p = self._get_pointer()
        return self._get_from_pointer(p.contents,copy)
        
    def _get_from_pointer(self,p,copy=False):
        if not self._isallocated():
            return np.zeros(1)
            #raise ValueError("Array not allocated yet")
        base_addr = p.base_addr
        offset = p.offset
        dtype = p.dtype
        
        dims=[]
        shape=[]
        for i in range(self.ndim):
            dims.append({})
            dims[i]['stride'] = p.dims[i].stride
            dims[i]['lbound'] = p.dims[i].lbound
            dims[i]['ubound'] = p.dims[i].ubound
            
        for i in range(self.ndim):
            shape.append(dims[i]['ubound']-dims[i]['lbound']+1)
            
        self._shape=tuple(shape)
        size = np.product(shape)
        
        if copy:
            # When we want a copy of the array not a pointer to the fortran memoray
            res = self._get_var_from_address(base_addr,size=size)
            res = np.asfortranarray(res)
            res = res.reshape(shape).astype(self.npdtype)
        else:
            # When we want to pointer to the underlaying fortran memoray
            # will leak as we dont have a deallocate call to call in a del func
            ptr = ctypes.cast(base_addr,ctypes.POINTER(self._ctype_single))
            res = np.ctypeslib.as_array(ptr,shape= self._shape)
        
        return res
        

    def py_to_ctype(self, value):
        """
        Pass in a python value returns the ctype representation of it
        """
        self.set_func_arg(value)
        return self._value_array
        
    def py_to_ctype_f(self, value):
        """
        Pass in a python value returns the ctype representation of it, 
        suitable for a function
        
        Second return value is anything that needs to go at the end of the
        arg list, like a string len
        """
        return self.py_to_ctype(value),None

    def ctype_to_py(self, value):
        """
        Pass in a ctype value returns the python representation of it
        """
        return self.ctype_to_py_f(value.contents)
        
    def ctype_to_py_f(self, value):
        """
        Pass in a ctype value returns the python representation of it,
        as returned by a function (may be a pointer)
        """
        if hasattr(value,'contents'):
            return self._get_from_pointer(value.contents)
        else:
            return self._get_from_pointer(value)

            
    def py_to_ctype_p(self,value):
        """
        The ctype represnation suitable for function arguments wanting a pointer
        """
        return self.py_to_ctype(value)
            

    def pytype_def(self):
        return np.array

    def ctype_def(self):
        """
        The ctype type of this object
        """
        return self._ctype_desc

    def ctype_def_func(self,pointer=False,intent=''):
        """
        The ctype type of a value suitable for use as an argument of a function

        May just call ctype_def
        
        Second return value is anythng that needs to go at the end of the
        arg list, like a string len
        """

        return self.ctype_def(),None

    def _get_dtype(self):
        ftype=self._get_ftype()
        d=self.ndim
        d=d|(ftype<<self._GFC_DTYPE_TYPE_SHIFT)
        d=d|(ctypes.sizeof(self._ctype_single)<<self._GFC_DTYPE_SIZE_SHIFT)
        return d

    def _get_ftype(self):
        ftype=None
        dtype=self.ctype
        if 'c_int' in dtype:
            ftype=self._BT_INTEGER
        elif 'c_double' in dtype or 'c_real' in dtype or 'c_float' in dtype:
            ftype=self._BT_REAL
        elif 'c_bool' in dtype:
            ftype=self._BT_LOGICAL
        elif 'c_char' in dtype:
            ftype=self._BT_CHARACTER
        else:
            raise ValueError("Cant match dtype, got "+dtype)
        return ftype

    def __str__(self):
        x=self.get()
        if x is None:
            return "<array>"
        else:
            return str(self.get())
        
    def __repr__(self):
        x=self.get()
        if x is None:
            return "<array>"
        else:
            return repr(self.get())

    def __getattr__(self, name): 
        if name in self.__dict__:
            return self.__dict__[name]

        #return getattr(self.get(),name)
        
    def __del__(self):
        if '_value' in self.__dict__:
            #Problem occurs as both fortran and numpy are pointing to same memory address
            #Thus if fortran deallocates the array numpy will try to free the pointer
            #when del is called casuing a double free error
            
            #By calling remove_ownership we tell numpy it dosn't own the data
            #thus is shouldn't call free(ptr).
            remove_ownership(self._value)
            
            #Maybe leaks if fortran doesn't dealloc the array
                
                
    def _isallocated(self):
        
        try:
            p = self._get_pointer()
        except TypeError:
            return False
        if p.contents.base_addr:
            #Base addr is NULL if deallocated
            return True
        else:
            return False
        
    def _id(self,x):
        return x.ctypes.data
        
    def _create_dtype(self,ndim,itemsize,ftype):
        ftype=self._get_BT(ftype)
        d=ndim
        d=d|(ftype<<self._GFC_DTYPE_TYPE_SHIFT)
        d=d|int(itemsize)<<self._GFC_DTYPE_SIZE_SHIFT
        return d
    
    def _get_BT(self,ftype):
        if 'int' in ftype:
            BT=self._BT_INTEGER
        elif 'float' in ftype:
            BT=self._BT_REAL
        elif 'bool' in ftype:
            BT=self._BT_LOGICAL
        elif 'str' in ftype or 'bytes' in ftype:
            BT=self._BT_CHARACTER
        else:
            raise ValueError("Cant match dtype, got "+ftype)
        return BT
        
    def _BT_to_typestr(self,BT):
        try:
            res = self._BT_TYPESPEC[BT]
        except KeyError:
            raise BadFortranArray("Bad BT value "+str(BT))
            
        return _byte_order+res
    

    def _split_dtype(self,dtype):
        itemsize = dtype >> self._GFC_DTYPE_SIZE_SHIFT
        BT = (dtype >> self._GFC_DTYPE_TYPE_SHIFT ) & (self._GFC_DTYPE_RANK_MASK)
        ndim = dtype & self._GFC_DTYPE_RANK_MASK
        
        return ndim,BT,int(itemsize)
   
class fAssumedShape(fDummyArray):
    def _get_pointer(self):
        return self._ctype_desc.from_address(ctypes.addressof(self._value_array))
    
    
    def set_func_arg(self,value):
        
        super(fAssumedShape,self).set_func_arg(value)
        
        #Fix up bounds
    
        #From gcc source code
        #Parsed       Lower   Upper  Returned
        #------------------------------------
          #:           NULL    NULL   AS_DEFERRED (*)
          #x            1       x     AS_EXPLICIT
          #x:           x      NULL   AS_ASSUMED_SHAPE
          #x:y          x       y     AS_EXPLICIT
          #x:*          x      NULL   AS_ASSUMED_SIZE
          #*            1      NULL   AS_ASSUMED_SIZE
          
       # for i in range(self.ndim):
            #print(self._value_array.dims[i].lbound,self._value_array.dims[i].ubound)
            #self._value_array.dims[i].ubound=0
            #self._value_array.dims[i].lbound=0
            
    def __str__(self):
        return str(self._value_array)
        
    def __repr__(self):
        return repr(self._value_array)

    def py_to_ctype(self, value):
        """
        Pass in a python value returns the ctype representation of it
        """
        self.set_func_arg(value)
        return self._value_array
        
    def py_to_ctype_f(self, value):
        """
        Pass in a python value returns the ctype representation of it, 
        suitable for a function
        
        Second return value is anything that needs to go at the end of the
        arg list, like a string len
        """
        return self.py_to_ctype(value),None    
    
class fAssumedSize(fExplicitArray):
    
    
    def ctype_def_func(self,pointer=False,intent=''):
        """
        The ctype type of a value suitable for use as an argument of a function

        May just call ctype_def
        
        Second return value is anythng that needs to go at the end of the
        arg list, like a string len
        """
        
        x=ctypes.POINTER(getattr(ctypes, self.ctype))
        y=None
        return x,y  
    
    def _make_array_shape(self,bounds=None):
        
        return [99]*self.ndims
    
    
    def py_to_ctype_p(self,value):
        """
        The ctype representation suitable for function arguments wanting a pointer
        """
        self._data = value
        ct = getattr(ctypes, self.ctype)
        addr = self._data.ctypes.get_data()
        t = ctypes.POINTER(ct)
        return ctypes.cast(addr,t)
        
    def py_to_ctype_f(self,value):
        """
        The ctype representation suitable for function arguments wanting a pointer
        """
        return self.py_to_ctype_p(value),None

class fAllocatableArray(fDummyArray):
    def py_to_ctype(self, value):
        """
        Pass in a python value returns the ctype representation of it
        """
        self.set_func_arg(value)
        
        # self._value_array needs to be empty if the array is allocatable and not
        # allready allocated
        self._value_array.base_addr=ctypes.c_void_p(0)
        
        return self._value_array
        
    def py_to_ctype_f(self, value):
        """
        Pass in a python value returns the ctype representation of it, 
        suitable for a function
        
        Second return value is anything that needs to go at the end of the
        arg list, like a string len
        """
        return self.py_to_ctype(value),None   
        
    def ctype_to_py_f(self, value):
        """
        Pass in a ctype value returns the python representation of it,
        as returned by a function (may be a pointer)
        """
        shape=[]
        for i in value.dims:
            shape.append(i.ubound-i.lbound+1)
        shape=tuple(shape)
        
        p=ctypes.POINTER(self._ctype_single)
        res=ctypes.cast(value.base_addr,p)
        return np.ctypeslib.as_array(res,shape=shape)
        

    
class fParamArray(fParam):
    def get(self):
        """
        A parameters value is stored in the dict, as we cant access them
        from the shared lib.
        """
        return np.array(self.value, dtype=self.pytype)




