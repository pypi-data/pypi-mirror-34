"""Stoner.Core provides the core classes for the Stoner package."""
from __future__ import print_function
__all__ = ["StonerLoadError", "StonerSetasError","_setas","regexpDict","typeHintedDict","metadataObject","DataArray","DataFile"]

import re
#import pdb # for debugging
import os
import io
import copy
import warnings
import os.path as path
import inspect as _inspect_
from textwrap import TextWrapper
from ast import literal_eval
import itertools
from collections import OrderedDict,MutableMapping
from traceback import format_exc
import csv
import numpy as _np_
from numpy import NaN # pylint: disable=unused-import
import numpy.ma as _ma_

from .compat import python_v3,string_types,int_types,index_types,get_filedialog,classproperty,str2bytes,bytes2str
from .tools import isNone,all_size,all_type,_attribute_store,operator,isiterable,typedList,islike_list,get_option,istuple

try:
    from tabulate import tabulate
    tabulate.PRESERVE_WHITESPACE = True
except ImportError:
    tabulate=None


try:
    assert not python_v3 # blist doesn't seem entirely reliable in 3.5 :-(
    from blist import sorteddict
except (AssertionError,ImportError): #Fail if blist not present or Python 3
    sorteddict=OrderedDict
try:
    from magic import Magic as filemagic,MAGIC_MIME_TYPE
except ImportError:
    filemagic=None

def copy_into(source,dest):
    """Copies the data associated with source to dest.

    Args:
        source(DataFile): The DataFile object to be copied from
        dest (DataFile): The DataFile objrct to be changed by recieving the copiued data.

    Returns:
        The modified *dest* DataFile.

    Unlike copying or deepcopying a DataFile, this function preserves the class of the destination and just
    overwrites the attributes that represent the data in the DataFile.
    """
    dest.data = source.data.copy()
    dest.setas=source.setas
    for attr in source._public_attrs:
        if not hasattr(source,attr) or callable(getattr(source,attr)) or attr in ["data"]:
            continue
        try:
            setattr(dest,attr,copy.deepcopy(getattr(source,attr)))
        except NotImplementedError: # Deepcopying failed, so just copy a reference instead
            setattr(dest,attr,getattr(source,attr))
    return dest

class StonerLoadError(Exception):

    """An exception thrown by the file loading routines in the Stoner Package.

    This special exception is thrown when one of the subclasses of :py:class:`Stoner.Core.DataFile`
    attmpts and then fails to load some data from disk. Generally speaking this is not a real
    error, but simply indicates that the file format is not recognised by that particular subclass,
    and thus another subclass should have a go instead.
    """

    pass

class StonerSetasError(AttributeError):

    """An exception tjrown when we try to access a column in data without setas being set."""

    pass


class _tab_delimited(csv.Dialect):

    """A customised csv dialect class for reading tab delimited text files."""

    delimiter = "\t"
    quoting = csv.QUOTE_NONE
    doublequote = False
    lineterminator = "\r\n"


class _setas(MutableMapping):

    """A Class that provides a mechanism for managing the column assignments in a DataFile like object.

    Implements a MutableMapping bsed on the column_headers as the keys (with a few tweaks!).

    Note:
        Iterating over setas will return the column assignments rather than the standard mapping behaviour of iterating over the keys. Otherwise
        the interface is essentially as a Mapping class.
    """

    _col_defaults={2: {"axes":2,"xcol":0,"ycol":1,"zcol":None,"ucol":None,"vcol":None,"wcol":None,"xerr":None,"yerr":None,"zerr":None}, # xy
                  3: {"axes":2,"xcol":0,"ycol":1,"zcol":None,"ucol":None,"vcol":None,"wcol":None,"xerr":None,"yerr":2,"zerr":None}, # xye
                  4: {"axes":2,"xcol":0,"ycol":2,"zcol":None,"ucol":None,"vcol":None,"wcol":None,"xerr":1,"yerr":3,"zerr":None}, #xdye
                  5: {"axes":5,"xcol":0,"ycol":1,"zcol":None,"ucol":2,"vcol":3,"wcol":4,"xerr":None,"yerr":None,"zerr":None}, #xyuvw
                  6: {"axes":6,"xcol":0,"ycol":1,"zcol":2,"ucol":3,"vcol":4,"wcol":5,"xerr":None,"yerr":None,"zerr":None},} # xyzuvw


    def __init__(self, initial_val=None, **kargs):
        """Constructs the setas instance and sets an initial value.

        Args:
            ref (DataFile): Contains a reference to the owning DataFile instance

        Keyword Arguments:
            initial_val (string or list or dict): Initial values to set
        """
        self._row=kargs.pop("_row",False)
        self._cols = _attribute_store()
        self._shape=tuple()
        self._setas = list()
        self._column_headers = typedList(string_types)


        if initial_val is not None:
            self(initial_val)
        elif kargs:
            self(**kargs)

    def _decode_string(self,value):
        """Expands a string of column assignments, replacing numbers with repeated characters."""
        pattern = re.compile("[^0-9]*(([0-9]+?)(x|y|z|d|e|f|u|v|w|\.|\-))")
        while True:
            res = pattern.match(value)
            if res is None:
                break
            (total, count, code) = res.groups()
            if count == "":
                count = 1
            else:
                count = int(count)
            value = value.replace(total, code * count, 1)
        return value

    def _prepare_call(self,args,kargs):
        """Extract a value to be used to evaluate the setas attribute during a call."""
        reset=kargs.pop("reset",True)
        if not isinstance(reset,bool):
            reset=True

        if args:
            value = args[0]
            if isinstance(value, string_types):  # expand the number-code combos in value
                if reset:
                    self.setas=[]
                value=self._decode_string(value)
            elif isinstance(value, _setas):
                value = value.setas
        else:
            value = kargs
            if reset:
                self.setas=[]
        return value

    @property
    def _size(self):
        """Calculate a size of the setas attribute."""
        if len(self._shape)==1 and self._row:
            c=self._shape[0]
        elif len(self._shape)==1:
            c=1
        elif len(self._shape)>1:
            c=self.shape[1]
        else:
            c=len(self._column_headers)
        return c

    @property
    def _unique_headers(self):
        """Return either a column header or an index if the column_header is duplicated."""
        ret=[]
        for i,ch in enumerate(self.column_headers):
            if ch not in ret:
                ret.append(ch)
            else:
                ret.append(i)
        return ret

    @property
    def clone(self):
        """Create an exact copy of the current object."""
        cls=self.__class__
        new = cls()
        for attr in self.__dict__:
            if not callable(self.__dict__[attr]):
                new.__dict__[attr] = copy.deepcopy(self.__dict__[attr])
        return new

    @property
    def cols(self):
        """Get the current column assignments."""
        if not self._cols:
            self._cols.update(self._get_cols())
        return self._cols

    @cols.setter
    def cols(self,value):
        """Update the current column assignments."""
        if not isinstance(value,dict):
            raise AttributeError("cols attribute must be a dictionary")
        self._cols=_attribute_store(value)

    @property
    def column_headers(self):
        """Get the current column headers."""
        c=self._size
        l=len(self._column_headers)
        if l<c: # Extend the column headers if necessary
            self._column_headers.extend(["Column {}".format(i+l) for i in range(c-l)])
        return self._column_headers

    @column_headers.setter
    def column_headers(self,value):
        """Set the colum headers."""
        if isinstance(value,_np_.ndarray): #Convert ndarray to list of strings
            value=value.astype(str).tolist()
        self._column_headers=typedList(string_types,value)

    @property
    def not_set(self):
        """Return a boolean array if not set."""
        return _np_.array([x=="." for x in self._setas])

    @property
    def set(self):
        """Return a boolean array if column is set."""
        return ~self.not_set

    @property
    def setas(self):
        """Guard the setas attribute."""
        c=self._size
        l=len(self._setas)
        if c>l:
            self._setas.extend(["."]*(c-l))
        self._setas=self._setas[:c]
        return self._setas

    @setas.setter
    def setas(self,value):
        """Minimal attribute setter."""
        self._setas=value

    @property
    def shape(self):
        """Return the shape of the array that we think we are."""
        return self._shape

    @shape.setter
    def shape(self,value):
        """Update the note of our shape."""
        value=tuple(value)
        if 0<=len(value)<=2:
            self._shape=tuple(value)
        else:
            raise AttributeError("shape attribute should be a 2-tuple not a {}-tuple".format(len(value)))

    def __call__(self, *args, **kargs):
        """Treat the current instance as a callable object and assign columns accordingly.

        Variois forms of this method are accepted::

        setas("xyzuvw")
        setas(["x"],["y"],["z"],["u"],["v"],["w"])
        setas(x="column_1",y=3,column4="z")
        """
        if not (args  or kargs): #New - bare call to setas will return the current value.
            return self.setas
        if len(args)==1 and not (isinstance(args[0], string_types+(_setas,)) or isiterable(args[0])):
            raise SyntaxError("setas should be called with eother a string, iterable object or setas object, not a {}".format(type(args[0])))

        #If reset is neither in kargs nor a False boolean, then clear the existing setas assignments
        value=self._prepare_call(args,kargs)
        _=self.setas # Forxce setas to be the right length
        if isinstance(value, dict):
            for k,v in value.items():
                if isinstance(k,string_types) and len(k)==1 and k in "xyzuvwdef": #of the form x:column_name
                    for v_item in self.find_col(v,force_list=True):
                        try:
                            self._setas[v_item]=k
                        except:
                            print(len(self._setas),v,v_item,k)
                elif isinstance(k, index_types) and isinstance(v,string_types) and len(v)==1 and v in "xyzuvwdef": #of the form column_name:x
                    k=self.find_col(k)
                    self._setas[k]=v
                else:
                    raise IndexError("Unable to workout what do with {}:{} when setting the setas attribute.".format(k,v))
        elif isiterable(value):
            if len(value) > self._size:
                value = value[:self._size]
            elif len(value) < self._size:
                value = [v for v in value]  # Ensure value is now a list
                value.extend(list("." * (self._size - len(value))))
            value=value[:self._size]
            for i, v in enumerate(value):
                if v.lower() not in "xyzedfuvw.-":
                    raise ValueError("Set as column element is invalid: {}".format(v))
                if v != "-":
                    self.setas[i] = v.lower()
        else:
            raise ValueError("Set as column string ended with a number")
        self.cols.update(self._get_cols())

    def __contains__(self,item):
        """Use getitem to test for membership. Either column assignments or column index types are tested."""
        try:
            _=self[item]
        except (IndexError,KeyError,ValueError):
            return False
        return True

    def __delitem__(self,name):
        """Unset either by column index or column assignment.

        Equivalent to unsetting the same object."""
        self.unset(name)

    def __eq__(self,other):
        """Checks to see if this is the same object, or has the same headers and the same setas values."""
        ret=False
        if isinstance(other,string_types): # Expand strings and convert to list
            other=[c for c in self._decode_string(other)]
        if not isinstance(other,_setas): # Ok, need to check whether items match
            if isiterable(other) and len(other)<=self._size:
                for m in self.setas[len(other):]: #Check that if other is short we don't have assignments there
                    if m!=".":
                        return False
                for o,m in zip(other,self.setas):
                    if o!=m: # Look for mis-matched assignments
                        return False
                else:
                    return True
            else: # If other is longer then we can't matchj
                return False
        elif id(self)==id(other):
            ret=True
        else:
            ret=(self.column_headers==other.column_headers and self.setas==other.setas)
        return ret

    def __getattr__(self,name):
        """Try to see if attribute name is a key in self.cols and return that instead."""
        if name in self.cols:
            return self.cols[name]
        return super(_setas,self).__getattr__(name)

    def __getitem__(self, name):
        """Permit the setas attribute to be treated like either a list or a dictionary.

        Args:
            name (int, slice or string): if *name* is an integer or a slice, return the column type
                of the corresponding column(s). If a string, should be a single letter
                from the set x,y,z,u,v,w,d,e,f - if so returns the corresponding
                column(s)

        Returns:
            Either a single letter x,y,z,u,v,w,d,e or f, or a list of letters if used in
            list mode, or a single coliumn name or list of names if used in dictionary mode.
        """
        if isinstance(name, string_types) and len(name) == 1 and name in "xyzuvwdef.-":
            ret = list()
            s=0
            while name in self._setas[s:]:
                s=self._setas.index(name)+1
                ret.append(self.column_headers[s-1])
            if len(ret)==1:
                ret=ret[0]
        elif isinstance(name, string_types) and len(name) == 2 and name[0]=="#" and name[1] in "xyzuvwdef.-":
            ret = list()
            name=name[1]
            s=0
            while name in self._setas[s:]:
                s=self._setas.index(name)+1
                ret.append(s-1)
            if len(ret)==1:
                ret=ret[0]
        elif isinstance(name,index_types):
            ret=self.setas[self.find_col(name)]
        elif isinstance(name, slice):
            indices = name.indices(len(self.setas))
            name = range(*indices)
            ret = [self[x] for x in name]
        elif isiterable(name):
            ret=[self[x] for x  in name]
        else:
            raise IndexError("{} was not found in the setas attribute.".format(name))
        return ret

    def __iter__(self):
        """Iterate over thew column assignments.

        .. warn::

            This class does not follow standard Mapping semantics - iterating iterates over the values and not the items.
        """
        _=self.setas #Force setas to fix size
        for c in self._setas:
            yield c

    def __ne__(self,other):
        """!= is the same as no ==."""
        return not self.__eq__(other)

    def __setitem__(self, name, value):
        """Allow setting of the setas variable like a dictionary or a list.

        Args:
            name (string or int): If name is a string, it should be in the set x,y,z,u,v,w,d,e or f
                and value should be a column index type. If name is an integer, then value should be
                a single letter string in the set above.
            value (integer or column index): See above.
        """
        if islike_list(name): #Sipport indexing with a list like object
            if islike_list(value) and len(value)==len(name):
                for n,v in zip(name,value):
                    self._setas[n]=v
            else:
                for n in name:
                    self[n]=value
        elif isinstance(name, string_types) and len(name) == 1 and name in "xyzuvwdef.-": #indexing by single letter
            for c in self.find_col(value,force_list=True):
                self._setas[c]=name
        elif isinstance(name,index_types) and isinstance(value,string_types) and len(value)==1 and value in "xyzuvwdef.-":
            for c in self.find_col(name,force_list=True):
                self.setas[c]=value

    def __len__(self):
        """Return our own length."""
        return self._size

    def __repr__(self):
        """Our representation is as a list of the values."""
        return self.setas.__repr__()

    def __str__(self):
        """Our string representation is just fromed by joing the assingments together."""
        #Quick string conversion routine
        return "".join(self.setas)

    #################################################################################################################
    #############################   Operator Methods ################################################################

    def __add_core__(self,new,other):
        """Allow the user to add a dictionary to setas to add extra columns."""
        if isinstance(other,_setas): #Deal with the other value being a setas attribute already.
            other=other.to_dict()
        elif istuple(other,index_types,string_types) or istuple(other,string_types,index_types):
            other={other[0]:other[1]}
        if not isinstance(other,dict):
            return NotImplemented
        for k,v in other.items():
            if isinstance(k,string_types) and len(k)==1 and k in "xyzuvwdef": #of the form x:column_name
                for v in new.find_col(v,force_list=True):
                    new._setas[v]=k
            elif isinstance(k, index_types) and isinstance(v,string_types) and len(v)==1 and v in "xyzuvwdef": #of the form column_name:x
                k=new.find_col(k)
                new._setas[k]=v
            else:
                raise IndexError("Unable to workout what do with {}:{} when setting the setas attribute.".format(k,v))
        return new

    def __add__(self,other):
        """Jump to the core."""
        new=self.clone
        return self.__add_core__(new,other)

    def __iadd__(self,other):
        """Jump to the core."""
        new=self
        return self.__add_core__(new,other)

    def __sub_core__(self,new,other):
        """Implement subtracting either column indices or x,y,z,d,e,f,u,v,w for the current setas."""
        if isinstance(other,string_types) and len(other)==1 and other in "xyzuvwdef":
            while True:
                try:
                    new._setas[new._setas.index(other)]="."
                except ValueError:
                    break
        elif isinstance(other,index_types):
            try:
                new._setas[new.find_col(other)]="."
            except KeyError:
                pass
        elif isiterable(other):
            for o in other:
                new=self.__sub_core__(new,o)
                if new is NotImplemented:
                    return NotImplemented
        else:
            return NotImplemented
        return new


    def __sub__(self,other):
        """Jump to the core."""
        new=self.clone
        return self.__sub_core__(new,other)

    def __isub__(self,other):
        """Jump to the core."""
        new=self
        return self.__sub_core__(new,other)

    def find_col(self, col, force_list=False):
        """Indexes the column headers in order to locate a column of data.shape.

        Indexing can be by supplying an integer, a string, a regular experssion, a slice or a list of any of the above.

        -   Integer indices are simply checked to ensure that they are in range
        -   String indices are first checked for an exact match against a column header
            if that fails they are then compiled to a regular expression and the first
            match to a column header is taken.
        -   A regular expression index is simply matched against the column headers and the
            first match found is taken. This allows additional regular expression options
            such as case insensitivity.
        -   A slice index is converted to a list of integers and processed as below
        -   A list index returns the results of feading each item in the list at :py:meth:`find_col`
            in turn.

        Args:
            col (int, a string, a re, a slice or a list):  Which column(s) to retuirn indices for.

        Keyword Arguments:
            force_list (bool): Force the output always to be a list. Mainly for internal use only

        Returns:
            The matching column index as an integer or a KeyError
        """
        if isinstance(col, int_types):  # col is an int so pass on
            if col >= len(self.column_headers):
                raise IndexError('Attempting to index a non - existant column {}'.format(col))
            if col < 0:
                col = col % len(self.column_headers)
        elif isinstance(col, string_types):  # Ok we have a string
            col = str(col)
            if col in self.column_headers:  # and it is an exact string match
                col = self.column_headers.index(col)
            else:  # ok we'll try for a regular expression
                test = re.compile(col)
                possible = [x for x in self.column_headers if test.search(x)]
                if not possible:
                    try:
                        col = int(col)
                    except ValueError:
                        raise KeyError('Unable to find any possible column matches for "{} in {}"'.format(col,self.column_headers))
                    if col < 0 or col >= self.data.shape[1]:
                        raise KeyError('Column index out of range')
                else:
                    col = self.column_headers.index(possible[0])
        elif isinstance(col, re._pattern_type):
            test = col
            possible = [x for x in self.column_headers if test.search(x)]
            if not possible:
                raise KeyError('Unable to find any possible column matches for {}'.format(col.pattern))
            else:
                col = self.find_col(possible)
        elif isinstance(col, slice):
            indices = col.indices(self.shape[1])
            col = range(*indices)
            col = self.find_col(col)
        elif isiterable(col):
            col = [self.find_col(x) for x in col]
        else:
            raise TypeError('Column index must be an integer, string, list or slice, not a {}'.format(type(col)))
        if force_list and not isinstance(col, list):
            col = [col]
        return col

    def clear(self):
        """"Clear the current setas attrbute.

        Notes:
            Equivalent to doing :py:meth:`_setas.unset` with no argument.
        """
        self.unset()

    def get(self,name,default=None):
        """Implement a get method."""
        try:
            return self[name]
        except (IndexError,KeyError):
            if default is not None:
                return default
            else:
                raise KeyError("{} is not in setas and no default was given.".format(name))

    def keys(self):
        """Mapping keys are the same as iterating over the unique headers"""
        for c in self._unique_headers:
            yield c

    def values(self):
        """Mapping values are the same as iterating over setas."""
        for v in self.setas:
            yield v

    def items(self):
        """Mapping items iterates over keys and values."""
        for k,v in zip(self._unique_headers,self.setas):
            yield k,v

    def pop(self,name,default=None):
        """Implement a get method."""
        try:
            ret=self[name]
            self.unset(name)
            return ret
        except (IndexError,KeyError):
            if default is not None:
                return default
            else:
                raise KeyError("{} is not in setas and no default was given.".format(name))

    def popitem(self):
        for c in "xdyezfuvw":
            if c in self:
                v=self[c]
                self.unset(c)
                return (c,v)
        else:
            raise KeyError("No columns set in setas!")

    def setdefault(self,name,default=None):
        """Implement a setdefault method."""
        try:
            return self[name]
        except (IndexError,KeyError):
            self[name]=default
            return default

    def unset(self,what=None):
        """Remove column settings from the setas attribute in  method call.

        Parameters:
            what (str,iterable,dict or None): What to unset.

        Notes:
            The *what* parameter determines what to unset, possible values are:

            -   A single lets from *xyzuvwdef* - all column assignments of the corresponding type are unset
            -   A column index type - all matching columns are unset
            -   A list or other iterable of the above - all matching entries are unset
            -   None - all setas assignments are cleared.
        """
        if what is None:
            self.setas=[]
            _=self.setas
        else:
            self-=what

    def update(self,other):
        """Replace any assignments in self with assignments from other."""
        if isinstance(other,_setas):
            other=other.to_dict()
        elif not isinstance(other,dict):
            raise TypeError("setas.update requires a dictionary not a {}".format(type(other)))
        vals=list(other.values())
        keys=list(other.keys())
        for k in "xyzuvwdef":
            if k in other:
                try:
                    c=self[k]
                    self[c]="."
                except IndexError:
                    pass
                self[k]=other[k]
            elif k in vals:
                try:
                    c=self[k]
                    self[c]="."
                except IndexError:
                    pass
                self[k]=keys[vals.index(k)]
        return self

    def to_dict(self):
        """Return the setas attribute as a dictionary.

        If multiple columns are assigned to the same type, then the column names are
        returned as a list. If column headers are duplicated"""
        ret=dict()
        for i,(k,ch) in enumerate(zip(self._setas,self._unique_headers)):
            if k!=".":
                if k in ret:
                    ret[k].append(ch)
                else:
                    ret[k]=[ch]
        for k in ret:
            if len(ret[k])==1:
                ret[k]=ret[k][0]
        return ret

    def _get_cols(self, what=None, startx=0,no_guess=False):
        """Uses the setas attribute to work out which columns to use for x,y,z etc.

        Keyword Arguments:
            what (string): Returns either xcol, ycol, zcol, ycols,xcols rather than the full dictionary
            starts (int): Start looking for x columns at this column.

        Returns:
            A single integer, a list of integers or a dictionary of all columns.
        """
        #Do the xcolumn and xerror first. If only one x column then special case to reset startx to get any
        #y columns
        if len(self.setas) < len(self.column_headers):
            self.setas.extend(list("." * (len(self.column_headers) - len(self.setas))))

        if self.setas.count("x")==1:
            xcol=self.setas.index("x")
            maxcol=len(self.setas)+1
            startx=0
            xerr=self.setas.index("d") if "d" in self.setas else None
        elif self.setas.count("x")>1:
            xcol = self.setas[startx:].index("x") + startx
            startx=xcol
            maxcol = self.setas[xcol + 1:].index("x") + xcol + 1
            xerr=self.setas[startx:maxcol].index("d") if "d" in self.setas[startx:maxcol] else None
        else:
            xcol = None
            maxcol = len(self.setas)+1
            startx=0
            xerr=None


        #No longer enforce ordering of yezf - allow them to appear in any order.
        ycol = list()
        yerr = list()
        zcol = list()
        zerr = list()
        ucol = list()
        vcol = list()
        wcol =  list()

        columns=[ycol,yerr,zcol,zerr,ucol,vcol,wcol]
        letters="yezfuvw"
        for col,lett in zip(columns,letters):
            col.extend([None] * self.setas[startx:maxcol].count(lett))
            start=startx
            for i,n in enumerate(col):
                try:
                    col[i]=self.setas[start:maxcol].index(lett)+start
                    start=col[i]+1
                except ValueError:
                    break

        if xcol is None:
            axes = 0
        elif not ycol:
            axes = 1
        elif not zcol:
            axes = 2
        else:
            axes = 3
        if axes == 2 and len(ucol) * len(vcol) > 0:
            axes = 4
        elif axes == 3:
            if len(ucol) * len(vcol) * len(wcol) > 0:
                axes = 6
            elif len(ucol) * len(vcol) > 0:
                axes = 5
        ret = _attribute_store()
        ret.update({
            "xcol": xcol,
            "xerr": xerr,
            "ycol": ycol,
            "yerr": yerr,
            "zcol": zcol,
            "zerr": zerr,
            "ucol": ucol,
            "vcol": vcol,
            "wcol": wcol,
            "axes": axes
        })
        if ret["axes"]==0 and len(self.shape)>=2 and self.shape[1] in self._col_defaults and not no_guess:
            ret.update(self._col_defaults[self.shape[1]])
        for n in list(ret.keys()):
            if ret[n] is None or (isinstance(ret[n],list) and  not ret[n]):
                ret["has_{}".format(n)]=False
            else:
                ret["has_{}".format(n)]=True
        ret["has_uvw"] = ret["has_ucol"] & ret["has_vcol"] & ret["has_wcol"]
        if what == "xcol":
            ret = ret["xcol"]
        elif what in ("ycol", "zcol", "ucol", "vcol", "wcol", "yerr", "zerr"):
            ret = ret[what][0]
        elif what in ("ycols", "zcols", "ucols", "vcols", "wcols", "yerrs", "zerrs"):
            ret = ret[what[0:-1]]
        return ret

