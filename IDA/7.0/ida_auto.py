# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.




"""
IDA Plugin SDK API wrapper: auto
"""


from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ida_auto', [dirname(__file__)])
        except ImportError:
            import _ida_auto
            return _ida_auto
        if fp is not None:
            try:
                _mod = imp.load_module('_ida_auto', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ida_auto = swig_import_helper()
    del swig_import_helper
else:
    import _ida_auto
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
        func.func_dict["bc695redef"] = True
        return func


def get_auto_state(*args):
  """
  get_auto_state() -> atype_t
  """
  return _ida_auto.get_auto_state(*args)

def set_auto_state(*args):
  """
  set_auto_state(new_state) -> atype_t
  """
  return _ida_auto.set_auto_state(*args)
class auto_display_t(object):
    """
    Proxy of C++ auto_display_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    type = _swig_property(_ida_auto.auto_display_t_type_get, _ida_auto.auto_display_t_type_set)
    ea = _swig_property(_ida_auto.auto_display_t_ea_get, _ida_auto.auto_display_t_ea_set)
    state = _swig_property(_ida_auto.auto_display_t_state_get, _ida_auto.auto_display_t_state_set)
    def __init__(self, *args):
        """
        __init__(self) -> auto_display_t
        """
        this = _ida_auto.new_auto_display_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ida_auto.delete_auto_display_t
    __del__ = lambda self : None;
auto_display_t_swigregister = _ida_auto.auto_display_t_swigregister
auto_display_t_swigregister(auto_display_t)
cvar = _ida_auto.cvar
AU_NONE = cvar.AU_NONE
AU_UNK = cvar.AU_UNK
AU_CODE = cvar.AU_CODE
AU_WEAK = cvar.AU_WEAK
AU_PROC = cvar.AU_PROC
AU_TAIL = cvar.AU_TAIL
AU_TRSP = cvar.AU_TRSP
AU_USED = cvar.AU_USED
AU_TYPE = cvar.AU_TYPE
AU_LIBF = cvar.AU_LIBF
AU_LBF2 = cvar.AU_LBF2
AU_LBF3 = cvar.AU_LBF3
AU_CHLB = cvar.AU_CHLB
AU_FINAL = cvar.AU_FINAL
st_Ready = cvar.st_Ready
st_Think = cvar.st_Think
st_Waiting = cvar.st_Waiting
st_Work = cvar.st_Work


def get_auto_display(*args):
  """
  get_auto_display(auto_display)
  """
  return _ida_auto.get_auto_display(*args)

def show_auto(*args):
  """
  show_auto(ea, type=AU_NONE)
  """
  return _ida_auto.show_auto(*args)

def show_addr(*args):
  """
  show_addr(ea)
  """
  return _ida_auto.show_addr(*args)

def set_ida_state(*args):
  """
  set_ida_state(st) -> idastate_t
  """
  return _ida_auto.set_ida_state(*args)

def may_create_stkvars(*args):
  """
  may_create_stkvars() -> bool
  """
  return _ida_auto.may_create_stkvars(*args)

def may_trace_sp(*args):
  """
  may_trace_sp() -> bool
  """
  return _ida_auto.may_trace_sp(*args)

def auto_mark_range(*args):
  """
  auto_mark_range(start, end, type)
  """
  return _ida_auto.auto_mark_range(*args)

def auto_mark(*args):
  """
  auto_mark(ea, type)
  """
  return _ida_auto.auto_mark(*args)

def auto_unmark(*args):
  """
  auto_unmark(start, end, type)
  """
  return _ida_auto.auto_unmark(*args)

def plan_ea(*args):
  """
  plan_ea(ea)
  """
  return _ida_auto.plan_ea(*args)

def plan_range(*args):
  """
  plan_range(sEA, eEA)
  """
  return _ida_auto.plan_range(*args)

def auto_make_code(*args):
  """
  auto_make_code(ea)
  """
  return _ida_auto.auto_make_code(*args)

def auto_make_proc(*args):
  """
  auto_make_proc(ea)
  """
  return _ida_auto.auto_make_proc(*args)

def reanalyze_callers(*args):
  """
  reanalyze_callers(ea, noret)
  """
  return _ida_auto.reanalyze_callers(*args)

def revert_ida_decisions(*args):
  """
  revert_ida_decisions(ea1, ea2)
  """
  return _ida_auto.revert_ida_decisions(*args)

def auto_apply_type(*args):
  """
  auto_apply_type(caller, callee)
  """
  return _ida_auto.auto_apply_type(*args)

def auto_apply_tail(*args):
  """
  auto_apply_tail(tail_ea, parent_ea)
  """
  return _ida_auto.auto_apply_tail(*args)

def plan_and_wait(*args):
  """
  plan_and_wait(ea1, ea2, final_pass=True) -> int
  """
  return _ida_auto.plan_and_wait(*args)

def auto_wait(*args):
  """
  auto_wait() -> bool
  """
  return _ida_auto.auto_wait(*args)

def auto_cancel(*args):
  """
  auto_cancel(ea1, ea2)
  """
  return _ida_auto.auto_cancel(*args)

def auto_is_ok(*args):
  """
  auto_is_ok() -> bool
  """
  return _ida_auto.auto_is_ok(*args)

def peek_auto_queue(*args):
  """
  peek_auto_queue(low_ea, type) -> ea_t
  """
  return _ida_auto.peek_auto_queue(*args)

def auto_get(*args):
  """
  auto_get(type, lowEA, highEA) -> ea_t
  """
  return _ida_auto.auto_get(*args)

def auto_recreate_insn(*args):
  """
  auto_recreate_insn(ea) -> int
  """
  return _ida_auto.auto_recreate_insn(*args)

def is_auto_enabled(*args):
  """
  is_auto_enabled() -> bool
  """
  return _ida_auto.is_auto_enabled(*args)

def enable_auto(*args):
  """
  enable_auto(enable) -> bool
  """
  return _ida_auto.enable_auto(*args)
if _BC695:
    analyze_area = plan_and_wait
    autoCancel = auto_cancel
    autoIsOk = auto_is_ok
    autoMark = auto_mark
    autoUnmark = auto_unmark
    autoWait = auto_wait
    noUsed = plan_ea
    setStat = set_ida_state
    showAddr = show_addr
    showAuto = show_auto



