"""
Base Parser Types for `nc5ng` submodules

.. automodule:: .




"""
import fortranformat as ff
import logging
from os.path import basename, exists, join, isdir, isfile, isabs
from os import listdir



class BaseFileParser(object):
    """ Base Class for File Parsers
    
    
    
    """
    def __init__(self, parser=None, fdir=None, ffile=None):
        self.parser = parser
        self.fdir = fdir
        self.ffile = ffile
        
        

    @property
    def parser(self):
        return self._parser
    @parser.setter
    def parser(self, value):
        self._parser = value

    @property
    def fdir(self):
        return getattr(self, '_fdir', None)

    @fdir.setter
    def fdir(self, value):
        self._fdir = value
        if (value is not None) and not(isabs(value)):
            logging.warning("%s is not an absolute path"%str(value))

    @property
    def ffile(self):
        return self._ffile

    @ffile.setter
    def ffile(self, value):
        self._ffile = value
        

    def __call__(self, it):
        if self.parser and hasattr(self.parser, '__call__'):
            return [self.parser(_line) for _line in it]
        elif self.parser and hasattr(self.parser, 'read'):
            return [self.parser.read(_line) for _line in it]
        else:
            return None

    def __fromfile__(self, f):
        return {'meta': {}, 'data':[ _ for _ in self(f) if _ is not None] }

    def fromfile(self, ffile=None, process=None, fdir=None):
        if ffile is None and self.ffile is not None:
            ffile = self.ffile

        if fdir is None and self.fdir is not None:
            fdir = self.fdir
        
        if (fdir is not None) and (ffile is not None) and  not(isabs(ffile)):
            ffile = join(fdir, ffile)

        with open(ffile,'r') as f:
            res = self.__fromfile__(f)
            res['meta']['source'] = ffile
            return res
        
        return None

class FortranFormatFileParser(BaseFileParser):
    """ FileParser for Fortran Fixed Format Files
    
    :param fformat: fortran format string
    :param ffilter: file pre-filter (exclude/include lines)
    """
    def __init__(self, fformat = None, ffilter = None):
        self._parser = None
        self.fformat = fformat
        self.ffilter = ffilter
        
    @property
    def fformat(self):
        return self._fformat
    
    @fformat.setter
    def fformat(self, value):
        self._fformat = value
        if self._fformat:
            self._parser = ff.FortranRecordReader(self._fformat)

    @property
    def ffilter(self):
        return self._ffilter

    @ffilter.setter
    def ffilter(self, value):
        if value is None:
            self._ffilter = lambda x: x
        else:
            self._ffilter = value            
    
    def __call__(self, it):
        if self._parser:
            return [ self._ffilter( self._parser.read(_line) ) for _line in it ]
    
        

class IndexedFortranFormatFileParser(FortranFormatFileParser):
    """ Extentsion for FortranFileParser that allows classes to 
    switch between pre-registered formats by index

    :param args: Either list of ``[format1,filter1],[format2,filter2],...`` or serial list ``format1, filter1, format2, filter2, ...``
    :param kwargs: Keyword argument dictionary  ``index:[format,filter]``, dictionary key used for indexing file parser
    """

    def __init__(self, *args, **kwargs):
        super().__init__()
        self._running_index=0
        self._index=0
        self.indexed_format = {}
        
        for entry in args:
            try:
                fformat,ffilter = entry
            except TypeException:
                fformat = args.pop(0)
                if args: ffilter = args.pop(0)
                else: ffilter=None
            self._register_format(fformat, ffilter)
        for index, entry in kwargs.items():
            try:
                fformat, ffilter = entry
            except TypeException:
                fformat = entry
                ffilter = None
            self._register_format(fformat, ffilter, index)
        self.index=0

    def _register_format(self, fformat, ffilter=None, index = None, overwrite=False):
        if index is None:
            index = self._running_index
            self.fformat = fformat
            self._running_index = self._running_index + 1

        if (index not in self.indexed_format or overwrite):
            self.indexed_format[index]=(fformat,ffilter)
            if (index == self.index):
                self.index = index # reload filters
            return index
        else:
            return None

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, index=None):
        if index in self.indexed_format:
            fformat, ffilter = self.indexed_format[index]
            self.fformat = fformat
            self.ffilter = ffilter
            self._index = index
        else:
            pass
        
    def __getitem__(self,index):
        if index in self.indexed_format:
            return FortranFormatFileParser(*self.indexed_format[index])
        else:
            return None

    def __contains__(self, value):
        return index in self.indexed_format

    def __call__(self, it, index=None):        
        if index is None or index == self.index:
            return super().__call__(it)
        elif index in self:
            return p(it)
        else:
            return None