class _evaluatable(object):

    """Just a placeholder to indicate that special action needs to be taken to convert a string representation to a valid Python type."""

    pass

class regexpDict(sorteddict):

    """An ordered dictionary that permits looks up by regular expression."""

    allowed_keys=(object,)

    def __lookup__(self,name,multiple=False,exact=False):
        """Lookup name and find a matching key or raise KeyError.

        Parameters:
            name (str, re._pattern_type): The name to be searched for

        Keyword Arguments:
            multiple (bool): Return a singl entry ()default, False) or multiple entries

        Returns:
            Canonical key matching the specified name.

        Raises:
            KeyError: if no key matches name.
        """
        ret=None
        try: #name directly as key
            super(regexpDict,self).__getitem__(name)
            ret=name
        except (KeyError,TypeError): #Fall back to regular expression lookup
            if not exact and not isinstance(name,string_types):
                name=repr(name)
            if exact:
                raise KeyError("{} not a key and exact match requested.".format(name))
            nm=name
            if isinstance(name,string_types):
                try:
                    nm=re.compile(name)
                except Exception:
                    pass
            elif isinstance(name,int_types): #We can do this because we're an OrderedDict!
                ret=list(self.keys())[name]
            else:
                nm=name
            if isinstance(nm,re._pattern_type):
                ret=[n for n in self.keys() if isinstance(n,string_types) and nm.match(n)]
        if ret is None or isiterable(ret) and not ret:
            raise KeyError("{} is not a match to any key.".format(name))
        else:
            if multiple: #sort out returing multiple entries or not
                if not isinstance(ret,list):
                    ret=[ret]
            else:
                if isinstance(ret,list):
                    ret=ret[0]
            return ret

    def __getitem__(self,name):
        """Adds a lookup via regular expression when retrieving items."""
        return super(regexpDict,self).__getitem__(self.__lookup__(name))

    def __setitem__(self,name,value):
        """Overwrites any matching key, or if not found adds a new key."""
        try:
            key=self.__lookup__(name,exact=True)
        except KeyError:
            if not isinstance(name,self.allowed_keys):
                raise KeyError("{} is not a match to any key.".format(name))
            key=name
        super(regexpDict,self).__setitem__(key, value)

    def __delitem__(self,name):
        """Deletes keys that match by regular expression as well as exact matches"""
        super(regexpDict,self).__delitem__(self.__lookup__(name))

    def __contains__(self,name):
        """Returns True if name either is an exact key or matches when interpreted as a regular experssion."""
        try:
            name=self.__lookup__(name)
            return True
        except (KeyError,TypeError):
            return False

    def has_key(self,name):
        """Key is definitely in dictionary as literal"""
        return super(regexpDict,self).__contains__(name)


class typeHintedDict(regexpDict):

    """Extends a :py:class:`blist.sorteddict` to include type hints of what each key contains.

    The CM Physics Group at Leeds makes use of a standard file format that closely matches
    the :py:class:`DataFile` data structure. However, it is convenient for this file format
    to be ASCII text for ease of use with other programs. In order to represent metadata which
    can have arbitary types, the LabVIEW code that generates the data file from our measurements
    adds a type hint string. The Stoner Python code can then make use of this type hinting to
    choose the correct representation for the metadata. The type hinting information is retained
    so that files output from Python will retain type hints to permit them to be loaded into
    strongly typed languages (sch as LabVIEW).

    Attributes:
        _typehints (dict): The backing store for the type hint information
        __regexGetType (re): Used to extract the type hint from a string
        __regexSignedInt (re): matches type hint strings for signed intergers
        __regexUnsignedInt (re): matches the type hint string for unsigned integers
        __regexFloat (re): matches the type hint strings for floats
        __regexBoolean (re): matches the type hint string for a boolean
        __regexStrng (re): matches the type hint string for a string variable
        __regexEvaluatable (re): matches the type hint string for a compoind data type
        __types (dict): mapping of type hinted types to actual Python types
        __tests (dict): mapping of the regex patterns to actual python types

    Notes:
        Rather than subclassing a plain dict, this is a subclass of a :py:class:`blist.sorteddict` which stores the entries in a binary list structure.
        This makes accessing the keys much faster and also ensures that keys are always returned in alphabetical order.
    """

    allowed_keys=string_types
    #Force metadata keys to be strings
    _typehints = sorteddict()

    __regexGetType = re.compile(r'([^\{]*)\{([^\}]*)\}')
    # Match the contents of the inner most{}
    __regexSignedInt = re.compile(r'^I\d+')
    # Matches all signed integers
    __regexUnsignedInt = re.compile(r'^U / d+')
    # Match unsigned integers
    __regexFloat = re.compile(r'^(Extended|Double|Single)\sFloat')
    # Match floating point types
    __regexBoolean = re.compile(r'^Boolean')
    __regexString = re.compile(r'^(String|Path|Enum)')
    __regexEvaluatable = re.compile(r'^(Cluster||\d+D Array|List)')

    __types = {
        'Boolean': bool,
        'I32': int,
        'Double Float': float,
        'Cluster': dict,
        'AnonCluster':tuple,
        'Array': _np_.ndarray,
        'List': list,
        'String': str
    }
    # This is the inverse of the __tests below - this gives
    # the string type for standard Python classes

    __tests = [(__regexSignedInt, int), (__regexUnsignedInt, int), (__regexFloat, float), (__regexBoolean, bool),
               (__regexString, str),  (__regexEvaluatable, _evaluatable())]

    # This is used to work out the correct python class for
    # some string types

    def __init__(self, *args, **kargs):
        """Construct the typeHintedDict.

        Args:
            *args, **kargs: Pass any parameters through to the dict() constructor.


        Calls the dict() constructor, then runs through the keys of the
        created dictionary and either uses the string type embedded in
        the keyname to generate the type hint (and remove the
        embedded string type from the keyname) or determines the likely
        type hint from the value of the dict element.
        """
        super(typeHintedDict, self).__init__(*args, **kargs)
        for key in list(self.keys()):  # Chekc through all the keys and see if they contain
            # type hints. If they do, move them to the
            # _typehint dict
            value = super(typeHintedDict, self).__getitem__(key)
            super(typeHintedDict, self).__delitem__(key)
            self[key] = value  #__Setitem__ has the logic to handle embedded type hints correctly


    @property
    def types(self):
        """Return the dictrionary of value types."""
        return self._typehints

    def findtype(self, value):
        """Determines the correct string type to return for common python classes.

        Args:
            value (any): The data value to determine the type hint for.

        Returns:
            A type hint string

        Note:
            Understands booleans, strings, integers, floats and _np_
            arrays(as arrays), and dictionaries (as clusters).
        """
        typ = "String"
        for t in self.__types:
            if isinstance(value, self.__types[t]):
                if t == "Cluster" or t=="AnonCluster":
                    elements = []
                    if isinstance(value,dict):
                        for k in value:
                            elements.append(self.findtype(value[k]))
                    else:
                        for v in value:
                            elements.append(self.findtype(v))
                    tt = ','
                    tt = tt.join(elements)
                    typ = 'Cluster (' + tt + ')'
                elif t == 'Array':
                    z = _np_.zeros(1, dtype=value.dtype)
                    typ = "{}D Array ({})".format(len(_np_.shape(value)),self.findtype(z[0]))
                else:
                    typ = t
                break
        return typ

    def __mungevalue(self, t, value):
        """Based on a string type t, return value cast to an appropriate python class.

        Args:
            t (string): is a string representing the type
            value (any): is the data value to be munged into the
                        correct class
        Returns:
            Returns the munged data value

        Detail:
            The class has a series of precompiled regular
            expressions that will match type strings, a list of these has been
            constructed with instances of the matching Python classes. These
            are tested in turn and if the type string matches the constructor of
            the associated python class is called with value as its argument.
        """
        ret = None
        for (regexp, valuetype) in self.__tests:
            m = regexp.search(t)
            if m is not None:
                if isinstance(valuetype, _evaluatable):
                    try:
                        array=_np_.array
                        nan=_np_.nan
                        if isinstance(value, string_types): #we've got a string already don't need repr
                            ret = eval(value, globals(), locals())
                        else:
                            ret = eval(repr(value), globals(), locals()) # pylint: disable=eval-used
                    except NameError:
                        ret = str(value)
                    except SyntaxError:
                        ret = ""
                    break
                else:
                    ret = valuetype(value)
                    break
        else:
            ret = str(value)
        return ret

    def string_to_type(self, value):
        """Given a string value try to work out if there is a better python type dor the value.

        First of all the first character is checked to see if it is a [ or { which would
        suggest this is a list of dictionary. If the value looks like a common boolean
        value (i.e. Yes, No, True, Fale, On, Off) then it is assumed to be a boolean value.
        Fianlly it interpretation as an int, float or string is tried.

        Args:
            value (string): string representation of he value
        Returns:
            A python object of the natural type for value
        """
        ret = None
        if not isinstance(value, string_types):
            raise TypeError("Value must be a string not a {}".format(type(value)))
        value = value.strip()
        if value:
            tests = ['list(' + value + ')', 'dict(' + value + ')']
            try:
                i = "[{".index(value[0])
                array=_np_.array
                nan=_np_.nan
                ret = eval(tests[i],  globals(), locals()) # pylint: disable=eval-used
            except (SyntaxError, ValueError):
                if value.lower() in ['true', 'yes', 'on', 'false', 'no', 'off']:
                    ret = value.lower() in ['true', 'yes', 'on']  #Boolean
                else:
                    for trial in [int, float, str]:
                        try:
                            ret = trial(value)
                            break
                        except ValueError:
                            continue
                    else:
                        ret = None
        return ret

    def __deepcopy__(self,memo):
        """Implements a deepcopy method for typeHintedDict to work around something that gives a hang in newer Python 2.7.x"""
        cls = self.__class__
        result = cls()
        memo[id(self)] = result
        for k in self:
            result[k]=copy.deepcopy(self[k])
            result.types[k]=self.types[k]
        return result

    def _get_name_(self, name):
        """Checks a string name for an embedded type hint and strips it out.

        Args:
            name(string): String containing the name with possible type hint embedeed
        Returns:
            (name,typehint) (tuple): A tuple containing just the name of the mateadata and (if found
                the type hint string),
        """
        name = str(name)
        m = self.__regexGetType.search(name)
        if m is not None:
            k = m.group(1)
            t = m.group(2)
            return k, t
        k = name
        t = None
        return k, None

    def __getitem__(self, name):
        """Provides a get item method that checks whether its been given a typehint in the item name and deals with it appropriately.

        Args:
            name (string): metadata key to retrieve

        Returns:
            metadata value
        """
        key=name
        (name, typehint) = self._get_name_(name)
        name=self.__lookup__(name,True)
        value = [super(typeHintedDict, self).__getitem__(nm) for nm in name]
        if typehint is not None:
            value = [self.__mungevalue(typehint, v) for v in value]
        if len(value)==0:  # pylint: disable=len-as-condition
            raise KeyError("{} is not a valid key even when interpreted as a sregular expression!".format(key))
        elif len(value)==1:
            return value[0]
        else:
            return {k:v for k,v in zip(name,value)}

    def __setitem__(self, name, value):
        """Provides a method to set an item in the dict, checking the key for an embedded type hint or inspecting the value as necessary.

        Args:
            name (string): The metadata keyname
            value (any): The value to store in the metadata string

        Note:
            If you provide an embedded type string it is your responsibility
            to make sure that it correctly describes the actual data
            typehintDict does not verify that your data and type string are
            compatible.
        """
        name, typehint = self._get_name_(name)
        if typehint is not None:
            self._typehints[name] = typehint
            if value is None:  # Empty data so reset to string and set empty #RCT changed the test here
                super(typeHintedDict, self).__setitem__(name, "")
                self._typehints[name] = "String"
            else:
                try:
                    super(typeHintedDict, self).__setitem__(name, self.__mungevalue(typehint, value))
                except ValueError:
                    pass # Silently fail
        else:
            self._typehints[name] = self.findtype(value)
            super(typeHintedDict, self).__setitem__(name,  value)

    def __delitem__(self, name):
        """Deletes the specified key.

        Args:
            name (string): The keyname to be deleted
        """
        name = self._get_name_(name)[0]
        name=self.__lookup__(name)

        del (self._typehints[name])
        super(typeHintedDict, self).__delitem__(name)

    def __repr__(self):
        """Create a text representation of the dictionary with type data."""
        ret=["{}:{}:{}".format(repr(key),self.type(key),repr(self[key])) for key in self]
        return "\n".join(ret)

    def copy(self):
        """Provides a copy method that is aware of the type hinting strings.

        This produces a flat dictionary with the type hint embedded in the key name.

        Returns:
            A copy of the current typeHintedDict
        """
        cls=self.__class__
        ret = cls()
        for k in self.keys():
            t = self._typehints[k]
            ret._typehints[k]=t
            super(typeHintedDict,ret).__setitem__(k,copy.deepcopy(self[k]))
        return ret

    def filter(self, name):
        """Filter the dictionary keys by name

        Reduce the metadata dictionary leaving only keys satisfied by name.

        Keyword Arguments:
            name(str or callable):
                either a str to match or a callable function that takes metadata key-value
                as an argument and returns True or False
        """
        rem = []
        for k in self.keys():
            if isinstance(name, string_types):
                if not name in k:
                    rem.append(k)
            elif hasattr(name, '__call__'):
                if not name(k):
                    rem.append(k)
            else:
                raise ValueError('name must be a string or a function')
        for k in rem:
            del(self[k])

    def type(self, key):
        """Returns the typehint for the given k(s).

        This simply looks up the type hinting dictionary for each key it is given.

        Args:
            key (string or sequence of strings): Either a single string key or a iterable type containing
                keys
        Returns:
            The string type hint (or a list of string type hints)
        """
        if isinstance(key, string_types):
            return self._typehints[key]
        else:
            try:
                return [self._typehints[x] for x in key]
            except TypeError:
                return self._typehints[key]

    def export(self, key):
        """Exports a single metadata value to a string representation with type hint.

        In the ASCII based file format, the type hinted metadata is represented
        in the first column of a tab delimited text file as a series of lines
        with format keyname{typhint}=string_value.

        Args:
            key (string): The metadata key to export
        Returns:
            A string of the format : key{type hint} = value
        """
        if isinstance(self[key], string_types): #avoid string within string problems and backslash overdrive
            ret = "{}{{{}}}={}".format(key, self.type(key), self[key])
        else:
            ret = "{}{{{}}}={}".format(key, self.type(key), repr(self[key]))
        return ret

    def export_all(self):
        """Return all the entries in the typeHintedDict as a list of exported lines.

        Returns:
            (list of str): A list of exported strings

        Notes:
            The keys are returned in sorted order as a result of the underlying blist.sorteddict meothd.
        """
        return [self.export(x) for x in self]

    def import_all(self,lines):
        """Reads multiple lines of strings and tries to import keys from them.

        Args:
            lines(list of str): The lines of metadata values to import.
        """
        for line in lines:
            self.import_key(line)

    def import_key(self,line):
        """Import a single key from a string like key{type hint} = value.

        This is the inverse of the :py:meth:`typeHintedDict.export` method.

        Args:
            line(str): The string line to be interpreted as a key-value pair.

        """
        parts=line.split("=")
        k=parts[0]
        v="=".join(parts[1:]) #rejoin any = in the value string
        self[k] = v


