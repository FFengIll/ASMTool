# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.




"""
IDA Plugin SDK API wrapper: loader
"""


from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ida_loader', [dirname(__file__)])
        except ImportError:
            import _ida_loader
            return _ida_loader
        if fp is not None:
            try:
                _mod = imp.load_module('_ida_loader', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ida_loader = swig_import_helper()
    del swig_import_helper
else:
    import _ida_loader
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


import ida_idaapi

import sys
_BC695 = sys.modules["__main__"].IDAPYTHON_COMPAT_695_API

if _BC695:






    def bc695redef(func):
        ida_idaapi._BC695.replace_fun(func)
        return func

class qvector_snapshotvec_t(object):
    """
    Proxy of C++ qvector<(p.snapshot_t)> class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args):
        """
        __init__(self) -> qvector_snapshotvec_t
        __init__(self, x) -> qvector_snapshotvec_t
        """
        this = _ida_loader.new_qvector_snapshotvec_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ida_loader.delete_qvector_snapshotvec_t
    __del__ = lambda self : None;
    def push_back(self, *args):
        """
        push_back(self, x)
        push_back(self) -> snapshot_t *&
        """
        return _ida_loader.qvector_snapshotvec_t_push_back(self, *args)

    def pop_back(self, *args):
        """
        pop_back(self)
        """
        return _ida_loader.qvector_snapshotvec_t_pop_back(self, *args)

    def size(self, *args):
        """
        size(self) -> size_t
        """
        return _ida_loader.qvector_snapshotvec_t_size(self, *args)

    def empty(self, *args):
        """
        empty(self) -> bool
        """
        return _ida_loader.qvector_snapshotvec_t_empty(self, *args)

    def qclear(self, *args):
        """
        qclear(self)
        """
        return _ida_loader.qvector_snapshotvec_t_qclear(self, *args)

    def clear(self, *args):
        """
        clear(self)
        """
        return _ida_loader.qvector_snapshotvec_t_clear(self, *args)

    def resize(self, *args):
        """
        resize(self, _newsize, x)
        resize(self, _newsize)
        """
        return _ida_loader.qvector_snapshotvec_t_resize(self, *args)

    def capacity(self, *args):
        """
        capacity(self) -> size_t
        """
        return _ida_loader.qvector_snapshotvec_t_capacity(self, *args)

    def reserve(self, *args):
        """
        reserve(self, cnt)
        """
        return _ida_loader.qvector_snapshotvec_t_reserve(self, *args)

    def truncate(self, *args):
        """
        truncate(self)
        """
        return _ida_loader.qvector_snapshotvec_t_truncate(self, *args)

    def swap(self, *args):
        """
        swap(self, r)
        """
        return _ida_loader.qvector_snapshotvec_t_swap(self, *args)

    def extract(self, *args):
        """
        extract(self) -> snapshot_t **
        """
        return _ida_loader.qvector_snapshotvec_t_extract(self, *args)

    def inject(self, *args):
        """
        inject(self, s, len)
        """
        return _ida_loader.qvector_snapshotvec_t_inject(self, *args)

    def __eq__(self, *args):
        """
        __eq__(self, r) -> bool
        """
        return _ida_loader.qvector_snapshotvec_t___eq__(self, *args)

    def __ne__(self, *args):
        """
        __ne__(self, r) -> bool
        """
        return _ida_loader.qvector_snapshotvec_t___ne__(self, *args)

    def begin(self, *args):
        """
        begin(self) -> qvector< snapshot_t * >::iterator
        begin(self) -> qvector< snapshot_t * >::const_iterator
        """
        return _ida_loader.qvector_snapshotvec_t_begin(self, *args)

    def end(self, *args):
        """
        end(self) -> qvector< snapshot_t * >::iterator
        end(self) -> qvector< snapshot_t * >::const_iterator
        """
        return _ida_loader.qvector_snapshotvec_t_end(self, *args)

    def insert(self, *args):
        """
        insert(self, it, x) -> qvector< snapshot_t * >::iterator
        """
        return _ida_loader.qvector_snapshotvec_t_insert(self, *args)

    def erase(self, *args):
        """
        erase(self, it) -> qvector< snapshot_t * >::iterator
        erase(self, first, last) -> qvector< snapshot_t * >::iterator
        """
        return _ida_loader.qvector_snapshotvec_t_erase(self, *args)

    def find(self, *args):
        """
        find(self, x) -> qvector< snapshot_t * >::iterator
        find(self, x) -> qvector< snapshot_t * >::const_iterator
        """
        return _ida_loader.qvector_snapshotvec_t_find(self, *args)

    def has(self, *args):
        """
        has(self, x) -> bool
        """
        return _ida_loader.qvector_snapshotvec_t_has(self, *args)

    def add_unique(self, *args):
        """
        add_unique(self, x) -> bool
        """
        return _ida_loader.qvector_snapshotvec_t_add_unique(self, *args)

    def _del(self, *args):
        """
        _del(self, x) -> bool
        """
        return _ida_loader.qvector_snapshotvec_t__del(self, *args)

    def __len__(self, *args):
        """
        __len__(self) -> size_t
        """
        return _ida_loader.qvector_snapshotvec_t___len__(self, *args)

    def __getitem__(self, *args):
        """
        __getitem__(self, i) -> snapshot_t
        """
        return _ida_loader.qvector_snapshotvec_t___getitem__(self, *args)

    def __setitem__(self, *args):
        """
        __setitem__(self, i, v)
        """
        return _ida_loader.qvector_snapshotvec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator

    def at(self, *args):
        """
        at(self, n) -> snapshot_t
        """
        return _ida_loader.qvector_snapshotvec_t_at(self, *args)

qvector_snapshotvec_t_swigregister = _ida_loader.qvector_snapshotvec_t_swigregister
qvector_snapshotvec_t_swigregister(qvector_snapshotvec_t)

class loader_t(object):
    """
    Proxy of C++ loader_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    version = _swig_property(_ida_loader.loader_t_version_get, _ida_loader.loader_t_version_set)
    flags = _swig_property(_ida_loader.loader_t_flags_get, _ida_loader.loader_t_flags_set)
    def __init__(self, *args):
        """
        __init__(self) -> loader_t
        """
        this = _ida_loader.new_loader_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ida_loader.delete_loader_t
    __del__ = lambda self : None;
loader_t_swigregister = _ida_loader.loader_t_swigregister
loader_t_swigregister(loader_t)
LDRF_RELOAD = _ida_loader.LDRF_RELOAD
"""
loader recognizes 'NEF_RELOAD' flag
"""
LDRF_REQ_PROC = _ida_loader.LDRF_REQ_PROC
"""
Requires a processor to be set. if this bit is not set, load_file()
must call set_processor_type(..., SETPROC_LOADER)
"""
ACCEPT_ARCHIVE = _ida_loader.ACCEPT_ARCHIVE
"""
Specify that a file format is served by archive loader See
'loader_t::accept_file'
"""
ACCEPT_CONTINUE = _ida_loader.ACCEPT_CONTINUE
"""
Specify that the function must be called another time See
'loader_t::accept_file'
"""
ACCEPT_FIRST = _ida_loader.ACCEPT_FIRST
"""
Specify that a file format should be place first in "load file" dialog
box. See 'loader_t::accept_file'
"""
NEF_SEGS = _ida_loader.NEF_SEGS
"""
Create segments.
"""
NEF_RSCS = _ida_loader.NEF_RSCS
"""
Load resources.
"""
NEF_NAME = _ida_loader.NEF_NAME
"""
Rename entries.
"""
NEF_MAN = _ida_loader.NEF_MAN
"""
Manual load.
"""
NEF_FILL = _ida_loader.NEF_FILL
"""
Fill segment gaps.
"""
NEF_IMPS = _ida_loader.NEF_IMPS
"""
Create import segment.
"""
NEF_FIRST = _ida_loader.NEF_FIRST
"""
into the database.

This is the first file loaded
"""
NEF_CODE = _ida_loader.NEF_CODE
"""
load as a code segment

for 'load_binary_file()' :
"""
NEF_RELOAD = _ida_loader.NEF_RELOAD
"""
reload the file at the same place: - don't create segmentsdon't create
fixup infodon't import segmentsetc load only the bytes into the base.
a loader should have 'LDRF_RELOAD' bit set
"""
NEF_FLAT = _ida_loader.NEF_FLAT
"""
Autocreate FLAT group (PE)
"""
NEF_MINI = _ida_loader.NEF_MINI
"""
Create mini database (do not copy segment bytes from the input file;
use only the file header metadata)
"""
NEF_LOPT = _ida_loader.NEF_LOPT
"""
Display additional loader options dialog.
"""
NEF_LALL = _ida_loader.NEF_LALL
"""
Load all segments without questions.
"""

DLLEXT = _ida_loader.DLLEXT
LOADER_DLL = _ida_loader.LOADER_DLL

def load_binary_file(*args):
  """
  load_binary_file(filename, li, _neflags, fileoff, basepara, binoff, nbytes) -> bool


  Load a binary file into the database. This function usually is called
  from ui.
  
  @param filename: the name of input file as is (if the input file is
                   from library, then this is the name from the library)
                   (C++: const char *)
  @param li: loader input source (C++: linput_t *)
  @param _neflags: Load file flags . For the first file, the flag
                   NEF_FIRST  must be set. (C++: ushort)
  @param fileoff: Offset in the input file (C++: qoff64_t)
  @param basepara: Load address in paragraphs (C++: ea_t)
  @param binoff: Load offset (load_address=(basepara<<4)+binoff) (C++:
                 ea_t)
  @param nbytes: Number of bytes to load from the file.   0: up to the
                 end of the file (C++: uint64)
  """
  return _ida_loader.load_binary_file(*args)

def process_archive(*args):
  """
  process_archive(temp_file, li, module_name, neflags, defmember, loader) -> int


  Calls 'loader_t::process_archive()' For parameters and return value
  description look at 'loader_t::process_archive()' . Additional
  parameter:
  
  @param temp_file (C++: qstring  *)
  @param li (C++: linput_t *)
  @param module_name (C++: qstring  *)
  @param neflags (C++: ushort  *)
  @param defmember (C++: const char *)
  @param loader: pointer to  load_info_t  structure. (C++: const
                 load_info_t  *)
  """
  return _ida_loader.process_archive(*args)
OFILE_MAP = _ida_loader.OFILE_MAP
OFILE_EXE = _ida_loader.OFILE_EXE
OFILE_IDC = _ida_loader.OFILE_IDC
OFILE_LST = _ida_loader.OFILE_LST
OFILE_ASM = _ida_loader.OFILE_ASM
OFILE_DIF = _ida_loader.OFILE_DIF

def gen_file(*args):
  """
  gen_file(otype, fp, ea1, ea2, flags) -> int


  Generate an output file. 'OFILE_EXE' :
  
  @param otype: type of output file. (C++: ofile_type_t)
  @param fp: the output file handle (C++: FILE *)
  @param ea1: start address. For some file types this argument is
              ignored (C++: ea_t)
  @param ea2: end address. For some file types this argument is ignored
              as usual in ida, the end address of the range is not
              included (C++: ea_t)
  @param flags: Generate file flags (C++: int)
  @return: number of the generated lines. -1 if an error occurred
  """
  return _ida_loader.gen_file(*args)
GENFLG_MAPSEG = _ida_loader.GENFLG_MAPSEG
"""
 'OFILE_MAP' : generate map of segments
"""
GENFLG_MAPNAME = _ida_loader.GENFLG_MAPNAME
"""
 'OFILE_MAP' : include dummy names
"""
GENFLG_MAPDMNG = _ida_loader.GENFLG_MAPDMNG
"""
 'OFILE_MAP' : demangle names
"""
GENFLG_MAPLOC = _ida_loader.GENFLG_MAPLOC
"""
 'OFILE_MAP' : include local names
"""
GENFLG_IDCTYPE = _ida_loader.GENFLG_IDCTYPE
"""
 'OFILE_IDC' : gen only information about types
"""
GENFLG_ASMTYPE = _ida_loader.GENFLG_ASMTYPE
"""
 'OFILE_ASM' , 'OFILE_LST' : gen information about types too
"""
GENFLG_GENHTML = _ida_loader.GENFLG_GENHTML
"""
 'OFILE_ASM' , 'OFILE_LST' : generate html ( 'ui_genfile_callback'
will be used)
"""
GENFLG_ASMINC = _ida_loader.GENFLG_ASMINC
"""
 'OFILE_ASM' , 'OFILE_LST' : gen information only about types
"""

def file2base(*args):
  """
  file2base(li, pos, ea1, ea2, patchable) -> int


  Load portion of file into the database. This function will include
  (ea1..ea2) into the addressing space of the program (make it enabled)
  
  @param li: pointer of input source (C++: linput_t *)
  @param pos: position in the file (C++: qoff64_t)
  @param ea1: range of destination linear addresses (C++: ea_t)
  @param ea2: range of destination linear addresses (C++: ea_t)
  @param patchable: should the kernel remember correspondence of file
                    offsets to linear addresses. (C++: int)
  """
  return _ida_loader.file2base(*args)
FILEREG_PATCHABLE = _ida_loader.FILEREG_PATCHABLE
"""
means that the input file may be patched (i.e. no compression, no
iterated data, etc)
"""
FILEREG_NOTPATCHABLE = _ida_loader.FILEREG_NOTPATCHABLE
"""
form in the file.

the data is kept in some encoded
"""

def base2file(*args):
  """
  base2file(fp, pos, ea1, ea2) -> int


  Unload database to a binary file. This function works for wide byte
  processors too.
  
  @param fp: pointer to file (C++: FILE *)
  @param pos: position in the file (C++: qoff64_t)
  @param ea1: range of source linear addresses (C++: ea_t)
  @param ea2: range of source linear addresses (C++: ea_t)
  @return: 1-ok(always), write error leads to immediate exit
  """
  return _ida_loader.base2file(*args)

def extract_module_from_archive(*args):
  """
  extract_module_from_archive(filename, bufsize, temp_file_ptr, is_remote) -> bool


  Extract a module for an archive file. Parse an archive file, show the
  list of modules to the user, allow him to select a module, extract the
  selected module to a file (if the extract module is an archive, repeat
  the process). This function can handle ZIP, AR, AIXAR, OMFLIB files.
  The temporary file will be automatically deleted by IDA at the end.
  
  @param filename: in: input file. out: name of the selected module.
                   (C++: char *)
  @param bufsize: size of the buffer with 'filename' (C++: size_t)
  @param temp_file_ptr: will point to the name of the file that contains
                        the extracted module (C++: char **)
  @param is_remote: is the input file remote? (C++: bool)
  """
  return _ida_loader.extract_module_from_archive(*args)

def get_basic_file_type(*args):
  """
  get_basic_file_type(li) -> filetype_t


  Get the input file type. This function can recognize libraries and zip
  files.
  
  @param li (C++: linput_t *)
  """
  return _ida_loader.get_basic_file_type(*args)

def get_file_type_name(*args):
  """
  get_file_type_name() -> size_t


  Get name of the current file type. The current file type is kept in
  {filetype}.
  
  @return: size of answer, this function always succeeds
  """
  return _ida_loader.get_file_type_name(*args)

def load_ids_module(*args):
  """
  load_ids_module(fname) -> int


  Load and apply IDS file. This function loads the specified IDS file
  and applies it to the database. If the program imports functions from
  a module with the same name as the name of the ids file being loaded,
  then only functions from this module will be affected. Otherwise (i.e.
  when the program does not import a module with this name) any function
  in the program may be affected.
  
  @param fname: name of file to apply (C++: char *)
  """
  return _ida_loader.load_ids_module(*args)

def get_plugin_options(*args):
  """
  get_plugin_options(plugin) -> char const *


  Get plugin options from the command line. If the user has specified
  the options in the -Oplugin_name:options format, them this function
  will return the 'options' part of it The 'plugin' parameter should
  denote the plugin name Returns NULL if there we no options specified
  
  @param plugin (C++: const char *)
  """
  return _ida_loader.get_plugin_options(*args)
PLUGIN_DLL = _ida_loader.PLUGIN_DLL
"""
Pattern to find plugin files.
"""
MODULE_ENTRY_LOADER = _ida_loader.MODULE_ENTRY_LOADER
MODULE_ENTRY_PLUGIN = _ida_loader.MODULE_ENTRY_PLUGIN
MODULE_ENTRY_IDP = _ida_loader.MODULE_ENTRY_IDP
class idp_name_t(object):
    """
    Proxy of C++ idp_name_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    lname = _swig_property(_ida_loader.idp_name_t_lname_get, _ida_loader.idp_name_t_lname_set)
    sname = _swig_property(_ida_loader.idp_name_t_sname_get, _ida_loader.idp_name_t_sname_set)
    hidden = _swig_property(_ida_loader.idp_name_t_hidden_get, _ida_loader.idp_name_t_hidden_set)
    def __init__(self, *args):
        """
        __init__(self) -> idp_name_t
        """
        this = _ida_loader.new_idp_name_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ida_loader.delete_idp_name_t
    __del__ = lambda self : None;
idp_name_t_swigregister = _ida_loader.idp_name_t_swigregister
idp_name_t_swigregister(idp_name_t)

class idp_desc_t(object):
    """
    Proxy of C++ idp_desc_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    path = _swig_property(_ida_loader.idp_desc_t_path_get, _ida_loader.idp_desc_t_path_set)
    mtime = _swig_property(_ida_loader.idp_desc_t_mtime_get, _ida_loader.idp_desc_t_mtime_set)
    family = _swig_property(_ida_loader.idp_desc_t_family_get, _ida_loader.idp_desc_t_family_set)
    names = _swig_property(_ida_loader.idp_desc_t_names_get, _ida_loader.idp_desc_t_names_set)
    is_script = _swig_property(_ida_loader.idp_desc_t_is_script_get, _ida_loader.idp_desc_t_is_script_set)
    checked = _swig_property(_ida_loader.idp_desc_t_checked_get, _ida_loader.idp_desc_t_checked_set)
    def __init__(self, *args):
        """
        __init__(self) -> idp_desc_t
        """
        this = _ida_loader.new_idp_desc_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ida_loader.delete_idp_desc_t
    __del__ = lambda self : None;
idp_desc_t_swigregister = _ida_loader.idp_desc_t_swigregister
idp_desc_t_swigregister(idp_desc_t)

IDP_DLL = _ida_loader.IDP_DLL
class plugin_info_t(object):
    """
    Proxy of C++ plugin_info_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    next = _swig_property(_ida_loader.plugin_info_t_next_get, _ida_loader.plugin_info_t_next_set)
    path = _swig_property(_ida_loader.plugin_info_t_path_get, _ida_loader.plugin_info_t_path_set)
    org_name = _swig_property(_ida_loader.plugin_info_t_org_name_get, _ida_loader.plugin_info_t_org_name_set)
    name = _swig_property(_ida_loader.plugin_info_t_name_get, _ida_loader.plugin_info_t_name_set)
    org_hotkey = _swig_property(_ida_loader.plugin_info_t_org_hotkey_get, _ida_loader.plugin_info_t_org_hotkey_set)
    hotkey = _swig_property(_ida_loader.plugin_info_t_hotkey_get, _ida_loader.plugin_info_t_hotkey_set)
    arg = _swig_property(_ida_loader.plugin_info_t_arg_get, _ida_loader.plugin_info_t_arg_set)
    entry = _swig_property(_ida_loader.plugin_info_t_entry_get, _ida_loader.plugin_info_t_entry_set)
    dllmem = _swig_property(_ida_loader.plugin_info_t_dllmem_get, _ida_loader.plugin_info_t_dllmem_set)
    flags = _swig_property(_ida_loader.plugin_info_t_flags_get, _ida_loader.plugin_info_t_flags_set)
    comment = _swig_property(_ida_loader.plugin_info_t_comment_get, _ida_loader.plugin_info_t_comment_set)
    def __init__(self, *args):
        """
        __init__(self) -> plugin_info_t
        """
        this = _ida_loader.new_plugin_info_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ida_loader.delete_plugin_info_t
    __del__ = lambda self : None;
plugin_info_t_swigregister = _ida_loader.plugin_info_t_swigregister
plugin_info_t_swigregister(plugin_info_t)


def find_plugin(*args):
  """
  find_plugin(name, load_if_needed=False) -> plugin_t *


  Find a user-defined plugin and optionally load it.
  
  @param name: short plugin name without path and extension, or absolute
               path to the file name (C++: const char *)
  @param load_if_needed: if the plugin is not present in the memory, try
                         to load it (C++: bool)
  @return: pointer to plugin description block
  """
  return _ida_loader.find_plugin(*args)

def get_fileregion_offset(*args):
  """
  get_fileregion_offset(ea) -> qoff64_t


  Get offset in the input file which corresponds to the given ea. If the
  specified ea can't be mapped into the input file offset, return -1.
  
  @param ea (C++: ea_t)
  """
  return _ida_loader.get_fileregion_offset(*args)

def get_fileregion_ea(*args):
  """
  get_fileregion_ea(offset) -> ea_t


  Get linear address which corresponds to the specified input file
  offset. If can't be found, return 'BADADDR'
  
  @param offset (C++: qoff64_t)
  """
  return _ida_loader.get_fileregion_ea(*args)

def gen_exe_file(*args):
  """
  gen_exe_file(fp) -> int


  Generate an exe file (unload the database in binary form).
  
  @param fp (C++: FILE *)
  @return: fp the output file handle. if fp == NULL then return:   1:
           can generate an executable file 0: can't generate an
           executable file
  """
  return _ida_loader.gen_exe_file(*args)

def reload_file(*args):
  """
  reload_file(file, is_remote) -> int


  Reload the input file. This function reloads the byte values from the
  input file. It doesn't modify the segmentation, names, comments, etc.
  
  @param file: name of the input file. if file == NULL then returns:
               1: can reload the input file 0: can't reload the input
               file (C++: const char *)
  @param is_remote: is the file located on a remote computer with the
                    debugger server? (C++: bool)
  """
  return _ida_loader.reload_file(*args)
MAX_DATABASE_DESCRIPTION = _ida_loader.MAX_DATABASE_DESCRIPTION
"""
Maximum database snapshot description length.
"""
class snapshot_t(object):
    """
    Proxy of C++ snapshot_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    id = _swig_property(_ida_loader.snapshot_t_id_get, _ida_loader.snapshot_t_id_set)
    flags = _swig_property(_ida_loader.snapshot_t_flags_get, _ida_loader.snapshot_t_flags_set)
    desc = _swig_property(_ida_loader.snapshot_t_desc_get, _ida_loader.snapshot_t_desc_set)
    filename = _swig_property(_ida_loader.snapshot_t_filename_get, _ida_loader.snapshot_t_filename_set)
    children = _swig_property(_ida_loader.snapshot_t_children_get, _ida_loader.snapshot_t_children_set)
    def __eq__(self, *args):
        """
        __eq__(self, r) -> bool
        """
        return _ida_loader.snapshot_t___eq__(self, *args)

    def __ne__(self, *args):
        """
        __ne__(self, r) -> bool
        """
        return _ida_loader.snapshot_t___ne__(self, *args)

    def __lt__(self, *args):
        """
        __lt__(self, r) -> bool
        """
        return _ida_loader.snapshot_t___lt__(self, *args)

    def __gt__(self, *args):
        """
        __gt__(self, r) -> bool
        """
        return _ida_loader.snapshot_t___gt__(self, *args)

    def __le__(self, *args):
        """
        __le__(self, r) -> bool
        """
        return _ida_loader.snapshot_t___le__(self, *args)

    def __ge__(self, *args):
        """
        __ge__(self, r) -> bool
        """
        return _ida_loader.snapshot_t___ge__(self, *args)

    def clear(self, *args):
        """
        clear(self)
        """
        return _ida_loader.snapshot_t_clear(self, *args)

    def __init__(self, *args):
        """
        __init__(self) -> snapshot_t
        """
        this = _ida_loader.new_snapshot_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ida_loader.delete_snapshot_t
    __del__ = lambda self : None;
snapshot_t_swigregister = _ida_loader.snapshot_t_swigregister
snapshot_t_swigregister(snapshot_t)
SSF_AUTOMATIC = _ida_loader.SSF_AUTOMATIC
"""
automatic snapshot
"""


def build_snapshot_tree(*args):
  """
  build_snapshot_tree(root) -> bool


  Build the snapshot tree.
  
  @param root: snapshot root that will contain the snapshot tree
               elements. (C++: snapshot_t  *)
  @return: success
  """
  return _ida_loader.build_snapshot_tree(*args)
SSUF_DESC = _ida_loader.SSUF_DESC
"""
Update the description.
"""
SSUF_PATH = _ida_loader.SSUF_PATH
"""
Update the path.
"""
SSUF_FLAGS = _ida_loader.SSUF_FLAGS
"""
Update the flags.
"""

def flush_buffers(*args):
  """
  flush_buffers() -> int


  Flush buffers to the disk.
  """
  return _ida_loader.flush_buffers(*args)

def is_trusted_idb(*args):
  """
  is_trusted_idb() -> bool


  Is the database considered as trusted?
  """
  return _ida_loader.is_trusted_idb(*args)

def save_database(*args):
  """
  save_database(outfile, flags, root=None, attr=None) -> bool


  Save current database using a new file name.when both root and attr
  are not NULL then the snapshot attributes will be updated, otherwise
  the snapshot attributes will be inherited from the current database.
  
  @param outfile: output database file name (C++: const char *)
  @param flags: Database flags (C++: uint32)
  @param root: optional: snapshot tree root. (C++: const  snapshot_t  *)
  @param attr: optional: snapshot attributes (C++: const  snapshot_t  *)
  @return: success
  """
  return _ida_loader.save_database(*args)
DBFL_KILL = _ida_loader.DBFL_KILL
"""
delete unpacked database
"""
DBFL_COMP = _ida_loader.DBFL_COMP
"""
collect garbage
"""
DBFL_BAK = _ida_loader.DBFL_BAK
"""
create backup file (if !DBFL_KILL)
"""
DBFL_TEMP = _ida_loader.DBFL_TEMP
"""
temporary database
"""

def is_database_flag(*args):
  """
  is_database_flag(dbfl) -> bool


  Get the current database flag
  
  @param dbfl: flag  Database flags (C++: uint32)
  @return: the state of the flag (set or cleared)
  """
  return _ida_loader.is_database_flag(*args)

def set_database_flag(*args):
  """
  set_database_flag(dbfl, cnd=True)


  Set or clear database flag
  
  @param dbfl: flag  Database flags (C++: uint32)
  @param cnd: set if true or clear flag otherwise (C++: bool)
  """
  return _ida_loader.set_database_flag(*args)

def clr_database_flag(*args):
  """
  clr_database_flag(dbfl)
  """
  return _ida_loader.clr_database_flag(*args)
PATH_TYPE_CMD = _ida_loader.PATH_TYPE_CMD
PATH_TYPE_IDB = _ida_loader.PATH_TYPE_IDB
PATH_TYPE_ID0 = _ida_loader.PATH_TYPE_ID0

def get_path(*args):
  """
  get_path(pt) -> char const *


  Get the file path
  
  @param pt: file path type  Types of the file pathes (C++: path_type_t)
  @return: file path, never returns NULL
  """
  return _ida_loader.get_path(*args)

def set_path(*args):
  """
  set_path(pt, path)


  Set the file path
  
  @param pt: file path type  Types of the file pathes (C++: path_type_t)
  @param path: new file path, use NULL or empty string to clear the file
               path (C++: const char *)
  """
  return _ida_loader.set_path(*args)

def get_elf_debug_file_directory(*args):
  """
  get_elf_debug_file_directory() -> char const *


  Get the value of the ELF_DEBUG_FILE_DIRECTORY configuration directive.
  """
  return _ida_loader.get_elf_debug_file_directory(*args)

def mem2base(*args):
  """
  mem2base(py_mem, ea, fpos=-1) -> int


  Load database from the memory.
  @param mem: the buffer
  @param ea: start linear addresses
  @param fpos: position in the input file the data is taken from.
               if == -1, then no file position correspond to the data.
  @return:
      - Returns zero if the passed buffer was not a string
      - Otherwise 1 is returned
  """
  return _ida_loader.mem2base(*args)

def load_plugin(*args):
  """
  load_plugin(name) -> PyObject *


  Loads a plugin
  @return:
      - None if plugin could not be loaded
      - An opaque object representing the loaded plugin
  """
  return _ida_loader.load_plugin(*args)

def run_plugin(*args):
  """
  run_plugin(plg, arg) -> bool


  Runs a plugin
  @param plg: A plugin object (returned by load_plugin())
  @return: Boolean
  """
  return _ida_loader.run_plugin(*args)

def load_and_run_plugin(*args):
  """
  load_and_run_plugin(name, arg) -> bool


  Load & run a plugin.
  
  
  @param name (C++: const char *)
  @param arg (C++: size_t)
  """
  return _ida_loader.load_and_run_plugin(*args)
if _BC695:
    NEF_TIGHT=0
    @bc695redef
    def save_database(outfile, flags=0):
        if isinstance(flags, bool):
            flags = DBFL_KILL if flags else 0
        return _ida_loader.save_database(outfile, flags)
    save_database_ex=save_database
    MAX_FILE_FORMAT_NAME=64