class metadataObject(MutableMapping):

    """Provides a base class representing some sort of object that has metadata stored in a :py:class:`Stoner.Core.typeHintedDict` object.

    Attributes:
        metadata (typeHintedDict): of key-value metadata pairs. The dictionary tries to retain information about the type of data so as to aid import and
            export from CM group LabVIEW code.
   """

    def __init__(self, *args, **kargs):
        """Initialises the current metadata attribute."""
        metadata=kargs.pop("metadata",None)
        if metadata is not None:
            self.metadata.update(metadata)
        super(metadataObject,self).__init__()

    @property
    def metadata(self):
        """Read the metadata dictionary."""
        try:
            return self._metadata
        except AttributeError: #Oops no metadata yet
            self._metadata=typeHintedDict()
            return self._metadata

    @metadata.setter
    def metadata(self,value):
        """Update the metadata object with type checking."""
        if not isinstance(value,typeHintedDict) and isiterable(value):
            self._metadata=typeHintedDict(value)
        elif isinstance(value,typeHintedDict):
            self._metadata=value
        else:
            raise TypeError("metadata must be something that can be turned into a dictionary, not a {}".format(type(value)))

    def __getitem__(self,name):
        """Pass through to metadata dictionary."""
        return self.metadata[name]

    def __setitem__(self,name,value):
        """Pass through to metadata dictionary."""
        self.metadata[name]=value

    def __delitem__(self,name):
        """Pass through to metadata dictionary."""
        del self.metadata[name]

    def __len__(self):
        """Pass through to metadata dictionary."""
        return len(self.metadata)

    def __iter__(self):
        """Pass through to metadata dictionary."""
        return self.metadata.__iter__()

    def keys(self):
        """Return the keys of the metadata dictionary."""
        return self.metadata.keys()

    def save(self,path):
        """Stub method for a save function."""
        raise NotImplementedError("Save is not implemented in the base class.")

    def _load(self,filename):
        """Stub method for a load function."""
        raise NotImplementedError("Save is not implemented in the base class.")


class DataArray(_ma_.MaskedArray):

    r"""A sub class of :py:class:`numpy.ma.MaskedArray` with a copy of the setas attribute to allow indexing by name.

    Attributes:
        column_headers (list): of strings of the column names of the data.
        i (array of integers): When read, returns the row  umbers of the data. When written to, sets the
            base row index. The base row index is preserved when a DataArray is indexed.
        x,y,z (1D DataArray): When a column is declared to contain *x*, *y*, or *z* data, then these attributes access
            the corresponding columns. When written to, the attributes overwrite the existing column's data.
        d,e,f (1D DataArray): Where a column is identified as containing uncertainities for *x*, *y* or *z* data, then these
            attributes provide a quick access to them. When written to, the attributes overwrite the existing column's data.
        u,v,w (1D DataArray): Columns may be identieid as containing vectgor field information. These attributes provide quick
            access to them, assuming that they are defined as cartesian co-ordinates. When written to, the attributes
            overwrite the existing column's data.
        p,q,r (1D DataArray): These attributes access calculated columns that convert :math:`(x,y,z)` data or :math:`(u,v,w)`
            into :math:`(\phi,\theta,r)` polar co-ordinates. If on *x* and *y* columns are defined, then 2D polar
            co-ordinates are returned for *q* and *r*.
        setas (list or string): Actually a proxy to a magic class that handles the assignment of columns to different axes and
            also tracks the names of columns (so that columns may be accessed as named items).



    This array type is used to represent numeric data in the Stoner Package - primarily as a 2D
    matrix in :py:class:`Stoner.Core.DataFile` but also when a 1D row is required. In con trast to
    the parent class, DataArray understands that it came from a DataFile which has a setas attribute and column
    assignments. This allows the row to be indexed by column name, and also for quick
    attribute access to work. This makes writing functions to work with a single row of data
    more attractive.
    """

    #============================================================================================================================
    ############################                       Object Construction                        ###############################
    #============================================================================================================================

    def __new__(cls, input_array, *args,**kargs):
        """Create the new instance of the DataArray."""
        # Input array is an already formed ndarray instance
        # We first cast to be our class type
        setas=kargs.pop("setas",_setas())
        if isinstance(input_array,_ma_.MaskedArray):
            default_mask=input_array.mask
        else:
            default_mask=None
        mask=_np_.copy(kargs.pop("mask",default_mask))
        column_headers=kargs.pop("column_headers",[])
        _row=kargs.pop("isrow",False)
        if isinstance(input_array,DataArray):
            i=input_array.i
        else:
            i=0
        obj = _ma_.asarray(input_array,*args,**kargs).view(cls)
        # add the new attribute to the created instance
        setas.shape=obj.shape
        obj._setas = setas
        if mask is not None:
            obj.mask=mask
        else:
            obj.mask=False
        # Finally, we must return the newly created object:
        obj.i=i
        obj.setas._row=_row and len(obj.shape)==1
        #Set shared mask - stops some deprication warnings
        obj.unshare_mask()
        obj.column_headers=column_headers
        return obj

    def __array_finalize__(self, obj):
        """Numpy ndarray magic method."""
        # see InfoArray.__array_finalize__ for comments
        super(DataArray,self).__array_finalize__(obj)
        if obj is None:
            self._setas=_setas()
            self.i=0
            self.mask=False
            self._setas._row=False
            self._setas.shape=(0,)
        else:
            self._setas = getattr(obj, '_setas', _setas())
            if isinstance(obj,DataArray):
                self.i=obj.i
                self.mask=obj.mask
                self._setas._row=getattr(obj._setas,'_row',False)
            else:
                self.i=0
                self.mask=False
                self._setas._row=False
            self._setas.shape=getattr(self,'shape',(0,))

    def __array_wrap__(self, out_arr, context=None):
        """Make sure ufuncs do the right thing with DataArrays"""
        ret=_ma_.MaskedArray.__array_wrap__(self, out_arr, context)
        return ret

    #============================================================================================================================
    ############################                  Property Accessor Functions                     ###############################
    #============================================================================================================================

    @property
    def _(self):
        """Return the DataArray as a normal numpy array for those operations that need this"""
        return _ma_.getdata(self)

    @property
    def isrow(self):
        """Defines whether this is a single row or a column if 1D."""
        return self._setas._row

    @isrow.setter
    def isrow(self,value):
        """Set whether this object is a single row or not."""
        self._setas._row = len(self.shape)==1 and value

    @property
    def r(self):
        r"""Calculate the radius :math:`\rho` co-ordinate if using spherical or polar co-ordinate systems."""
        axes = int(self._setas.cols["axes"])
        m = [lambda d: None, lambda d: None, lambda d: _np_.sqrt(d.x ** 2 + d.y ** 2),
             lambda d: _np_.sqrt(d.x ** 2 + d.y ** 2 + d.z ** 2),
             lambda d: _np_.sqrt(d.x ** 2 + d.y ** 2 + d.z ** 2), lambda d: _np_.sqrt(d.u ** 2 + d.v ** 2),
             lambda d: _np_.sqrt(d.u ** 2 + d.v ** 2 + d.w ** 2)]
        ret = m[axes](self)
        if ret is None:
            raise StonerSetasError("Insufficient axes defined in setas to calculate the r component. need 2 not {}".format(axes))
        else:
            return ret

    @property
    def q(self):
        r"""Calculate the azimuthal :math:`\theta` co-ordinate if using spherical or polar co-ordinates."""
        axes = int(self._setas.cols["axes"])
        m = [lambda d: None, lambda d: None, lambda d: _np_.arctan2(d.x, d.y), lambda d: _np_.arctan2(d.x, d.y),
             lambda d: _np_.arctan2(d.x, d.y), lambda d: _np_.arctan2(d.u, d.v),
             lambda d: _np_.arctan2(d.u, d.v)]
        ret = m[axes](self)
        if ret is None:
            raise StonerSetasError("Insufficient axes defined in setas to calculate the theta component. need 2 not {}".format(axes))
        else:
            return ret

    @property
    def p(self):
        r"""Calculate the inclination :math:`\phi` co-ordinate for spherical co-ordinate systems."""
        axes = int(self._setas.cols["axes"])
        m = [lambda d: None, lambda d: None, lambda d: None, lambda d: _np_.arcsin(d.z),
             lambda d: _np_.arsin(d.z), lambda d: _np_.arcsin(d.w), lambda d: _np_.arcsin(d.w)]
        ret = m[axes](self)
        if ret is None:
            raise StonerSetasError("Insufficient axes defined in setas to calculate the phi component. need 3 not {}".format(axes))
        else:
            return ret

    @property
    def i(self):
        """Return the row indices of the DataArray or sets the base index - the row number of the first row."""
        if not hasattr(self,"_ibase"):
            self._ibase=[]
        if len(self._ibase)==1 and self.isrow:
            ret=min(self._ibase)
        else:
            ret=self._ibase
        return ret

    @i.setter
    def i(self,value):
        if self.ndim==0:
            pass
        elif self.ndim==1 and self.isrow:
            if isiterable(value) and value:
                self._ibase=_np_.array([min(value)])
            else:
                self._ibase=_np_.array([value])
        elif self.ndim>=1:
            r=self.shape[0]
            if isiterable(value) and len(value)==r: #Iterable and the correct length - assing straight
                self._ibase=_np_.array(value)
            elif isiterable(value): # Iterable but not the correct length - count from min of value
                self._ibase=_np_.arange(min(value),min(value)+r)
            else: # No iterable
                self._ibase=_np_.arange(value,value+r)

    @property
    def column_headers(self):
        """Pass through to the setas attribute."""
        return self._setas.column_headers

    @column_headers.setter
    def column_headers(self, value):
        """Write the column_headers attribute (delagated to the setas object)."""
        self._setas.column_headers = value

    @property
    def setas(self):
        """Returns an object for setting column assignments."""
        if "_setas" not in self.__dict__:
            self._setas=_setas()
        if self._setas.shape!=self.shape:
            self._setas.shape=self.shape
        return self._setas

    @setas.setter
    def setas(self,value):
        if isinstance(value,_setas):
            value=value.clone
        setas=self.setas
        setas(value)

    #============================================================================================================================
    ############################              Speical Methods                ####################################################
    #============================================================================================================================

    def __getattr__(self,name):
        """Get a column using the setas attribute."""
        #Overrides __getattr__ to allow access as row.x etc.
        col_check = {
            "x": "xcol",
            "d": "xerr",
            "y": "ycol",
            "e": "yerr",
            "z": "zcol",
            "f": "zerr",
            "u": "ucol",
            "v": "vcol",
            "w": "wcol",
        }
        if name in self.setas.cols:
            return self.setas.__getattr__(name)
        if name not in col_check:
            return super(DataArray,self).__getattribute__(name)
        indexer=[slice(0,dim,1) for ix,dim in enumerate(self.shape)]
        col = col_check[name]
        if col.startswith("x"):
            if self._setas.cols[col] is not None:
                indexer[-1]=self._setas.cols[col]
                ret = self[tuple(indexer)]
            else:
                ret = None
        else:
            if isiterable(self._setas.cols[col]) and len(self._setas.cols[col])>0:
                indexer[-1]=self._setas.cols[col][0]
            elif isiterable(self._setas.cols[col]):
                indexer[-1]=self._setas.cols[col]
            else:
                return None
            ret = self[tuple(indexer)]
        if ret is None:
            raise StonerSetasError("Tried accessing a {} column, but setas is not defined.".format(name))
        else:
            return ret

    def __getitem__(self,ix):
        """Indexing function for DataArray.

        Args:
            ix (various): Index to find.

        Returns:
            An indexed part of the DataArray object with extra attributes.

        Notes:
            This tries to support all of the indexing operations of a regular numpy array,
            plus the special operations where one columns are named.

        Warning:
            Teh code almost certainly makes some assumptiuons that DataArray is one or 2D and
            may blow up with 3D arrays ! On the other hand it has a special case exception for where
            you give a string as the first index element and assumes that you've forgotten that we're
            row major and tries to do the right thing.
        """
        #Is this goign to be a single row ?
        single_row=isinstance(ix,int_types) or (isinstance(ix,tuple) and len(ix)>0 and isinstance(ix[0],int_types))
        #If the index is a single string type, then build a column accessing index
        if isinstance(ix,string_types):
            if self.ndim>1:
                ix=(slice(None,None,None),self._setas.find_col(ix))
            else:
                ix=(self._setas.find_col(ix),)
        if isinstance(ix,(int_types,slice)):
            ix=(ix,)
        elif isinstance(ix,tuple) and ix and isinstance(ix[-1],string_types): # index still has a string type in it
            ix=list(ix)
            ix[-1]=self._setas.find_col(ix[-1])
            ix=tuple(ix)
        elif isinstance(ix,tuple) and ix and isiterable(ix[-1]): # indexing with a list of columns
            ix=list(ix)
            if all_type(ix[-1],bool):
                ix[-1]=_np_.arange(len(ix[-1]))[ix[-1]]
            ix[-1]=[self._setas.find_col(c) for c in ix[-1]]
            ix=tuple(ix)
        elif isinstance(ix,tuple) and ix and isinstance(ix[0],string_types): # oops! backwards indexing
            c=ix[0]
            ix=list(ix[1:])
            ix.append(self._setas.find_col(c))
            ix=tuple(ix)
            # Now can index with our constructed multidimesnional indexer
        ret=super(DataArray,self).__getitem__(ix)
        if ret.ndim==0 or isinstance(ret,_np_.ndarray) and ret.size==1:
            return ret.dtype.type(ret)
        elif not isinstance(ret,_np_.ndarray): #bugout for scalar resturns
            return ret
        elif ret.ndim>=2: # Potentially 2D array here
            if ix[-1] is None: # Special case for increasing an array dimension
                if self.ndim==1: # Going from 1 D to 2D
                    ret.setas=self.setas.clone
                    ret.i=self.i
                    ret.name=getattr(self,"name","Column")
                return ret
            else: # A regular 2D array
                ret.isrow=single_row
                ret.setas=self.setas.clone
                ret.column_headers=copy.copy(self.column_headers)
                if len(ix)>0 and isiterable(ix[-1]):  # pylint: disable=len-as-condition
                    ret.column_headers=list(_np_.array(ret.column_headers)[ix[-1]])
                # Sort out whether we need an array of row labels
                if isinstance(self.i,_np_.ndarray) and len(ix)>0:  # pylint: disable=len-as-condition
                    if isiterable(ix[0]) or isinstance(ix[0],int_types):
                        ret.i=self.i[ix[0]]
                    else:
                        ret.i=0
                else:
                    ret.i=self.i
        elif ret.ndim==1: # Potentially a single row or single column
            ret.isrow=single_row
            if len(ix)==len(self.setas):
                tmp=_np_.array(self.setas)[ix[-1]]
                ret.setas(tmp)
                tmpcol=_np_.array(self.column_headers)[ix[-1]]
                ret.column_headers=tmpcol
            else:
                ret.setas=self.setas.clone
                ret.column_headers=copy.copy(self.column_headers)
            # Sort out whether we need an array of row labels
            if single_row and isinstance(self.i,_np_.ndarray):
                ret.i=self.i[ix[0]]
            else: #This is a single element?
                ret.i=self.i
            if not single_row:
                ret.name=self.column_headers
        return ret

    def __setitem__(self,ix,val):
        """Override __setitem__ to handle string indexing."""
        if isinstance(ix,string_types):
            ix=self._setas.find_col(ix)
        elif isinstance(ix,tuple) and isinstance(ix[-1],string_types):
            ix=list(ix)
            ix[-1]=self._setas.find_col(ix[-1])
            ix=tuple(ix)
        elif isinstance(ix,tuple) and isinstance(ix[0],string_types):
            c=ix[0]
            ix=list(ix[1:])
            ix.append(self._setas.find_col(c))
            ix=tuple(ix)

        if self.sharedmask: #We do not want to share a mask when we're about to change soimething here...
            self.unshare_mask()

        super(DataArray,self).__setitem__(ix,val)

    #============================================================================================================================
    ############################              Private Methods                ####################################################
    #============================================================================================================================

    def _col_args(self,scalar=True,xcol=None,ycol=None,zcol=None,ucol=None,vcol=None,wcol=None,xerr=None,yerr=None,zerr=None,**kargs):
        """Utility method that creates an object which has keys  based either on arguments or setas attribute."""
        cols={"xcol":xcol,"ycol":ycol,"zcol":zcol,"ucol":ucol,"vcol":vcol,"wcol":wcol,"xerr":xerr,"yerr":yerr,"zerr":zerr}
        no_guess=True
        for i in cols.values():
            if not i is None: #User specification wins out
                break
        else: #User didn't set any values, setas will win
            no_guess=False
        ret=_attribute_store(self.setas._get_cols(no_guess=no_guess))
        for c in list(cols.keys()):
            if isNone(cols[c]): # Not defined, fallback on setas
                del cols[c]
                continue
            elif isinstance(cols[c],bool) and not cols[c]: #False, delete column altogether
                del cols[c]
                if c in ret:
                    del ret[c]
                continue
            elif c in ret and isinstance(ret[c],list):
                if isinstance(cols[c],_np_.ndarray) and cols[c].size==len(self):
                    continue
            cols[c]=self.setas.find_col(cols[c])
        ret.update(cols)
        if scalar:
            for c in ret:
                if isinstance(ret[c],list):
                    if ret[c]:
                        ret[c]=ret[c][0]
                    else:
                        ret[c]=None
        elif isinstance(scalar,bool) and not scalar:
            for c in ret:
                if c.startswith("x") or c.startswith("has_"):
                    continue
                if not isiterable(ret[c]) and ret[c] is not None:
                    ret[c]=list([ret[c]])
                elif ret[c] is None:
                    ret[c]=[]
        return ret


    #============================================================================================================================
    ############################              Public Methods                ####################################################
    #============================================================================================================================

    def keys(self):
        """Return a list of column headers."""
        return self._setas.column_headers

    def swap_column(self, *swp,**kargs):
        """Swaps pairs of columns in the data.

        Useful for reordering data for idiot programs that expect columns in a fixed order.

        Args:
            swp  (tuple of list of tuples of two elements): Each
                element will be iused as a column index (using the normal rules
                for matching columns).  The two elements represent the two
                columns that are to be swapped.
            headers_too (bool): Indicates the column headers
                are swapped as well

        Returns:
            self: A copy of the modified :py:class:`DataFile` objects

        Note:
            If swp is a list, then the function is called recursively on each
            element of the list. Thus in principle the @swp could contain
            lists of lists of tuples
        """
        headers_too=kargs.pop("headers_too",True)
        setas_too=kargs.pop("setas_too",True)

        if len(swp)==1:
            swp=swp[0]
        if isinstance(swp, list) and all_type(swp,tuple) and all_size(swp,2):
            for item in swp:
                self.swap_column(item, headers_too=headers_too)
        elif isinstance(swp, tuple):
            col1 = self._setas.find_col(swp[0])
            col2 = self._setas.find_col(swp[1])
            self[:, [col1, col2]] = self[:, [col2, col1]]
            if headers_too:
                self._setas.column_headers[col1], self._setas.column_headers[col2] = self._setas.column_headers[col2], self._setas.column_headers[col1]
            if setas_too:
                self._setas[col1], self._setas[col2] = self._setas[col2], self._setas[col1]
        else:
            raise TypeError("Swap parameter must be either a tuple or a \
            list of tuples")

class DataFile(metadataObject):

    """:py:class:`Stoner.Core.DataFile` is the base class object that represents a matrix of data, associated metadata and column headers.

    Attributes:
        column_headers (list): of strings of the column names of the data.
        data (2D numpy masked array): The attribute that stores the nuermical data for each DataFile. This is a :py:class:`DataArray` instance - which
            is itself a subclass of :py:class:`numpy.ma.MaskedArray`.
        title (string): The title of the measurement.
        filename (string): The current filename of the data if loaded from or
                           already saved to disc. This is the default filename used by the :py:meth:`Stoner.Core.DataFile.load`
                           and :py:meth:`Stoner.Core.DataFile.save`.
        header (string): A readonly property that returns a pretty formatted string giving the header of tabular representation.
        mask (array of booleans): Returns the current mask applied to the numerical data equivalent to self.data.mask.
        mime_type (list of str): The possible mime-types of data files represented by each matching filename pattern in :py:attr:`Datafile.pattern`.
        patterns (list): A list of filename extenion glob patterns that matrches the expected filename patterns for a DataFile (*.txt and *.dat")
        priority (int): Used to indicathe order in which subclasses of :py:class:`DataFile` are tried when loading data. A higher number means a lower
                            priority (!)
        setas (list or string): Defines certain columns to contain X, Y, Z or errors in X,Y,Z data.
        shape (tuple of integers): Returns the shape of the data (rows,columns) - equivalent to self.data.shape.
        records (numpy record array): Returns the data in the form of a list of yuples where each tuple maps to the columsn names.
        clone (DataFile): Creates a deep copy of the :py:class`DataFile` object.
        dict_records (array of dictionaries): View the data as an array or dictionaries where each dictionary represnets one
            row with keys dervied from column headers.
        dims (int): When data columns are set as x,y,z etc. returns the number of dimensions implied in the data set
        dtype (numpoy dtype): Returns the datatype stored in the :py:attr:`DataFile.data` attribute.
        T (:py:class:`DataArray`): Transposed version of the data.
        subclasses (list): Returns a list of all the subclasses of DataFile currently in memory, sorted by
                           their py:attr:`Stoner.Core.DataFile.priority`. Each entry in the list consists of the
                           string name of the subclass and the class object.
        xcol (int): If a column has been designated as containing *x* values, this will return the index of that column
        xerr (int): Similarly to :py:attr:`DataFile.xcol` but for the x-error value column.
        ycol (list of int): Similarly to :py:attr:`DataFile.xcol` but for the y value columns.
        yerr (list of int): Similarly to :py:attr:`DataFile.xcol` but for the y error value columns.
        zcol (list of int): Similarly to :py:attr:`DataFile.xcol` but for the z value columns.
        zerr (list of int): Similarly to :py:attr:`DataFile.xcol` but for the z error value columns.
        ucol (list of int): Similarly to :py:attr:`DataFile.xcol` but for the u (x-axis direction cosine) columns.
        vcol (list of int): Similarly to :py:attr:`DataFile.xcol` but for the v (y-axis direction cosine) columns.
        wcol (list of int): Similarly to :py:attr:`DataFile.xcol` but for the w (z-axis direction cosine) columns.
    """

    #: priority (int): is the load order for the class, smaller numbers are tried before larger numbers.
    #   .. note::
    #
    #      Subclasses with priority<=32 should make some positive identification that they have the right
    #      file type before attempting to read data.
    priority=32

    #: pattern (list of str): A list of file extensions that might contain this type of file. Used to construct
    # the file load/save dialog boxes.
    _patterns=["*.txt","*.tdi"] # Recognised filename patterns

    #mimetypes we match
    mime_type=["text/plain"]

    _conv_string = _np_.vectorize(str)
    _conv_float = _np_.vectorize(float)

    #============================================================================================================================
    ############################                       Object Construction                        ###############################
    #============================================================================================================================

    def __new__(cls, *args,**kargs):
        """Do some init stuff before the mixins kick in."""
        self=metadataObject.__new__(cls)
        self.debug = kargs.pop("debug",False)
        self._masks = [False]
        self._filename = None
        self._public_attrs_real={}
        super(DataFile,self).__setattr__("_data",DataArray([]))
        self.column_headers = list()
        self._baseclass = DataFile
        return self


    def __init__(self, *args, **kargs):
        """Constructor method for :py:class:`DataFile`.

        various forms are recognised

        .. py:function:: DataFile('filename',<optional filetype>,<args>)
            :noindex:

            Creates the new DataFile object and then executes the :py:class:`DataFile`.load
            method to load data from the given *filename*.

        .. py:function:: DataFile(array)
            :noindex:

            Creates a new DataFile object and assigns the *array* to the
            :py:attr:`DataFile.data`  attribute.

        .. py:function:: DataFile(dictionary)
            :noindex:

            Creates the new DataFile object. If the dictionary keys are all strigns and the values are all
            numpy D arrays of equal length, then assumes the dictionary represents columns of data and the keys
            are the column titles, otherwise initialises the metadata with :parameter: dictionary.

        .. py:function:: DataFile(array,dictionary)
            :noindex:

            Creates the new DataFile object and does the combination of the
            previous two forms.


        .. py:function:: DataFile(DataFile)
            :noindex:

            Creates the new DataFile object and initialises all data from the
            existing :py:class:`DataFile` instance. This on the face of it does the same as
            the assignment operator, but is more useful when one or other of the
            DataFile objects is an instance of a sub - class of DataFile

        Args:
            args (positional arguments): Variable number of arguments that match one of the
                definitions above
            kargs (keyword Arguments): All keyword arguments that match public attributes are
                used to set those public attributes.
        """
        # init instance attributes
        super(DataFile,self).__init__(*args,**kargs) # initialise self.metadata)
        self._public_attrs={
            "data": _np_.ndarray,
            "column_headers": list,
            "setas": (string_types, list),
            "metadata": typeHintedDict,
            "debug": bool,
            "filename": string_types,
            "mask": (_np_.ndarray, bool),
        }
        self._repr_limits=(256,6)
        i = len(args) if len(args) < 3 else 3
        handler = [None, self._init_single, self._init_double, self._init_many][i]
        self.mask = False
        self.data._setas._get_cols()
        if handler is not None:
            handler(*args, **kargs)
        self.metadata["Stoner.class"] = self.__class__.__name__
        if kargs:  # set public attributes from keywords
            to_go=[]
            for k in kargs:
                if k in self._public_attrs:
                    if isinstance(kargs[k], self._public_attrs[k]):
                        self.__setattr__(k, kargs[k])
                    else:
                        self._raise_type_error(k)
                        to_go.append(k)
                else:
                    raise AttributeError("{} is not a recognised attribute ({})".format(k,list(self._public_attrs.keys())))
            for k in to_go:
                del kargs[k]
        if self.debug: print("Done DataFile init")

    def _init_single(self, *args, **kargs):
        """Handles constructor with 1 arguement - called from __init__."""
        arg = args[0]
        if (isinstance(arg, string_types) or (isinstance(arg, bool) and not arg)):
            # Filename- load datafile
            self.load(filename=arg, **kargs)
        elif isinstance(arg, _np_.ndarray):
            # numpy.array - set data
            self.data = DataArray(_np_.atleast_2d(arg),setas=self.data._setas)
            self.column_headers = ['Column_{}'.format(x) for x in range(_np_.shape(args[0])[1])]
        elif isinstance(arg, dict):  # Dictionary - use as data or metadata
            if all_type(arg.keys(),string_types) and all_type(arg.values(),_np_.ndarray) and _np_.all(
                [len(arg[k].shape)==1 and _np_.all(len(arg[k])==len(arg.values()[0])) for k in arg]):
                self.data=_np_.column_stack(tuple(arg.values()))
                self.column_headers=list(arg.keys())
            else:
                self.metadata = arg.copy()
        elif isinstance(arg, DataFile):
            for a in arg.__dict__:
                if not callable(a) and a!="_baseclass":
                    super(DataFile, self).__setattr__(a, copy.copy(arg.__getattribute__(a)))
            self.metadata = arg.metadata.copy()
            self.data = DataArray(arg.data,setas=arg.setas.clone)
            self.data.setas = arg.setas.clone
        elif "<class 'Stoner.Image.core.ImageFile'>" in [str(x) for x in arg.__class__.__mro__]: #Crazy hack to avoid importing a circular ref!
            x=arg.get("x_vector",_np_.arange(arg.shape[0]))
            y=arg.get("y_vector",_np_.arange(arg.shape[1]))
            x,y=_np_.meshgrid(x,y)
            z=arg.image

            self.data=_np_.column_stack((x.ravel(),y.ravel(),z.ravel()))
            self.metadata=copy.deepcopy(arg.metadata)
            self.column_headers=["X","Y","Image Intensity"]
            self.setas="xyz"
        elif isiterable(arg) and all_type(arg,string_types):
            self.column_headers=list(arg)
        elif isiterable(arg) and all_type(arg,_np_.ndarray):
            self._init_many(*arg,**kargs)
        else:
            raise SyntaxError("No constructor for {}".format(type(arg)))
        self.data._setas.cols.update(self.setas._get_cols())

    def _init_double(self, *args, **kargs):
        """Two argument constructors handled here. Called form __init__"""
        (arg0, arg1) = args
        if isinstance(arg1,dict) or (isiterable(arg1) and all_type(arg1,string_types)):
            self._init_single(arg0,**kargs)
            self._init_single(arg1,**kargs)
        elif isinstance(arg0,_np_.ndarray) and isinstance(arg1,_np_.ndarray) and len(arg0.shape)==1 and len(arg1.shape)==1:
            self._init_many(*args,**kargs)

    def _init_many(self, *args, **kargs):
        """Handles more than two arguments to the constructor - called from init."""
        for a in args:
            if not (isinstance(a,_np_.ndarray) and len(a.shape)==1):
                self.load(*args, **kargs)
                break
        else:
            self.data=_np_.column_stack(args)

    #============================================================================================================================
    ############################                  Property Accessor Functions                     ###############################
    #============================================================================================================================

    @property
    def _public_attrs(self):
        """Return a dictionary of attributes setable by keyword argument with thier types."""
        return self._public_attrs_real

    @_public_attrs.setter
    def _public_attrs(self,value):
        """Privaye property to update the list of public attributes."""
        self._public_attrs_real.update(dict(value))

    @property
    def _repr_html_(self):
        if get_option("short_repr") or get_option("short_data_repr"):
            raise AttributeError("Rich html output su[[ressed")
        else:
            return self._repr_html_private

    @property
    def basename(self):
        """Returns the basename of the current filename."""
        return os.path.basename(self.filename)

    @property
    def clone(self):
        """Gets a deep copy of the current DataFile."""
        c = self.__class__()
        if self.debug: print("Cloning in DataFile")
        return copy_into(self,c)

    @property
    def column_headers(self):
        """Pass through to the setas attribute."""
        return self.data._setas.column_headers

    @column_headers.setter
    def column_headers(self, value):
        """Write the column_headers attribute (delagated to the setas object)."""
        self.data._setas.column_headers = value

    @property
    def data(self):
        """Property Accessors for the main numerical data."""
        return _np_.atleast_2d(self._data)

    @data.setter
    def data(self, value):
        """Set the data attribute, but force it through numpy.ma.masked_array first."""
        nv=value
        if not nv.shape: #nv is a scalar - make it a 2D array
            nv = _ma_.atleast_2d(nv)
        elif len(nv.shape) == 1: #nv is a vector - make it a 2D array
            nv = _ma_.atleast_2d(nv).T
        elif len(nv.shape) > 2: #nv has more than 2D - raise an error # TODO 0.9? Support 3D arrays in DataFile?
            raise ValueError("DataFile.data should be no more than 2 dimensional not shape {}", format(nv.shape))
        if not isinstance(nv,DataArray): # nv isn't a DataArray, so preserve setas (does this preserve column_headers too?)
            nv = DataArray(nv)
            nv._setas=getattr(self,"_data")._setas.clone
        elif nv.shape[1]==self.shape[1]: # nv is a DataArray with the same number of columns - preserve column_headers and setas
            ch=getattr(self,"_data").column_headers
            nv._setas=getattr(self,"_data")._setas.clone
            nv.column_headers=ch
        nv._setas.shape=nv.shape
        self._data=nv

    @property
    def dict_records(self):
        """Return the data as a dictionary of single columns with column headers for the keys."""
        return _np_.array([dict(zip(self.column_headers, r)) for r in self.rows()])

    @property
    def dims(self):
        """An alias for self.data.axes"""
        return self.data.axes

    @property
    def dtype(self):
        """Return the _np_ dtype attribute of the data"""
        return self.data.dtype

    @property
    def filename(self):
        """Return DataFile filename, or make one up."""
        if self._filename is None:
            self.filename="Untitled"
        return self._filename

    @filename.setter
    def filename(self,filename):
        """Store the DataFile filename."""
        self._filename=filename

    @property
    def header(self):
        """Make a pretty header string that looks like the tabular representation."""
        if tabulate is None:
            raise ImportError("No tabulate.")
        fmt="rst"
        lb="<br/>" if fmt=="html" else "\n"
        rows,cols=self._repr_limits
        r,c=self.shape
        interesting,col_assignments,cols=self._interesting_cols(cols)
        c=min(c,cols)
        c_w=max([len(self.column_headers[x]) for x in interesting if x>-1])
        wrapper=TextWrapper(subsequent_indent="\t",width=max(20,max(20,(80-c_w*c))))
        if r>rows:
            shorten=[True,False]
            r=rows+rows%2
        else:
            shorten=[False,False]

        shorten[1]=c>cols
        r=max(len(self.metadata),r)

        outp=_np_.zeros((1,c+1),dtype=object)
        outp[:,:]="..."
        ch=[self.column_headers[ix] if ix>=0 else "...." for ix in interesting]

        for ix,(h,i) in enumerate(zip(ch,col_assignments)):
            ch[ix]="{}{}{}".format(h,lb,i)
            if self.debug: print(len(spaces1),len(spaces2))
        outp[0,1:]=ch
        #outp[1,1:]=col_assignments
        outp[0,0]="TDI Format 1.5{}index".format(lb)
        ret=tabulate(outp,tablefmt=fmt,numalign="decimal",stralign="center")
        return ret

    @property
    def mask(self):
        """Returns the mask of the data array."""
        self.data.mask = _ma_.getmaskarray(self.data)
        return self.data.mask

    @mask.setter
    def mask(self, value):
        """Set the mask attribute by setting the data.mask."""
        if callable(value):
            self._set_mask(value, invert=False)
        else:
            self.data.mask = value

    @classproperty
    def patterns(self):
        """Return the possible filename patterns for use in dialog boxes."""
        patterns=self._patterns
        for cls in self.subclasses:  # pylint: disable=not-an-iterable
            klass=self.subclasses[cls] # pylint: disable=unsubscriptable-object
            if klass is DataFile or "patterns" not in klass.__dict__:
                continue
            patterns.extend([p for p in klass.patterns if p not in patterns])
        return patterns

    @property
    def records(self):
        """Returns the data as a _np_ structured data array. If columns names are duplicated then they are made unique."""
        ch = copy.copy(self.column_headers)  # renoved duplicated column headers for structured record
        ch_bak=copy.copy(ch)
        setas=self.setas.clone #We'll need these later !
        f = self.data.flags
        if not f["C_CONTIGUOUS"] and not f["F_CONTIGUOUS"]:  # We need our data to be contiguous before we try a records view
            self.data = self.data.copy()
        for i,header in enumerate(ch):
            j = 0
            while ch[i] in ch[i + 1:] or ch[i] in ch[0:i]:
                j = j + 1
                ch[i] = "{}_{}".format(header, j)
        dtype = [(str(x), self.dtype) for x in ch]
        self.setas=setas
        self.column_headers=ch_bak
        try:
            return self.data.view(dtype=dtype).reshape(len(self))
        except TypeError as e:
            raise TypeError("Failed to get record view. Dtype was {}".format(dtype))

    @property
    def shape(self):
        """Pass through the numpy shape attribute of the data."""
        return self.data.shape

    @property
    def setas(self):
        """Get the list of column assignments."""
        return self._data._setas

    @setas.setter
    def setas(self, value):
        """Sets a new setas assignment by calling the setas object."""
        self._data._setas(value)

    @classproperty
    def subclasses(self):
        """Return a list of all in memory subclasses of this DataFile."""
        subclasses = {x: (x.priority,x.__name__) for x in itersubclasses(DataFile)}
        ret = OrderedDict()
        ret["DataFile"] = DataFile
        for cls, _ in sorted(list(subclasses.items()), key=lambda c: c[1]):
            ret[cls.__name__] = cls
        return ret

    @property
    def T(self):
        """Gets the current data transposed."""
        return self.data.T

    @T.setter
    def T(self, value):
        """Write directly to the transposed data."""
        self.data.T = value


    #============================================================================================================================
    #####################################                   Operator Functions                         ##########################
    #============================================================================================================================


    def __add__(self, other):
        """Implements a + operator to concatenate rows of data.

        Args:
            other (numpy arra `Stoner.Core.DataFile` or a dictionary or a list):

        Note:
            * If other is a dictionary then the keys of the dictionary are passed to
            :py:meth:`find_col` to see if they match a column, in which case the
            corresponding value will be used for theat column in the new row.
            Columns which do not have a matching key will be set to NaN. If other has keys
            that are not found as columns in self, additional columns are added.
            * If other is a list, then the add method is called recursively for each element
            of the list.
            * Returns: A Datafile object with the rows of @a other appended
            to the rows of the current object.
            * If other is a 1D numopy array with the same number of
            elements as their are columns in @a self.data then the numpy
            array is treated as a new row of data If @a ither is a 2D numpy
            array then it is appended if it has the same number of
            columns and @a self.data.
        """
        newdata = self.clone
        return self.__add_core__(other, newdata)

    def __iadd__(self, other):
        """Implements a += operator to concatenate rows of data inplace.

        Args:
            other (numpy arra `Stoner.Core.DataFile` or a dictionary or a list):

        Note:
            * If other is a dictionary then the keys of the dictionary are passed to
            :py:meth:`find_col` to see if they match a column, in which case the
            corresponding value will be used for theat column in the new row.
            Columns which do not have a matching key will be set to NaN. If other has keys
            that are not found as columns in self, additional columns are added.
            * If other is a list, then the add method is called recursively for each element
            of the list.
            * Returns: A Datafile object with the rows of @a other appended
            to the rows of the current object.
            * If other is a 1D numopy array with the same number of
            elements as their are columns in @a self.data then the numpy
            array is treated as a new row of data If @a ither is a 2D numpy
            array then it is appended if it has the same number of
            columns and @a self.data.
        """
        newdata = self
        return self.__add_core__(other, newdata)

    def __add_core__(self, other, newdata):
        """Implements the core work of adding other to self and modifying newdata.

        Args:
            other (DataFile,array,list): The data to be added
            newdata(DataFile): The instance to be modified

        Returns:
            newdata: A modified newdata
        """
        if isinstance(other, _np_.ndarray):
            if len(self) == 0:  # pylint: disable=len-as-condition
                ch=getattr(other,"column_headers",[])
                setas=getattr(other,"setas","")
                t = _np_.atleast_2d(other)
                c = t.shape[1]
                if len(self.column_headers) < c:
                    newdata.column_headers.extend(["Column_{}".format(x) for x in range(c - len(self.column_headers))])
                newdata.data = t
                newdata.setas=setas
                newdata.column_headers=ch
                ret = newdata
            elif len(_np_.shape(other)) == 1:
                # 1D array, so assume a single row of data
                if _np_.shape(other)[0] == _np_.shape(self.data)[1]:
                    newdata.data = _np_.append(self.data, _np_.atleast_2d(other), 0)
                    ret = newdata
                else:
                    ret = NotImplemented
            elif len(_np_.shape(other)) == 2 and _np_.shape(other)[1] == _np_.shape(self.data)[1]:
                # DataFile + array with correct number of columns
                newdata.data = _np_.append(self.data, other, 0)
                ret = newdata
            else:
                ret = NotImplemented
        elif isinstance(other, DataFile):  # Appending another DataFile
            new_data = _np_.ones((other.shape[0], self.shape[1])) * _np_.nan
            for i in range(self.shape[1]):
                column = self.column_headers[i]
                try:
                    new_data[:, i] = other.column(column)
                except KeyError:
                    pass
            newdata.metadata = copy.copy(self.metadata)
            newdata.data = _np_.append(self.data, new_data, axis=0)
            ret = newdata
        elif isinstance(other, list):
            for o in other:
                newdata = newdata + o
            ret = newdata
        else:
            ret = NotImplemented
        ret._data._setas.shape=ret.shape
        for attr in self.__dict__:
            if attr not in ("setas","metadata", "data", "column_headers", "mask") and not attr.startswith("_"):
                ret.__dict__[attr] = self.__dict__[attr]
        return ret

    def __and__(self, other):
        """Implements the & operator to concatenate columns of data in a :py:class:`DataFile` object.

        Args:
            other  (numpy array or :py:class:`DataFile`): Data to be added to this DataFile instance

        Returns:
            newdata: A :py:class:`DataFile` object with the columns of other con
        catenated as new columns at the end of the self object.

        Note:
            Whether other is a numopy array of :py:class:`DataFile`, it must
            have the same or fewer rows than the self object.
            The size of @a other is increased with zeros for the extra rows.
            If other is a 1D numpy array it is treated as a column vector.
            The new columns are given blank column headers, but the
            length of the :py:meth:`column_headers` is
            increased to match the actual number of columns.
        """
        #Prep the final DataFile
        newdata = self.clone
        return self.__and_core__(other, newdata)

    def __iand__(self, other):
        """Implements the &= operator to concatenate columns of data in a :py:class:`DataFile` object.

        Args:
            other  (numpy array or :py:class:`DataFile`): Data to be added to this DataFile instance

        Returns:
            self: A :py:class:`DataFile` object with the columns of other con
        catenated as new columns at the end of the self object.

        Note:
            Whether other is a numopy array of :py:class:`DataFile`, it must
            have the same or fewer rows than the self object.
            The size of @a other is increased with zeros for the extra rows.
            If other is a 1D numpy array it is treated as a column vector.
            The new columns are given blank column headers, but the
            length of the :py:meth:`column_headers` is
            increased to match the actual number of columns.
        """
        newdata = self
        return self.__and_core__(other, newdata)

    def __and_core__(self, other, newdata):
        """Implements the core of the & operator, returning data in newdata

        Args:
            other (array,DataFile): Data whose columns are to be added
            newdata (DataFile): instance of DataFile to be modified

        Returns:
            newdata: The modified DataFile (may be self or a clone of self depending
            on the operator's inplaceness)
        """
        if len(newdata.data.shape) < 2:
            newdata.data = _np_.atleast_2d(newdata.data)

        #Get other to be a numpy masked array of data
        #Get other_headers to be a suitable length list of strings
        if isinstance(other, DataFile):
            newdata.metadata.update(other.metadata)
            other_headers=other.column_headers
            other = copy.copy(other.data)
        elif isinstance(other,DataArray):
            other=copy.copy(other)
            if len(other.shape) < 2:  # 1D array, make it 2D column
                other = _np_.atleast_2d(other)
                other = other.T
            other_headers=["Column {}".format(i + newdata.shape[1])
                                           for i in range(other.shape[1])]
        elif isinstance(other, _np_.ndarray):
            other = DataArray(copy.copy(other))
            if len(other.shape) < 2:  # 1D array, make it 2D column
                other = _np_.atleast_2d(other)
                other = other.T
            other_headers=["Column {}".format(i + newdata.shape[1])
                                           for i in range(other.shape[1])]
        else:
            return NotImplemented

        newdata_headers=newdata.column_headers+other_headers

        # Workout whether to extend rows on one side or the other
        if _np_.product(newdata.data.shape) == 0:  #Special case no data yet
            newdata.data = other
        elif newdata.data.shape[0] == other.shape[0]:
            newdata.data = _np_.append(newdata.data, other, 1)
        elif newdata.data.shape[0] < other.shape[0]:  #Need to extend self.data
            extra_rows = other.shape[0] - self.data.shape[0]
            newdata.data = _np_.append(self.data, _np_.zeros((extra_rows, self.data.shape[1])), 0)
            new_mask = newdata.mask
            new_mask[-extra_rows:,:] = True
            newdata.data = _np_.append(newdata.data, other, 1)
            other_mask = _ma_.getmaskarray(other)
            new_mask = _np_.append(new_mask, other_mask, 1)
            newdata.mask = new_mask
        elif other.shape[0] < newdata.data.shape[0]:
            # too few rows we can extend with zeros
            extra_rows = self.data.shape[0] - other.shape[0]
            other = _np_.append(other, _np_.zeros((extra_rows, other.shape[1])), 0)
            other_mask = _ma_.getmaskarray(other)
            other_mask[-extra_rows:,:] = True
            new_mask = newdata.mask
            new_mask = _np_.append(new_mask, other_mask, 1)
            newdata.data = _np_.append(self.data, other, 1)
            newdata.mask = new_mask

        setas=self.setas.clone
        setas.column_headers=newdata_headers
        newdata._data._setas=setas
        newdata._data._setas.shape=newdata.shape
        for attr in self.__dict__:
            if attr not in ("setas","metadata", "data", "column_headers", "mask") and not attr.startswith("_"):
                newdata.__dict__[attr] = self.__dict__[attr]
        return newdata

    def __lshift__(self, other):
        """Overird the left shift << operator for a string or an iterable object to import using the :py:meth:`__read_iterable` function.

        Args:
            other (string or iterable object): Used to source the DataFile object

        Returns:
            DataFile: A new :py:class:`DataFile` object

        TODO:
            Make code work better with streams
        """
        newdata = DataFile()
        if isinstance(other, string_types):
            if python_v3:
                lines = map(lambda x: x, other.splitlines())
            else:
                lines = itertools.imap(lambda x: x, other.splitlines())
            newdata.__read_iterable(lines)
        elif isiterable(other):
            newdata.__read_iterable(other)
        return self.__class__(newdata)


    def __mod__(self, other):
        """Overload the % operator to mean column deletion.

        Args:
            Other (column index): column(s) to delete.

        Return:
            self: A copy of self with a column deleted.
        """
        newdata = self.clone
        return self.__mod_core__(other, newdata)

    def __imod__(self, other):
        """Overload the % operator to mean in-place column deletion.

        Args:
            Other (column index): column(s) to delete.

        Return:
            self: A copy of self with a column deleted.
        """
        newdata = self
        return self.__mod_core__(other, newdata)

    def __mod_core__(self, other, newdata):
        """Implements the column deletion method."""
        if isinstance(other, index_types):
            newdata.del_column(other)
        else:
            newdata = NotImplemented
        newdata._data._setas.shape=newdata.shape
        return newdata

    def __sub__(self, other):
        """Implements what to do when subtraction operator is used.

        Args:
            other (int,list of integers): Delete row(s) from data.

        Returns:
            newdata: A :py:data:`DataFile` with rows removed.
        """
        newdata = self.clone
        return self.__sub_core__(other, newdata)

    def __isub__(self, other):
        """Implements what to do when subtraction operator is used.

        Args:
            other (int,list of integers): Delete row(s) from data.

        Returns:
            self: The :py:data:`DataFile` with rows removed.
        """
        newdata = self
        return self.__sub_core__(other, newdata)

    def __sub_core__(self, other, newdata):
        """Actually do the subtraction."""
        if isinstance(other, (slice, int_types)) or callable(other):
            newdata.del_rows(other)
        elif isinstance(other, list) and (all_type(other,int_types) or all_type(other,bool)):
            newdata.del_rows(other)
        else:
            newdata = NotImplemented
        newdata._data._setas.shape=newdata.shape
        return newdata

    def __invert__(self):
        """The invert method will swap x and y column assignments around."""
        ret=self.clone
        setas=list(self.setas)
        cols=self.setas._cols
        if cols["axes"]==2:
            swaps=zip(["ycol","yerr"],["x","d"])
        elif cols["axes"]>=3:
            swaps=zip(["ycol","zcol","yerr","zerr"],["z","x","f","d"])
        setas[cols["xcol"]]="y"
        if cols["has_xerr"]:
            setas[cols["xerr"]]="e"
        for cname,nlet in swaps:
            for c in cols[cname]:
                setas[c]=nlet
        ret.setas=setas
        return ret#

    #============================================================================================================================
    ############################              Speical Methods                ####################################################
    #============================================================================================================================


    def __call__(self,*args,**kargs):
        """Clone the DataFile, but allowing additional arguments to modify the new clone.

        Creates a new clone of self and then passes all the arguments to the clones' __init__ method.
        """
        new_d=self.clone
        i = len(args) if len(args) < 2 else 2
        handler = [None, new_d._init_single, new_d._init_double, new_d._init_many][i]
        if handler is not None:
            handler(*args, **kargs)
        if kargs:  # set public attributes from keywords
            myattrs = new_d._public_attrs
            for k in kargs:
                if k in myattrs:
                    if isinstance(kargs[k], myattrs[k]):
                        new_d.__setattr__(k, kargs[k])
                    else:
                        if isinstance(myattrs[k], tuple):
                            typ = "one of " + ",".join([str(type(t)) for t in myattrs[k]])
                        else:
                            typ = "a {}".format(type(myattrs[k]))
                        raise TypeError("{} should be {} not a {}".format(k, typ, type(kargs[k])))

        return new_d

    def __contains__(self, item):
        """Operator function for membertship tests - used to check metadata contents.

        Args:
            item(string): name of metadata key

        Returns:
            bool: True if item in self.metadata
        """
        return item in self.metadata

    def __deepcopy__(self, memo):
        """Provides support for copy.deepcopy to work."""
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            try:
                setattr(result, k, copy.deepcopy(v, memo))
            except Exception:
                setattr(result, k, copy.copy(v))
        return result

    def __delitem__(self, item):
        """Implements row or metadata deletion.

        Args:
            item (ingteger or string):  row index or name of metadata to delete
        """
        if isinstance(item, string_types):
            del (self.metadata[item])
        else:
            self.del_rows(item)

    def __dir__(self):
        """Reeturns the attributes of the current object by augmenting the keys of self.__dict__ with the attributes that __getattr__ will handle."""
        attr = dir(type(self))
        col_check = {"xcol": "x", "xerr": "d", "ycol": "y", "yerr": "e", "zcol": "z", "zerr": "f"}
        for k in col_check:
            if "_setas" not in self.__dict__:
                break
            if k.startswith("x"):
                if k in self._data._setas.cols and self._data._setas.cols[k] is not None:
                    attr.append(col_check[k])
            else:
                if k in self._data._setas.cols and self._data._setas.cols[k]:
                    attr.append(col_check[k])
        return sorted(set(attr))

    def __floordiv__(self, other):
        """Just aslias for self.column(other)."""
        if not isinstance(other, index_types):
            return NotImplemented
        return self.column(other)

    def __getattr__(self, name):
        """Called for :py:class:`DataFile`.x to handle some special pseudo attributes and otherwise to act as a shortcut for :py:meth:`column`.

        Args:
            name (string): The name of the attribute to be returned.

        Returns:
            Various: the DataFile object in various forms

        Supported attributes:
            - records - return the DataFile data as a numpy structured
            array - i.e. rows of elements whose keys are column headings
            - clone - returns a deep copy of the current DataFile instance

        Otherwise the name parameter is tried as an argument to
        :py:meth:`DataFile.column` and the resultant column isreturned. If
        DataFile.column raises a KeyError this is remapped as an
        AttributeError.
       """
        setas_cols = ("x", "y", "z", "d", "e", "f", "u", "v", "w", "r", "q", "p")
        if name!="debug" and self.debug: print(name)
        try:
            return super(DataFile, self).__getattr__(name)
        except AttributeError:
            pass
        if name in setas_cols:
            ret=self._getattr_col(name)
            if ret is not None: return ret
        if name in self.setas.cols:
            ret=self.setas.cols[name]
            if ret is not None and ret!=[]:
                return ret
        try:
            col = self._data._setas.find_col(name)
            return self.column(col)
        except (KeyError, IndexError):
            pass
        if name in setas_cols: # Probably tried to use a setas col when it wasn't defined
            raise StonerSetasError("Tried accessing a {} column, but setas is not defined and {} is not a column name either".format(name,name))
        raise AttributeError("{} is not an attribute of DataFile nor a column name".format(name))

    def __getitem__(self, name):
        """Called for DataFile[x] to return either a row or iterm of metadata.

        Args:
            name (string or slice or int): The name, slice or number of the part of the
            :py:class:`DataFile` to be returned.

        Returns:
            mixed: an item of metadata or row(s) of data.

        - If name is an integer then the corresponding single row will be returned
        - if name is a slice, then the corresponding rows of data will be returned.
        - If name is a string then the metadata dictionary item             with the correspondoing key will be returned.
        - If name is a numpy array then the corresponding rows of the data are returned.
        - If a tuple is supplied as the arguement then there are a number of possible behaviours.
            - If the first element of the tuple is a string, then it is assumed that it is the nth element of the named metadata is required.
            - Otherwise itis assumed that it is a particular element within a column determined by the second part of the tuple that is required.

        Examples:
            DataFile['Temp',5] would return the 6th element of the
            list of elements in the metadata called 'Temp', while

            DataFile[5,'Temp'] would return the 6th row of the data column
            called 'Temp'

            and DataFile[5,3] would return the 6th element of the
            4th column.
        """
        if isinstance(name, string_types+(re._pattern_type,)):
            try:
                ret = self.__meta__(name)
            except KeyError:
                try:
                    ret=self.data[name]
                except KeyError:
                    raise KeyError("{} was neither a key in the metadata nor a column in the main data.".format(name))
        elif isinstance(name,tuple) and isinstance(name[0],string_types):
            try:
                rest=name[1:]
                ret=self.__meta__(name[0])
                ret=ret.__getitem__(*rest)
            except KeyError:
                try:
                    ret=self.data[name]
                except KeyError:
                    raise KeyError("{} was neither a key in the metadata nor a column in the main data.".format(name))
        elif isinstance(name,tuple) and name in self.metadata:
            ret=self.metadata[name]
        else:
            ret=self.data[name]
        return ret

    def __getstate__(self):
        """Get ready for picking this object - used for deepcopy."""
        return {"data": self.data, "column_headers": self.column_headers, "metadata": self.metadata,"filename":self.filename}


    def __iter__(self):
        """Provide agenerator for iterating.

        Pass through to :py:meth:`DataFile.rows` for the actual work.

        Returns:
            Next row
        """
        for r in self.rows(False):
            yield r

    def __len__(self):
        """Return the length of the data.

        Returns: Returns the number of rows of data
        """
        if _np_.prod(self.data.shape)>0:
            return _np_.shape(self.data)[0]
        return 0

    def __reduce_ex__(self, p):
        """Machinery used for deepcopy."""
        cls=self.__class__
        return (cls, (), self.__getstate__())

    def __repr__(self):
        """Outputs the :py:class:`DataFile` object in TDI format.

        This allows one to print any :py:class:`DataFile` to a stream based
        object andgenerate a reasonable textual representation of the data.shape

        Returns:
            self in a textual format.
        """
        if get_option("short_repr") or get_option("short_data_repr"):
            return self._repr_short_()
        try:
            return self._repr_table_()
        except Exception:
            return self.__repr_core__(256)

    def __setattr__(self, name, value):
        """Handles attempts to set attributes not covered with class attribute variables.

        Args:
            name (string): Name of attribute to set. Details of possible attributes below:

        - mask Passes through to the mask attribute of self.data (which is a numpy masked array). Also handles the case where you pass a callable object
            to nask where we pass each row to the function and use the return reult as the mask
        - data Ensures that the :py:attr:`data` attribute is always a :py:class:`numpy.ma.maskedarray`
        """
        if hasattr(type(self),name) and isinstance(getattr(type(self),name),property):
            super(DataFile, self).__setattr__(name, value)
        elif len(name) == 1 and name in "xyzuvwdef" and self.setas[name]:
            self.__setattr_col(name, value)
        else:
            super(DataFile, self).__setattr__(name, value)

    def __setitem__(self, name, value):
        """Called for :py:class:`DataFile`[name ] = value to write mewtadata entries.

        Args:
            name (string, tuple): The string key used to access the metadata or a tuple index into data
            value (any): The value to be written into the metadata or data/

        Notes:
            If name is a string or already exists as key in metadata, this setitem will set metadata values, otherwise if name
            is a tuple then if the first elem,ent in a string it checks to see if that is an existing metadata item that is iterable,
            and if so, sets the metadta. In all other circumstances, it attempts to set an item in the main data array.
        """
        if isinstance(name,string_types) or str(name) in self.metadata:
            self.metadata[name] = value
        elif isinstance(name,tuple):
            if isinstance(name[0],string_types) and name[0] in self.metadata and isiterable(self.metadata[name[0]]):
                if len(name)==2:
                    key=name[0]
                    name=name[1]
                else:
                    key=name[0]
                    name=tuple(name[1:])
                self.metadata[key][name]=value
            else:
                self.data[name]=value
        else:
            self.data[name]=value

    def __setstate__(self, state):
        """Internal function for pickling."""
        self.data = DataArray(state["data"],setas=self._data._setas)
        self.column_headers = state["column_headers"]
        self.metadata = state["metadata"]

    def __str__(self):
        """Provides an implementation for str(DataFile) that does not shorten the output."""
        return self.__repr_core__(False)

    #============================================================================================================================
    ############################              Private Methods                ####################################################
    #============================================================================================================================

    def _col_args(self,*args,**kargs):
        """Utility method that creates an object which has keys  based either on arguments or setas attribute."""
        return self.data._col_args(*args,**kargs) #Now just pass through to DataArray

    def __file_dialog(self, mode):
        """Creates a file dialog box for loading or saving ~b DataFile objects.

        Args:
            mode (string): The mode of the file operation  'r' or 'w'

        Returns:
            A filename to be used for the file operation.
        """
        # Wildcard pattern to be used in file dialogs.

        descs = {}
        patterns = self.patterns
        for p in patterns:  # pylint: disable=not-an-iterable
            descs[p] = self.__class__.__name__ + " file"
        for c in self.subclasses:  # pylint: disable=not-an-iterable
            for p in (self.subclasses[c].patterns):  # pylint: disable=unsubscriptable-object
                if p in descs:
                    descs[p] += ", " + self.subclasses[c].__name__ + " file"  # pylint: disable=unsubscriptable-object
                else:
                    descs[p] = self.subclasses[c].__name__ + " file"  # pylint: disable=unsubscriptable-object

        patterns = [(descs[p], p) for p in sorted(descs.keys())]
        patterns.insert(0,("All File", "*.*"))

        if self.filename is not None:
            filename = os.path.basename(self.filename)
            dirname = os.path.dirname(self.filename)
        else:
            filename = ""
            dirname = ""
        if "r" in mode:
            mode = "file"
        elif "w" in mode:
            mode = "save"
        else:
            mode = "directory"
        dlg = get_filedialog(what=mode, initialdir=dirname, initialfile=filename, filetypes=patterns)
        if dlg:
            self.filename = dlg
            return self.filename
        return None

    def _getattr_col(self, name):
        """Get a column using the setas attribute."""
        try:
            return self._data.__getattr__(name)
        except StonerSetasError:
            return None

    def _interesting_cols(self,cols):
        """Workout which columns the user might be interested in in the basis of the setas.

        ArgsL
            cols (float): Maximum Number of columns to display

        Returns
            list(ints): The indices of interesting columns with breaks in runs indicated by -1
        """
        c=self.shape[1]
        if c>cols:
            interesting=[]
            last=-1
            for ix,typ in enumerate(self.setas):
                if last!=-1 and last!=ix-1:
                    interesting.append(-1)
                    last=-1
                if typ!=".":
                    interesting.append(ix)
                    last=ix
            if interesting and interesting[-1]==-1:
                interesting=interesting[:-1]
            if interesting:
                c_start=max(interesting)+1
            else:
                c_start=0
            interesting.extend(range(c_start,c))
            if len(interesting)<cols:
                cols=len(interesting)
            if interesting[cols-3]!=-1:
                interesting[cols-2]=-1
            else:
                interesting[cols-2]=c-2
            interesting[cols-1]=c-1
            interesting=interesting[:cols]
            c=cols
        else:
            interesting=list(range(c))

        col_assignments=[]
        for i in interesting:
            if i!=-1:
                if self.setas[i]!=".":
                    col_assignments.append("{} ({})".format(i,self.setas[i]))
                else:
                    col_assignments.append("{}".format(i))
            else:
                col_assignments.append("")
        return interesting,col_assignments,cols

    def _load(self, filename, *args, **kargs):
        """Actually load the data from disc assuming a .tdi file format.

        Args:
            filename (str): Path to filename to be loaded. If None or False, a dialog bax is raised to
                ask for the filename.

        Returns:
            DataFile: A copy of the newly loaded :py:class`DataFile` object.

        Exceptions:
            StonerLoadError: Raised if the first row does not start with 'TDI Format 1.5' or 'TDI Format=1.0'.

        Note:
            The *_load* methods shouldbe overidden in each child class to handle the process of loading data from
                disc. If they encounter unexpected data, then they should raise StonerLoadError to signal this, so that
                the loading class can try a different sub-class instead.
        """
        if filename is None or not filename:
            self.get_filename('r')
        else:
            self.filename = filename
        with io.open(self.filename, "r",encoding="utf-8",errors="ignore") as datafile:
            try:
                reader = csv.reader(datafile, dialect=_tab_delimited())
                row = next(reader)
                if row[0].strip() == "TDI Format 1.5":
                    fmt = 1.5
                elif row[0].strip() == "TDI Format=Text 1.0":
                    fmt = 1.0
                else:
                    raise StonerLoadError("Not a TDI File")
            except Exception:
                raise StonerLoadError("Not a TDI File")
            col_headers_tmp = [x.strip() for x in row[1:]]
            data_array = 0
            metaDataArray = 0
            cols = 0
            for row in reader:  # Now read through the metadata columns
                if len(row) > 1 and row[1].strip() != "":
                    data_array += 1
                    still_data = True
                else:
                    still_data = False
                if row[0].strip() == "":  #end of metadata:
                    break
                else:
                    cols = max(cols, len(row))
                    metaDataArray += 1
                    self.metadata.import_key(row[0])
        #End of metadata reading, close filke and reopen to read data
        if still_data:  # data extends beyond metada - read with genfromtxt
            self.data = DataArray(_np_.genfromtxt(self.filename,
                                        skip_header=1,
                                        usemask=True,
                                        delimiter="\t",
                                        usecols=range(1, cols),
                                        invalid_raise=False,
                                        comments="\0"))
        elif data_array > 0:  # some data less than metadata
            footer = metaDataArray - data_array
            self.data = DataArray(_np_.genfromtxt(self.filename,
                                        skip_header=1,
                                        skip_footer=footer,
                                        usemask=True,
                                        delimiter="\t",
                                        comments="\0",
                                        usecols=range(1, cols)))
        else:
            self.data = _np_.atleast_2d(_np_.array([]))
        if len(self.data.shape) >= 2 and self.data.shape[1] > 0:
            self.column_headers=col_headers_tmp
        self["TDI Format"]=fmt

    def __parse_metadata(self, key, value):
        """Parse the metadata string, removing the type hints into a separate dictionary from the metadata.

        Args:
            key (string): The name of the metadata parameter to be written,
        possibly including a type hinting string.
            value (any): The value of the item of metadata.

        Note:
            Uses the typehint to set the type correctly in the dictionary

            All the clever work of managing the typehinting is done in the
        metadata dictionary object now.
        """
        self.metadata[key] = value

    def __read_iterable(self, reader):
        """Internal method to read a string representation of py:class:`DataFile` in line by line."""
        if "next" in dir(reader): # Python v2 iterator
            readline = reader.next
        elif "readline" in dir(reader): #Filelike iterator
            readline = reader.readline
        elif "__next__" in dir(reader):# Python v3 iterator
            readline = reader.__next__
        else:
            raise AttributeError("No method to read a line in {}".format(reader))
        row = readline().split('\t')
        if row[0].strip() == "TDI Format 1.5":
            fmt = 1.5
        elif row[0].strip() == "TDI Format=Text 1.0":
            fmt = 1.0
        else:
            raise RuntimeError("Not a TDI File")
        col_headers_tmp = [x.strip() for x in row[1:]]
        cols = len(col_headers_tmp)
        self._data._setas = _setas("." * cols)
        self.data = DataArray([],setas=self._data._setas)
        for r in reader:
            if r.strip() == "":  # Blank line
                continue
            row = r.rstrip().split('\t')
            cols = max(cols, len(row) - 1)
            if row[0].strip() != '':
                md = row[0].split('=')
                if len(md) == 2:
                    md[1] = "=".join(md[1:])
                elif len(md) <= 1:
                    md.extend(['', ''])

                if format == 1.5:
                    self.metadata[md[0].strip()] = md[1].strip()
                elif format == 1.0:
                    self.metadata[md[0].strip()] = self.metadata.string_to_type(md[1].strip())
            if len(row) < 2:
                continue
            self.data = _np_.append(self.data, self._conv_float(row[1:]))
        self.data = _np_.reshape(self.data, (-1, cols))
        self.column_headers = ["Column {}".format(i) for i in range(cols)]
        for i,head_temp in enumerate(col_headers_tmp):
            self.column_headers[i] = head_temp
        self["TDI Format"]=fmt

    def __repr_core__(self, shorten=1000):
        """Actuall do the repr work, but allow for a shorten parameter to save printing big files out to disc."""
        outp = "TDI Format 1.5\t" + "\t".join(self.column_headers) + "\n"
        m = len(self.metadata)
        self.data = _np_.atleast_2d(self.data)
        r = _np_.shape(self.data)[0]
        md = self.metadata.export_all()
        for x in range(min(r, m)):
            if self.data.ndim!=2 or self.shape[1]==1:
                outp = outp + md[x] + "\t{}\n".format(self.data[x])
            else:
                outp = outp + md[x] + "\t" + "\t".join([str(y) for y in self.data[x].filled()]) + "\n"
        if m > r:  # More metadata
            for x in range(r, m):
                outp = outp + md[x] + "\n"
        elif r > m:  # More data than metadata
            if shorten is not None and shorten and r - m > shorten:
                for x in range(m, m + shorten - 100):
                    if self.data.ndim!=2 or self.shape[1]==1:
                        outp += "\t" + "\t{}\n".format(self.data[x])
                    else:
                        outp += "\t" + "\t".join([str(y) for y in self.data[x].filled()]) + "\n"
                outp += "... {} lines skipped...\n".format(r - m - shorten + 100)
                for x in range(-100, -1):
                    if self.data.ndim!=2 or self.shape[1]==1:
                        outp += "\t" + "\t{}\n".format(self.data[x])
                    else:
                        outp += "\t" + "\t".join([str(y) for y in self.data[x].filled()]) + "\n"
            else:
                for x in range(m, r):
                    if self.data.ndim!=2 or self.shape[1]==1:
                        outp = outp + "\t" + "\t{}\n".format(self.data[x])
                    else:
                        outp = outp + "\t" + "\t".join([str(y) for y in self.data[x].filled()]) + "\n"
        return outp

    def _repr_html_private(self):
        """Version of repr_core that does and html output."""
        return self._repr_table_("html")

    def _repr_short_(self):
        return "{}({}) of shape {} ({}) and {} items of metadata".format(self.filename,type(self),self.shape,"".join(self.setas),len(self.metadata))

    def _repr_table_(self,fmt="rst"):
        """Convert the DataFile to a 2D array and then feed to tabulate."""
        if tabulate is None:
            raise ImportError("No tabulate.")
        lb="<br/>" if fmt=="html" else "\n"
        rows,cols=self._repr_limits
        r,c=self.shape
        interesting,col_assignments,cols=self._interesting_cols(cols)
        c=min(c,cols)
        c_w=max([len(self.column_headers[x]) for x in interesting if x>-1])
        wrapper=TextWrapper(subsequent_indent="\t",width=max(20,max(20,(80-c_w*c))))
        if r>rows:
            shorten=[True,False]
            r=rows+rows%2
        else:
            shorten=[False,False]

        shorten[1]=c>cols
        r=max(len(self.metadata),r)

        outp=_np_.zeros((r+1,c+1),dtype=object)
        outp[:,:]="..."
        ch=[self.column_headers[ix] if ix>=0 else "...." for ix in interesting]

        for ix,(h,i) in enumerate(zip(ch,col_assignments)):
            spaces1=" "*((c_w-len(h))//2)
            spaces2=" "*((c_w-len(i))//2)
            ch[ix]="{}{}{}{}{}".format(spaces1,h,lb,spaces2,i)
            if self.debug: print(len(spaces1),len(spaces2))
        outp[0,1:]=ch
        outp[1,1:]=col_assignments
        outp[0,0]="TDI Format 1.5{}index".format(lb)
        i=1
        for md in self.metadata.export_all():
            md=md.replace("=","= ")
            for line in wrapper.wrap(md):
                if i>=outp.shape[0]:
                    outp=_np_.append(outp,[[""]*outp.shape[1]],axis=0)
                outp[i,0]=line
                i+=1
        for ic,c in enumerate(interesting):
            if c>=0:
                if shorten[0]:

                    col_out=_np_.where(self.mask[:r//2-1,c],"#####",self.data[:r//2-1,c].astype(str))
                    outp[1:r//2,ic+1]=col_out
                    col_out=_np_.where(self.mask[-r//2:,c],"#####",self.data[-r//2:,c].astype(str))
                    outp[r//2+1:r+1,ic+1]=col_out
                else:
                    col_out=_np_.where(self.mask[:,c],"#####",self.data[:,c].astype(str))
                    outp[1:len(self.data)+1,ic+1]=col_out
        return tabulate(outp[1:],outp[0],tablefmt=fmt,numalign="decimal",stralign="left")

    def __search_index(self, xcol, value, accuracy):
        """Helper for the search method that returns an array of booleans for indexing matching rows."""
        x = self.find_col(xcol)
        if isinstance(value, (int_types, float)):
            ix = _np_.less_equal(_np_.abs(self.data[:, x] - value), accuracy)
        elif isinstance(value, tuple) and len(value) == 2:
            (l, u) = (min(value), max(value))
            l-=accuracy
            u+=accuracy
            v=self.data[:,x]
            l=_np_.ones_like(v)*l
            u=_np_.ones_like(v)*u
            ix=_np_.logical_and(v>l,v<=u)
        elif isinstance(value, (list, _np_.ndarray)):
            ix = _np_.zeros(len(self), dtype=bool)
            for v in value:
                ix = _np_.logical_or(ix, self.__search_index(xcol, v),accuracy)
        elif callable(value):
            ix = _np_.array([value(r[x],r) for r in self], dtype=bool)
        else:
            raise RuntimeError("Unknown search value type {}".format(value))
        return ix

    def __setattr_col(self, name, value):
        """Attempts to either assign data columns if set up, or setas setting.

        Args:
            name (length 1 string): Column type to work with (one of x,y,z,u,v,w,d,e or f)
            value (nd array or column index): If an ndarray and the column type corresponding to *name* is set up,
                then overwrite the column(s) of data with this new data. If an index type, then set the corresponding setas
                assignment to these columns.
        """
        if isinstance(value, _np_.ndarray):
            value = _np_.atleast_2d(value)
            if value.shape[0] == self.data.shape[0]:
                pass
            elif value.shape[1] == self.data.shape[0]:
                value = value.T
            else:
                raise RuntimeError("Value to be assigned to data columns is the wrong shape!")
            for i, ix in enumerate(self.find_col(self.setas[name], force_list=True)):
                self.data[:, ix] = value[:, i]
        elif isinstance(value, index_types):
            self._set_setas({name: value})

    def _set_mask(self, func, invert=False, cumulative=False, col=0):
        """Applies func to each row in self.data and uses the result to set the mask for the row.

        Args:
            func (callable): A Callable object of the form lambda x:True where x is a row of data (numpy
            invert (bool): Optionally invert te reult of the func test so that it unmasks data instead
            cumulative (bool): if tru, then an unmask value doesn't unmask the data, it just leaves it as it is.
        """
        i = -1
        args = len(_inspect_.getargs(func.__code__)[0])
        for r in self.rows():
            i += 1
            if args == 2:
                t = func(r[col], r)
            else:
                t = func(r)
            if isinstance(t, (bool, _np_.bool_)):
                if t ^ invert:
                    self.data[i] = _ma_.masked
                elif not cumulative:
                    self.data[i] = self._data.data[i]
            else:
                for j in range(min(len(t), _np_.shape(self.data)[1])):
                    if t[j] ^ invert:
                        self.data[i, j] = _ma_.masked
                    elif not cumulative:
                        self.data[i, j] = self.data.data[i, j]

    def _push_mask(self, mask=None):
        """Copy the current data mask to a temporary store and replace it with a new mask if supplied.

        Args:
            mask (:py:class:numpy.array of bool or bool or None):
                The new data mask to apply (defaults to None = unmask the data

        Returns:
            Nothing
        """
        self._masks.append(self.mask)
        if mask is None:
            self.data.mask = False
        else:
            self.mask = mask


    def _pop_mask(self):
        """Replaces the mask on the data with the last one stored by _push_mask().

        Returns:
            Nothing
        """
        self.mask = False
        self.mask = self._masks.pop()
        if not self._masks:
            self._masks = [False]

    def _raise_type_error(self,k):
        """Raise a type error when setting an attribute k."""
        if isinstance(self._public_attrs[k], tuple):
            typ = "one of " + ",".join([str(type(t)) for t in self._public_attrs[k]])
        else:
            typ = "a {}".format(type(self._public_attrs[k]))
        raise TypeError("{} should be {}".format(k, typ))

    #============================================================================================================================
    ############################              Public Methods                ####################################################
    #============================================================================================================================

    def add_column(self, column_data, header=None, index=None, func_args=None, replace=False,setas=None):
        """Appends a column of data or inserts a column to a datafile instance.

        Args:
            column_data (:py:class:`numpy.array` or list or callable): Data to append or insert or a callable function that will generate new data

        Keyword Arguments:
            header (string): The text to set the column header to,
                if not supplied then defaults to 'col#'
            index (index type): The  index (numeric or string) to insert (or replace) the data
            func_args (dict): If column_data is a callable object, then this argument
                can be used to supply a dictionary of function arguments to the callable object.
            replace (bool): Replace the data or insert the data (default)
            setas (str): Set the type of column (x,y,z data etc - see :py:attr:`Stoner.Core.DataFile.setas`)

        Returns:
            self: The :py:class:`DataFile` instance with the additonal column inserted.

        Note:
            Like most :py:class:`DataFile` methods, this method operates in-place in that it also modifies
            the original DataFile Instance as well as returning it.
        """
        if index is None or isinstance(index,bool) and index:
            index = self.shape[1]
            replace = False
            if header is None:
                header = "Col{}".format(index)
        else:
            index = self.find_col(index)
            if header is None:
                header = self.column_headers[index]

        if isinstance(setas,str) and len(setas)==1 and setas in "xyzdefuvw.-":
            pass
        elif setas is not None:
            raise TypeError("setas parameter should be a single letter in the set xyzdefuvw.-, not {}".format(setas))
        else:
            setas="."

        if isinstance(column_data, list):
            column_data = _np_.array(column_data)

        if isinstance(column_data, _np_.ndarray):
            if len(_np_.shape(column_data)) != 1:
                raise ValueError('Column data must be 1 dimensional')
            else:
                _np__data = column_data
        elif callable(column_data):
            if isinstance(func_args, dict):
                new_data = [column_data(x, **func_args) for x in self]
            else:
                new_data = [column_data(x) for x in self]
            _np__data = _np_.array(new_data)
        else:
            return NotImplemented
        #Sort out the sizes of the arrays
        cl = len(_np__data)
        if len(self.data.shape) == 2:
            (dr, dc) = self.data.shape
        elif len(self.data.shape) == 1:
            self.data = _np_.atleast_2d(self.data).T
            (dr, dc) = self.data.shape
        elif not self.data.shape:
            self.data = _np_.array([[]])
            (dr, dc) = (0, 0)
        if cl > dr and dc * dr > 0:
            self.data = DataArray(_np_.append(self.data, _np_.zeros((cl - dr, dc)), 0),setas=self.data._setas)
        elif cl < dr:
            _np__data = _np_.append(_np__data, _np_.zeros(dr - cl))
        if replace:
            self.data[:, index] = _np__data
            if setas!="-":
                self.setas[index]=setas

        else:
            if dc * dr == 0:
                self.data = DataArray(_np_.transpose(_np_.atleast_2d(_np__data)),setas=self.data._setas)
                self.column_headers=[header,]
                self.setas=setas

            else:
                columns=copy.copy(self.column_headers)
                old_setas=list(self.setas)
                if setas!="-":
                    old_setas.insert(index,setas)
                else:
                    old_setas.insert(index,old_setas[index])
                self.data = DataArray(_np_.insert(self.data, index, _np__data, 1))
                self.setas(old_setas)  # [ylint: disable=not-callable]
                columns.insert(index,header)
                self.column_headers=columns
        return self

    def closest(self,value,xcol=None):
        """Return the row in a data file which has an x-column value closest to the given value.

        Args:
            value (float): Value to search for.

        Keyword Arguments:
            xcol (index or None): Column in which to look for value, or None to use setas.

        Returns:
            ndarray: A single row of data as a :py:class:`Stoner.Core.DataArray`.

        Notes: To find which row it is that has been returned, use the :py:attr:`Stoner.Core.DataArray.i` index attribute.
        """
        _=self._col_args(xcol=xcol)
        xdata=_np_.abs(self//_.xcol-value)
        i=int(xdata.argmin())
        return self[i]



    def column(self, col):
        """Extracts one or more columns of data from the datafile by name, partial name, regular expression or numeric index.

        Args:
            col (int, string, list or re): is the column index as defined for :py:meth:`DataFile.find_col`

        Returns:
            ndarray: One or more columns of data as a :py:class:`numpy.ndarray`.
        """
        return self.data[:, self.find_col(col)]

    def columns(self,not_masked=False):
        """Generator method that will iterate over the columns of data int he datafile.

        Yields:
            1D array: Returns the next column of data.
        """
        for ix,col in enumerate(self.data.T):
            if _ma_.is_masked(col):
                continue
            else:
                yield self.column(ix)

    def count(self,axis=0):
        """Count the number of un-masked elements in the :py:class:`DataFile`.

        Keywords:
            axis (int): Which axis to count the unmasked elements along.

        Returns:
            (int): Number of unmasked elements.
        """
        return self.data.count(axis)

    def del_column(self, col=None, duplicates=False):
        """Deletes a column from the current :py:class:`DataFile` object.

        Args:
            col (int, string, iterable of booleans, list or re): is the column index as defined for :py:meth:`DataFile.find_col` to the column to be deleted

        Keyword Arguments:
            duplicates (bool): (default False) look for duplicated columns

        Returns:
            self: The :py:class:`DataFile` object with the column deleted.

        Note:
            - If duplicates is True and col is None then all duplicate columns are removed,
            - if col is not None and duplicates is True then all duplicates of the specified column are removed.
            - If duplicates is False then *col* must not be None otherwise a RuntimeError is raised.
            - If col is a list (duplicates should not be None) then the all the matching columns are found.
            - If col is an iterable of booleans, then all columns whose elements are False are deleted.
            - If col is None and duplicates is None, then all columns with at least one elelemtn masked
                    will be deleted
        """
        if duplicates:
            ch = self.column_headers
            dups = []
            if col is None:
                for i,chi in enumerate(ch):
                    if chi in ch[i + 1:]:
                        dups.append(ch.index(chi, i + 1))
            else:
                col = ch[self.find_col(col)]
                i = ch.index(col)
                while True:
                    try:
                        i = ch.index(col, i + 1)
                        dups.append(i)
                    except ValueError:
                        break
            return self.del_column(dups, duplicates=False)
        else:
            if col is None: # Without defining col we just compress by the mask
                self.data = _ma_.mask_cols(self.data)
                t = DataArray(self.column_headers)
                t.mask = self.mask[0]
                self.column_headers = list(_ma_.compressed(t))
                self.data = _ma_.compress_cols(self.data)
            elif isiterable(col) and all_type(col,bool): # If col is an iterable of booleans then we index by that
                col=~_np_.array(col)
                new_setas=_np_.array(self.setas)[col]
                new_column_headers=_np_.array(self.column_headers)[col]
                self.data=self.data[:,col]
                self.column_headers=new_column_headers
                self.setas=new_setas
            else: # Otherwise find individual columns
                c = self.find_col(col)
                ch=self.column_headers
                self.data = DataArray(_np_.delete(self.data, c, 1), mask=_np_.delete(self.data.mask, c, 1))
                if isinstance(c, list):
                    c.sort(reverse=True)
                else:
                    c = [c]
                for cl in c:
                    del ch[cl]
                self.column_headers=ch
            return self

    def del_nan(self,col=None,clone=False):
        """Remove rows that have nan in them.

        eyword Arguments:
            col (index types or None): column(s) to look for nan's in. If None or not given, use setas columns.
            cone (boolean): if True clone the current object before running and then return the clone not self.

        Return:
            self (DataFile): Returns a copy of the current object (or clone if *clone*=True)
        """
        if clone: #Set ret to be our clone
            ret=self.clone
        else: #Not cloning so ret is self
            ret=self

        if col is None: #If col is still None, use all columsn that are set to any value in self.setas
            col=[ix for ix,col in enumerate(self.setas) if col!="."]
        if not islike_list(col): #If col isn't a list, make it one now
            col=[col]
        col=[ret.find_col(c) for c in col] #Normalise col to be a list of integers
        dels=_np_.zeros(len(ret)).astype(bool)
        for ix in col:
            dels=_np_.logical_or(dels,_np_.isnan(ret.data[:,ix])) # dels contains True if any row contains a NaN in columns col
        not_masked=_np_.logical_not(_ma_.mask_rows(ret.data).mask[:,0]) # Get rows wqhich are not masked
        dels=_np_.logical_and(not_masked,dels) # And make dels just be unmasked rows with NaNs

        ret.del_rows(_np_.logical_not(dels)) # Del the those rows
        return ret

    def del_rows(self, col=None, val=None, invert=False):
        """Searchs in the numerica data for the lines that match and deletes the corresponding rows.

        Args:
            col (list,slice,int,string, re, callable or None): Column containg values to search for.
            val (float or callable): Specifies rows to delete. Maybe:

                - None - in which case the *col* argument is used to identify rows to be deleted,
                - a float in which case rows whose columncol = val are deleted
                - or a function - in which case rows where the function evaluates to be true are deleted.
                - a tuple, in which case rows where column col takes value between the minium and maximum of the tuple
                  are deleted.

        Keyword Arguments:
            invert (bool): Specifies whether to invert the logic of the test to delete a row. If True, keep the rows
                that would have been deleted otherwise.

        Returns:
            self: The current :py:class:`DataFile` object

        Note:
            If col is None, then all rows with masked data are deleted

            if *col* is callable then it is passed each row as a :py:class:`DataArray` and if it returns
            True, then the row will be deleted or kept depending on the value of *invert*.

            If *val* is a callable it should take two arguments - a float and a
            list. The float is the value of the current row that corresponds to column col abd the second
            argument is the current row.

        TODO:
            Implement val is a tuple for deletinging in a range of values.
        """
        if col is None:
            self.data = _ma_.mask_rows(self.data)
            self.data = _ma_.compress_rows(self.data)
        else:
            if isinstance(col, slice) and val is None: #delete rows with a slice to make a list of indices
                indices = col.indices(len(self))
                col = list(range(*indices))
            elif callable(col) and val is None: # Delete rows usinga callalble taking the whole row
                col=[r.i for r in self.rows() if col(r)]
            elif isiterable(col) and all_type(col,bool): # Delete rows by a list of booleans
                if len(col)<len(self):
                    col.extend([False]*(len(self)-len(col)))
                self.data=self.data[col]
                return self
            if isiterable(col) and all_type(col,int_types) and val is None and not invert:
                col.sort(reverse=True)
                for c in col:
                    self.del_rows(c)
            elif isinstance(col, list) and all_type(col,int_types) and val is None and invert:
                for i in range(len(self) - 1, -1, -1):
                    if i not in col:
                        self.del_rows(i)
            elif isinstance(col, int_types) and val is None and not invert:
                tmp_mask=self.mask
                tmp_setas=self.data._setas.clone
                self.data = _np_.delete(self.data, col, 0)
                self.data.mask=_np_.delete(tmp_mask, col, 0)
                self.data._setas=tmp_setas
            elif isinstance(col, int_types) and val is None and invert:
                self.del_rows([c], invert=invert)
            else:
                col = self.find_col(col)
                d = self.column(col)
                if callable(val):
                    rows = _np_.nonzero([(bool(val(x[col], x) and bool(x[col] is not _ma_.masked)) != invert)
                                         for x in self])[0]
                elif isinstance(val, float):
                    rows = _np_.nonzero([bool(x == val) != invert for x in d])[0]
                elif isiterable(val) and len(val) == 2:
                    (upper, lower) = (max(list(val)), min(list(val)))
                    rows = _np_.nonzero([bool(lower <= x <= upper) != invert for x in d])[0]
                else:
                    raise SyntaxError("If val is specified it must be a float,callable, or iterable object of length 2")
                tmp_mask=self.mask
                tmp_setas=self.data._setas.clone
                self.data = _np_.delete(self.data, rows, 0)
                self.data.mask=_np_.delete(tmp_mask, rows, 0)
                self.data._setas=tmp_setas
        return self

    def dir(self, pattern=None):
        """Return a list of keys in the metadata, filtering wiht a regular expression if necessary.

        Keyword Arguments:
            pattern (string or re): is a regular expression or None to list all keys

        Returns:
            list: A list of metadata keys.
        """
        if pattern is None:
            return list(self.metadata.keys())
        else:
            if isinstance(pattern, re._pattern_type):
                test = pattern
            else:
                test = re.compile(pattern)
            possible = [x for x in self.metadata.keys() if test.search(x)]
            return possible

    def filter(self, func=None, cols=None, reset=True):
        """Sets the mask on rows of data by evaluating a function for each row.

        Args:
            func (callable): is a callable object that should take a single list as a p[arameter representing one row.
            cols (list): a list of column indices that are used to form the list of values passed to func.
            reset (bool): determines whether the mask is reset before doing the filter (otherwise rows already masked out will be ignored
                in the filter (so the filter is logically or'd)) The default value of None results in a complete row being passed into func.

        Returns:
            self: The current :py:class:`DataFile` object with the mask set
        """
        if cols is not None:
            cols = [self.find_col(c) for c in cols]
        if reset: self.data.mask = False
        for r in self.rows():
            if cols is None:
                self.mask[r.i,:]= not func(r)
            else:
                self.mask[r.i,:] = not func(r[cols])
        return self

    def find_col(self, col, force_list=False):
        """Indexes the column headers in order to locate a column of data.shape.

        Indexing can be by supplying an integer, a string, a regular experssion, a slice or a list of any of the above.

        -   Integer indices are simply checked to ensure that they are in range
        -   String indices are first checked for an exact match against a column header
            if that fails they are then compiled to a regular expression and the first
            match to a column header is taken.
        -   A regular expression index is simply matched against the column headers and the
            first match found is taken. This allows additional regular expression options
            such as case insensitivity.
        -   A slice index is converted to a list of integers and processed as below
        -   A list index returns the results of feading each item in the list at :py:meth:`find_col`
            in turn.

        Args:
            col (int, a string, a re, a slice or a list):  Which column(s) to retuirn indices for.

        Keyword Arguments:
            force_list (bool): Force the output always to be a list. Mainly for internal use only

        Returns:
            int, list of ints: The matching column index as an integer or a KeyError
        """
        return self.data._setas.find_col(col, force_list)

    def get(self, item,default=None):
        """A wrapper around __get_item__ that handles missing keys by returning None.

        This is useful for the :py:class:`Stoner.Folder.DataFolder` class.

        Args:
            item (string): A string representing the metadata keyname

        Keyword Arguments:
            default (any): Default value to return if key not found

        Returns:
            mixed: self.metadata[item] or None if item not in self.metadata
        """
        try:
            return self[item]
        except KeyError:
            return default

    def get_filename(self, mode):
        """Forces the user to choose a new filename using a system dialog box.

        Args:
            mode (string): The mode of file operation to be used when calling the dialog box

        Returns:
            str: The new filename

        Note:
            The filename attribute of the current instance is updated by this method as well.
        """
        self.filename = self.__file_dialog(mode)
        return self.filename

    def insert_rows(self, row, new_data):
        """Insert new_data into the data array at position row. This is a wrapper for numpy.insert.

        Args:
            row (int):  Data row to insert into
            new_data (numpy array): An array with an equal number of columns as the main data array containing the new row(s) of data to insert

        Returns:
            self: A copy of the modified :py:class:`DataFile` object
        """
        self.data = _np_.insert(self.data, row, new_data, 0)
        return self

    def keys(self):
        """An alias for :py:meth:`DataFile.dir(None)` .

        Returns:
            a list of all the keys in the metadata dictionary
        """
        return self.dir(None)

    def load(self, filename=None, auto_load=True, filetype=None, *args, **kargs):
        """Loads the :py:class:`DataFile` in from disc guessing a better subclass if necessary.

        Args:
            filename (string or None): path to file to load

        Keyword Arguments:
            auto_load (bool): If True (default) then the load routine tries all the subclasses of :py:class:`DataFile` in turn to load the file
            filetype (:py:class:`DataFile`): If not none then tries using filetype as the loader

        Returns:
            DataFile: A copy of the loaded :py:data:`DataFile` instance

        Note:
            Possible subclasses to try and load from are identified at run time using the speciall :py:attr:`DataFile.subclasses` attribute.

            Some subclasses can be found in the :py:mod:`Stoner.FileFormats` module.

            Each subclass is scanned in turn for a class attribute priority which governs the order in which they are tried. Subclasses which can
            make an early positive determination that a file has the correct format can have higher priority levels. Classes should return
            a suitable expcetion if they fail to load the file.

            If not class can load a file successfully then a RunttimeError exception is raised.
        """
        if filename is None or (isinstance(filename, bool) and not filename):
            filename = self.__file_dialog('r')
        else:
            self.filename = filename

        if not path.exists(self.filename):
            raise IOError("Cannot find {} to load".format(self.filename))
        if filemagic is not None:
            with filemagic(flags=MAGIC_MIME_TYPE) as m:
                mimetype=m.id_filename(filename)
            if self.debug:
                print("Mimetype:{}".format(mimetype))
        cls = self.__class__
        failed = True
        if auto_load:  # We're going to try every subclass we canA
            for cls in self.subclasses.values():
                if self.debug: print(cls.__name__)
                try:
                    if filemagic is not None and mimetype not in cls.mime_type: #short circuit for non-=matching mime-types
                        if self.debug: print("Skipping {} due to mismatcb mime type {}".format(cls.__name__,cls.mime_type))
                        continue
                    test = cls()
                    if self.debug and filemagic is not None:
                        print("Trying: {} =mimetype {}".format(cls.__name__,test.mime_type))

                    kargs.pop("auto_load",None)
                    test._load(self.filename,auto_load=False,*args,**kargs)
                    if self.debug: print("Passed Load")
                    failed=False
                    test["Loaded as"]=cls.__name__
                    if (self.debug): print("Test matadata: {}".format(test.metadata))
                    copy_into(test,self)
                    if (self.debug): print("Self matadata: {}".format(self.metadata))

                    break
                except StonerLoadError as e:
                    if self.debug: print("Failed Load: {}".format(e))
                    continue
                except UnicodeDecodeError as e:
                    print("{} Failed with a uncicode decode error for {}\n{}".format(cls,filename,format_exc()))
                    continue
            else:
                raise IOError("Ran out of subclasses to try and load {} as. Recognised filetype are:{}".format(filename,list(self.subclasses.keys())))
        else:
            if filetype is None:
                test = cls()
                test._load(self.filename,*args,**kargs)
                self["Loaded as"] = cls.__name__
                self.data = test.data
                self.metadata.update(test.metadata)
                failed = False
            elif issubclass(filetype, DataFile):
                test = filetype()
                test._load(self.filename,*args,**kargs)
                self["Loaded as"] = filetype.__name__
                self.data = test.data
                self.metadata.update(test.metadata)
                self.column_headers=test.column_headers
                failed = False
            elif isinstance(filetype, DataFile):
                test = filetype.clone
                test._load(self.filename,*args,**kargs)
                self["Loaded as"] = filetype.__name__
                self.data = test.data
                self.metadata.update(test.metadata)
                self.column_headers=test.column_headers
                failed = False

        if failed:
            raise SyntaxError("Failed to load file")
        for k,i in kargs.items():
            if not callable(getattr(self,k,lambda x:False)):
                setattr(self,k,i)
        return self

    def rename(self, old_col, new_col):
        """Renames columns without changing the underlying data.

        Args:
            old_col (string, int, re):  Old column index or name (using standard rules)
            new_col (string): New name of column

        Returns:
            self: A copy of the modified :py:class:`DataFile` instance
        """
        old_col = self.find_col(old_col)
        self.column_headers[old_col] = new_col
        return self

    def reorder_columns(self, cols, headers_too=True,setas_too=True):
        """Construct a new data array from the original data by assembling the columns in the order given.

        Args:
            cols (list of column indices): (referred to the oriignal
                data set) from which to assemble the new data set
            headers_too (bool): Reorder the column headers in the same
                way as the data (defaults to True)
            setas_too (bool): Reorder the column assignments in the same
                way as the data (defaults to True)

        Returns:
            self: A copy of the modified :py:class:`DataFile` object
        """
        if headers_too:
            column_headers = [self.column_headers[self.find_col(x)] for x in cols]
        else:
            column_headers=self.column_headers
        if setas_too:
            setas = [self.setas[self.find_col(x)] for x in cols]
        else:
            setas=self.setas.clone

        newdata = _np_.atleast_2d(self.data[:, self.find_col(cols.pop(0))])
        for col in cols:
            newdata = _np_.append(newdata, _np_.atleast_2d(self.data[:, self.find_col(col)]), axis=0)
        self.data = DataArray(_np_.transpose(newdata))
        self.setas=setas
        self.column_headers=column_headers
        return self

    def rolling_window(self, window=7, wrap=True, exclude_centre=False):
        """Iterator that return a rolling window section of the data.

        Keyword Arguments:
            window (int): Size of the rolling window (must be odd and >= 3)
            wrap (bool): Whether to use data from the other end of the array when at one end or the other.
            exclude_centre (odd int or bool): Exclude the ciurrent row from the rolling window (defaults to False)

        Yields:
            ndarray: Yields with a section of data that is window rows long, each iteration moves the marker
            one row further on.
        """
        if isinstance(exclude_centre, bool) and exclude_centre:
            exclude_centre = 1
        if isinstance(exclude_centre, int_types) and not isinstance(exclude_centre, bool):
            if exclude_centre % 2 == 0:
                raise ValueError("If excluding the centre of the window, this must be an odd number of rows.")
            elif window - exclude_centre < 2 or window < 3 or window % 2 == 0:
                raise ValueError(
                    "Window must be at least two bigger than the number of rows exluded from the centre, bigger than 3 and odd")

        hw = int((window - 1) / 2)
        if exclude_centre:
            hc = int((exclude_centre - 1) / 2)

        for i in range(len(self)):
            if i < hw:
                pre_data = self.data[i - hw:]
            else:
                pre_data = _np_.zeros((0, self.shape[1]))
            if i + 1 > len(self) - hw:
                post_data = self.data[0:hw - (len(self) - i - 1)]
            else:
                post_data = _np_.zeros((0, self.shape[1]))
            starti = max(i - hw, 0)
            stopi = min(len(self), i + hw + 1)
            if exclude_centre: #hacked to stop problems with DataArray concatenation
                tmp=self.clone #copy all properties
                data = _np_.row_stack((self.data[starti:i - hc], self.data[i + 1 + hc:stopi]))
                tmp.data=_np_.array(data) #guarantee an ndarray
                data=tmp.data #get the DataArray
            else:
                data = self.data[starti:stopi]
            if wrap:
                tmp=self.clone #copy all properties
                ret = _np_.row_stack((pre_data, data, post_data))
                tmp.data=_np_.array(ret) #guarantee an ndarray
                ret=tmp.data #get the DataArray
            else:
                ret = data
            yield ret

    def rows(self,not_masked=False):
        """Generator method that will iterate over rows of data

        Keyword Arguments:
            not_masked(bool): If a row is masked and this is true, then don't return this row.

        Yields:
            1D array: Returns the next row of data
        """
        for row in self.data:
            if _ma_.is_masked(row) and not_masked:
                continue
            else:
                yield row

    def save(self, filename=None,**kargs):
        """Saves a string representation of the current DataFile object into the file 'filename'.

        Args:
            filename (string, bool or None): Filename to save data as, if this is
                None then the current filename for the object is used
                If this is not set, then then a file dialog is used. If f
                ilename is False then a file dialog is forced.
            as_loaded (bool,str): If True, then the *Loaded as* key is inspected to see what the original
                class of the DataFile was and then this class' save method is used to save the data. If a str then
                the keyword value is interpreted as the name of a subclass of the the current DataFile.

        Returns:
            self: The current :py:class:`DataFile` object
        """
        as_loaded=kargs.pop("as_loaded",False)
        if filename is None:
            filename = self.filename
        if filename is None or (isinstance(filename, bool) and not filename):
            # now go and ask for one
            filename = self.__file_dialog('w')
        if as_loaded:
            if isinstance(as_loaded,bool) and "Loaded as" in self: # Use the Loaded as key to find a different save routine
                cls=self.subclasses[self["Loaded as"]]  # pylint: disable=unsubscriptable-object
            elif isinstance(as_loaded,string_types) and as_loaded in self.subclasses:  # pylint: disable=unsupported-membership-test
                cls=self.subclasses[as_loaded]  # pylint: disable=unsubscriptable-object
            else:
                raise ValueError("{} cannot be interpreted as a valid sub class of {} so cannot be used to save this data".format(as_loaded,type(self)))
            ret=cls(self).save(filename)
            self.filename=ret.filename
            return self
        # Normalise the extension to ensure it's something we like...
        filename,ext=os.path.splitext(filename)
        if "*.{}".format(ext) not in DataFile.patterns:  # pylint: disable=unsupported-membership-test
            ext=DataFile.patterns[0][2:]  # pylint: disable=unsubscriptable-object
        filename="{}.{}".format(filename,ext)
        header = ["TDI Format 1.5"]
        header.extend(self.column_headers[:self.data.shape[1]])
        header = "\t".join(header)
        mdkeys = sorted(self.metadata)
        if len(mdkeys) > len(self):
            mdremains = mdkeys[len(self):]
            mdkeys = mdkeys[0:len(self)]
        else:
            mdremains = []
        mdtext = _np_.array([self.metadata.export(k) for k in mdkeys])
        if len(mdtext) < len(self):
            mdtext = _np_.append(mdtext, _np_.zeros(len(self) - len(mdtext), dtype=str))
        data_out = _np_.column_stack([mdtext, self.data])
        fmt = ["%s"] * data_out.shape[1]
        with io.open(filename, 'wb') as f:
            _np_.savetxt(f, data_out, fmt=fmt, header=header, delimiter="\t", comments="")
            for k in mdremains:
                t = self.metadata.export(k)
                f.write(str2bytes(self.metadata.export(k) + "\n")) #(str2bytes(self.metadata.export(k) + "\n"))

        self.filename = filename
        return self

    def search(self, xcol, value, columns=None, accuracy=0.0):
        """Searches in the numerica data part of the file for lines that match and returns  the corresponding rows.

        Args:
            xcol (int,string.re) is a Search Column Index
            value (float, tuple, list or callable): Value to look for

        Keyword Arguments:
            columns (index or array of indices or None (default)): columns of data to return - none represents all columns.
            accuracy (float): Uncertainty to accept when testing equalities

        Returns:
            ndarray: numpy array of matching rows or column values depending on the arguements.

        Note:
            The value is interpreted as follows:

            - a float looks for an exact match
            - a list is a list of exact matches
            - a tuple should contain a (min,max) value.
            - A callable object should have accept a float and an array representing the value of
              the search col for the the current row and the entire row.
        """
        ix = self.__search_index(xcol, value, accuracy)
        if columns is None:  #Get the whole slice
            data = self.data[ix,:]
        else:
            columns = self.find_col(columns)
            if not isinstance(columns, list):
                data = self.data[ix, columns]
            else:
                data = self.data[ix, columns[0]]
                for c in columns[1:]:
                    data = _np_.column_stack((data, self.data[ix, c]))
        return data

    def section(self, **kargs):
        """Assuming data has x,y or x,y,z co-ordinates, return data from a section of the parameter space.

        Keyword Arguments:
            x (float, tuple, list or callable): x values ,atch this condition are included inth e section
            y (float, tuple, list  or callable): y values ,atch this condition are included inth e section
            z (float, tuple,list  or callable): z values ,atch this condition are included inth e section
            r (callable): a function that takes a tuple (x,y,z) and returns True if the line is to be incluided in section

        Returns:
            DataFile: A :py:class:`DataFile` like object that includes only those lines from the original that match the section specification

        Internally this function is calling :py:meth:`DataFile.search` to pull out matching sections of the data array.
        To extract a 2D section of the parameter space orthogonal to one axis you just specify a condition on that axis. Specifying
        conditions on two axes will return a line of points along the third axis. The final keyword parameter allows you to select
        data points that lie in an arbitary plane or line. eg::

            d.section(r=lambda x,y,z:abs(2+3*x-2*y)<0.1 and z==2)

        would extract points along the line 2y=3x+2 (note the use of an < operator to avoid floating point rounding errors) where
        the z-co-ordinate is 2.
        """
        cols = self.setas._get_cols()
        tmp = self.clone
        xcol = cols["xcol"] if cols.has_xcol else None
        ycol = cols["ycol"][0] if cols.has_ucol else None
        zcol = cols["zcol"][0] if cols.has_zcol else None

        if "accuracy" in kargs:
            accuracy = kargs["accuracy"]
        else:
            accuracy = 0.0

        if "x" in kargs:
            tmp.data = tmp.search(xcol, kargs.pop("x"), accuracy=accuracy)
        if "y" in kargs:
            tmp.data = tmp.search(ycol, kargs.pop("y"), accuracy=accuracy)
        if "z" in kargs:
            tmp.data = tmp.search(zcol, kargs.pop("z"), accuracy=accuracy)
        if "r" in kargs:
            func = lambda x, r: kargs.pop("r")(r[xcol], r[ycol], r[zcol])
            tmp.data = tmp.search(0, func, accuracy=accuracy)

        if kargs: # Fallback to working with select if nothing else.
            tmp.select(**kargs)
        return tmp

    def select(self,*args, **kargs):
        """Produce a copy of the DataFile with only data rows that match a criteria.

        Args:
            args (various): A single positional argument if present is interpreted as follows:

            * If a callable function is given, the entire row is presented to it.
                If it evaluates True then that row is selected. This allows arbitary select operations
            * If a dict is given, then it and the kargs dictionary are merged and used to select the rows

        Keyword Arguments:
            kargs (various): Arbitary keyword arguments are interpreted as requestion matches against the corresponding
                columns. The keyword argument may have an additional *__operator** appended to it which is interpreted
                as follows:

                - *eq*  value equals argument value (this is the default test for scalar argument)
                - *ne*  value doe not equal argument value
                - *gt*  value doe greater than argument value
                - *lt*  value doe less than argument value
                - *ge*  value doe greater than or equal to argument value
                - *le*  value doe less than or equal to argument value
                - *between*  value lies beween the minimum and maximum values of the arguement (the default test for 2-length tuple arguments)
                - *ibetween*,*ilbetween*,*iubetween* as above but include both,lower or upper values

        Returns:
            (DatFile): a copy the DataFile instance that contains just the matching rows.

        Note:
            if the operator is preceeded by *__not__* then the sense of the test is negated.

            If any of the tests is True, then the row will be selected, so the effect is a logical OR. To
            achieve a logical AND, you can chain two selects together::

                d.select(temp__le=4.2,vti_temp__lt=4.2).select(field_gt=3.0)

            will select rows that have either temp or vti_temp metadata values below 4.2 AND field metadata values greater than 3.

            If you need to select on a row value that ends in an operator word, then append
            *__eq* in the keyword name to force the equality test. If the metadata keys to select on are not valid python identifiers,
            then pass them via the first positional dictionary value.

            There is a "magic" column name "_i" which is interpreted as the row numbers of the data.

        Example
            .. plot:: samples/select_example.py
                :include-source:
                :outname: select
        """
        if len(args)==1:
            if callable(args[0]):
                kargs["__"]=args[0]
            elif isinstance(args[0],dict):
                kargs.update(args[0])
        result=self.clone
        res=_np_.zeros(len(self),dtype=bool)
        for arg in kargs:
            parts=arg.split("__")
            if parts==["",""]:
                func=kargs[arg]
                res=_np_.logical_or(res,_np_.array([func(r) for r in self.data]))
                continue
            if len(parts)==1 or parts[-1] not in operator:
                parts.append("eq")
            if len(parts)>2 and parts[-2]=="not":
                end=-2
                negate=True
            else:
                end=-1
                negate=False
            if parts[0]=="_i":
                res=_np_.logical_or(res,_np_.logical_xor(negate,operator[parts[-1]](self.data.i,kargs[arg])))
            else:
                col="__".join(parts[:end])
                res=_np_.logical_or(res,_np_.logical_xor(negate,operator[parts[-1]](self.column(col),kargs[arg])))
        result.data=self.data[res,:]
        return result

    def sort(self, *order,**kargs):
        """Sorts the data by column name. Sorts in place and returns a copy of the sorted data object for chaining methods.

        Arguments:
            *order (column index or list of indices or callable function): One or more sort order keys.
                If the argument is a callable function then it should take a two tuple arguments and
                return +1,0,-1 depending on whether the first argument is bigger, equal or smaller. Otherwise
                if the argument is interpreted as a column index. If a single argument is supplied, then it may be
                a list of column indices. If no sort orders are supplied then the data is sorted by the :py:attr:`DataFile.setas` attribute
                or if that is not set, then order of the columns in the data.

        Keyword Arguments:
            reverse (boolean): If true, the sorted array isreversed.

        Returns:
            self: A copy of the :py:class:`DataFile` sorted object
        """
        reverse=kargs.pop("reverse",False)
        order=list(order)
        setas=self.setas.clone
        ch=copy.copy(self.column_headers)
        if not order:
            if self.setas.cols["xcol"] is not None:
                order=[self.setas.cols["xcol"]]
            order.extend(self.setas.cols["ycol"])
            order.extend(self.setas.cols["zcol"])
        if not order: # Ok, no setas here then
            order=None
        elif len(order)==1:
            order=order[0]

        if order is None:
            order = list(range(len(self.column_headers)))
        recs = self.records
        if callable(order):
            d = sorted(recs, cmp=order)
        elif isinstance(order,index_types):
            order = [recs.dtype.names[self.find_col(order)]]
            d = _np_.sort(recs, order=order)
        elif isiterable(order):
            order = [recs.dtype.names[self.find_col(x)] for x in order]
            d = _np_.sort(recs, order=order)
        else:
            raise KeyError("Unable to work out how to sort by a {}".format(type(order)))
        self.data = d.view(dtype=self.dtype).reshape(len(self), len(self.column_headers))
        if reverse:
            self.data=self.data[::-1]
        self.data._setas=setas
        self.column_headers=ch
        return self

    def split(self, *args):
        """Recursively splits the current :py:class:`DataFile` object into a :py:class:`Stoner.Forlders.DataFolder` objects where each one contains the rows from the original object which had the same value of a given column(s) or function.

        Args:
            *args (column index or function): Each argument is used in turn to find key values for the files in the DataFolder

        Returns:
            Stoner.Folders.DataFolder: A :py:class:`Stoner.Folders.DataFolder` object containing the individual
            :py:class:`AnalysisMixin` objects

        Note:
            On each iteration the first argument is called. If it is a column type then rows which amtch each unique value are collated
            together and made into a separate file. If the argument is a callable, then it is called for each row, passing the row
            as a single 1D array and the return result is used to group lines together. The return value should be hashable.

            Once this is done and the :py:class:`Stoner.Folders.DataFolder` exists, if there are remaining argument, then the method is
            called recusivelyt for each file and the resulkting DataFolder added into the root DataFolder and the file is removed.

            Thus, when all of the arguments are evaluated, the resulting DataFolder is a multi-level tree.

            .. warning::

                There has been a change in the arguments for the split function  from version 0.8 of the Stoner Package.
        """
        from Stoner import DataFolder
        if not args:
            xcol=self.setas._get_cols("xcol")
        else:
            args=list(args)
            xcol=args.pop(0)
        data=OrderedDict()

        if isinstance(xcol,index_types):
            for val in _np_.unique(self.column(xcol)):
                newfile=self.clone
                newfile.filename="{}={} {}".format(self.column_headers[self.find_col(xcol)],val,self.filename)
                newfile.data=self.search(xcol, val)
                data[val]=newfile
        elif callable(xcol):
            try: # Try to call function with all data in one go
                keys=xcol(self.data)
                if not isiterable(keys) or len(keys)!=len(self):
                    raise RuntimeError("Not returning an index of keys")
            except Exception: #Ok try instead to do it row by row
                keys=[xcol(r) for r in self]
            keys=_np_.array(keys)
            for key in _np_.unique(keys):
                data[key]=self.clone
                data[key].data=self.data[keys==key,:]
                data[key].filename="{}={} {}".format(xcol.__name__,key,self.filename)
                data[key].setas=self.setas
        else:
            raise NotImplementedError("Unable to split a file with an argument of type {}".format(type(xcol)))
        out = DataFolder(nolist=True,setas=self.setas)
        for k,f in data.items():
            if args:
                out.add_group(k)
                out.groups[k]=f.split(*args)
            else:
                out+=f
        return out

    def swap_column(self, *swp,**kargs):
        """Swaps pairs of columns in the data.

        Useful for reordering data for idiot programs that expect columns in a fixed order.

        Args:
            swp  (tuple of list of tuples of two elements): Each
                element will be iused as a column index (using the normal rules
                for matching columns).  The two elements represent the two
                columns that are to be swapped.
            headers_too (bool): Indicates the column headers
                are swapped as well

        Returns:
            self: A copy of the modified :py:class:`DataFile` objects

        Note:
            If swp is a list, then the function is called recursively on each
            element of the list. Thus in principle the @swp could contain
            lists of lists of tuples
        """
        self.data.swap_column(*swp,**kargs)
        return self

    def unique(self, col, return_index=False, return_inverse=False):
        """Return the unique values from the specified column - pass through for numpy.unique.

        Args:
            col (index): Column to look for unique values in

        Keyword Arguments:

        """
        return _np_.unique(self.column(col), return_index, return_inverse)

    #============================================================================================================================
    ############################              Depricated  Methods                ################################################
    #============================================================================================================================

    def __meta__(self, ky):
        """Returns specific items of  metadata.

        This is equivalent to doing DataFile.metadata[key]

        Args:
            ky (string): The name of the metadata item to be returned.

        Returns:
            mixed or None: Returns the item of metadata.

        Note:
           If key is not an exact match for an item of metadata,
            then a regular expression match is carried out.
        """
        if isinstance(ky, string_types):  # Ok we go at it with a string
            if str(ky) in self.metadata:
                ret = self.metadata[str(ky)]
            else:
                test = re.compile(ky)
                ret = self.__regexp_meta__(test)
        elif isinstance(ky, re._pattern_type):
            ret = self.__regexp_meta__(ky)
        else:
            raise TypeError("Only strings and regular expressions  are supported as search keys for metadata")
        return ret

    def __regexp_meta__(self, test):
        """Do a regular expression search for all meta data items.

        Args:
            test (compiled regular expression): Regular expression to test against meta data key names

        Returns:
            Either a single metadata item or a dictionary of metadata items
        """
        possible = [x for x in self.metadata if test.search(x)]
        if not possible:
            raise KeyError("No metadata with keyname: {}".format(test))
        elif len(possible) == 1:
            ret = self.metadata[possible[0]]
        else:
            d = dict()
            for p in possible:
                d[p] = self.metadata[p]
            ret = d
        return ret


# Module level functions


def itersubclasses(cls, _seen=None):
    """Iterate over subclasses of a given class

    Generator over all subclasses of a given class, in depth first order.

    >>> list(itersubclasses(int)) == [bool]
    True
    >>> class A(object): pass
    >>> class B(A): pass
    >>> class C(A): pass
    >>> class D(B,C): pass
    >>> class E(D): pass
    >>>
    >>> for cls in itersubclasses(A):
    ...     print(cls.__name__)
    B
    D
    E
    C
    >>> # get ALL (new-style) classes currently defined
    >>> [cls.__name__ for cls in itersubclasses(object)] #doctest: +ELLIPSIS
    ['type', ...'tuple', ...]
    """
    if not isinstance(cls, type):
        raise TypeError('itersubclasses must be called with ' 'new-style classes, not %.100r' % cls)
    if _seen is None: _seen = set()
    try:
        subs = cls.__subclasses__()
    except TypeError:  # fails only when cls is type
        subs = cls.__subclasses__(cls)
    for sub in subs:
        if sub not in _seen:
            _seen.add(sub)
            yield sub
            for sub in itersubclasses(sub, _seen):
                yield sub