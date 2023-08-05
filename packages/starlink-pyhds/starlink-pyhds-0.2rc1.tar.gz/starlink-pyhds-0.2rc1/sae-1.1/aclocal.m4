# generated automatically by aclocal 1.14.1-starlink -*- Autoconf -*-

# Copyright (C) 1996-2013 Free Software Foundation, Inc.

# This file is free software; the Free Software Foundation
# gives unlimited permission to copy and/or distribute it,
# with or without modifications, as long as this notice is preserved.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, to the extent permitted by law; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.

m4_ifndef([AC_CONFIG_MACRO_DIRS], [m4_defun([_AM_CONFIG_MACRO_DIRS], [])m4_defun([AC_CONFIG_MACRO_DIRS], [_AM_CONFIG_MACRO_DIRS($@)])])
m4_ifndef([AC_AUTOCONF_VERSION],
  [m4_copy([m4_PACKAGE_VERSION], [AC_AUTOCONF_VERSION])])dnl
m4_if(m4_defn([AC_AUTOCONF_VERSION]), [2.69],,
[m4_warning([this file was generated for autoconf 2.69.
You have another version of autoconf.  It may work, but is not guaranteed to.
If you have problems, you may need to regenerate the build system entirely.
To do so, use the procedure documented by the package, typically 'autoreconf'.])])

# -*- mode: m4 -*-
# Starlink M4 macros for autoconf
# original starconf.m4, installed by starconf 1.3, rnum=1003000
# DO NOT EDIT: it may be overwritten when starconf is next run

#  Copyright:
#     Copyright (C) 2003-2005 Council for the Central Laboratory of the
#     Research Councils
#
#  Licence:
#     This program is free software; you can redistribute it and/or
#     modify it under the terms of the GNU General Public Licence as
#     published by the Free Software Foundation; either version 2 of
#     the Licence, or (at your option) any later version.
#
#     This program is distributed in the hope that it will be
#     useful,but WITHOUT ANY WARRANTY; without even the implied
#     warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#     PURPOSE. See the GNU General Public Licence for more details.
#
#     You should have received a copy of the GNU General Public Licence
#     along with this program; if not, write to the Free Software
#     Foundation, Inc., 51 Franklin Street,Fifth Floor, Boston, MA
#     02110-1301, USA

# STAR_DEFAULTS(options='')
# -------------------------
# Defaults for Starlink configure.ac files.  The optional OPTIONS
# argument holds a space-separated list of option keywords, of which
# the only ones at present are `per-package-dirs', which causes
# applications and help to be installed in a package-specific
# directory, and 'docs-only', which indicates that the component contains
# only documentation.
#
# Certain features of this macro are documented in SSN/78, in particular
#   - Sets STARLINK
#   - Sets AM_FCFLAGS, AM_FFLAGS, AM_CFLAGS, AM_LDFLAGS to appropriate values
#   - Sets PACKAGE_VERSION_{MAJOR,MINOR,RELEASE,INTEGER}
# The behaviour of these should not be changed without changing the
# documentation, or without due consideration of the packages which use
# the earlier behaviour.  Everything else is, in principle, private
# (not that that's going to stop folk).
AC_DEFUN([STAR_DEFAULTS],
[##
m4_ifval([$1],
         [AC_FOREACH([Option], [$1],
                     [m4_case(Option,
                              [per-package-dirs], [_star_per_package_dirs=:],
                              [docs-only], [_star_docs_only=:],
                              [AC_FATAL([$0: unrecognised option $1])])
                      ])],
         [])

m4_define([per_dir_PREFIX],   [m4_ifdef([OVERRIDE_PREFIX],
                                        [OVERRIDE_PREFIX],
                                        [/star])])
m4_define([per_dir_STARLINK], [m4_ifdef([OVERRIDE_STARLINK],
                                        [OVERRIDE_STARLINK],
                                        [/star])])

test -n "$_star_per_package_dirs" || _star_per_package_dirs=false
test -n "$_star_docs_only"        || _star_docs_only=false


# Ensure that STARLINK has a value, defaulting to
# /star.  Note that this directory may be
# different from /star, and reflects the value of
# STARCONF_DEFAULT_STARLINK that the `starconf' package was configured
# with before its installation. 
#
# We use $STARLINK as the location of any other Starlink tools we need
# to use during the building of our packages, and for the location of
# any manifests we need to check.  It is permissable for it to be
# different from $(prefix): this is partly because we have no way of
# enforcing that the two be the same, since the user can set
# prefix=xxx on the `make install' command line, and partly so that it
# is possible to make a test version of a new package, using tools
# from an old installation, but installing in a new place.
#
# However, we install software in /star by
# default.  This is so even if $STARLINK and STARCONF_DEFAULT_STARLINK
# are different, because in this case we are planning to use a
# previous installation in $STARLINK or $STARCONF_DEFAULT_STARLINK,
# but install the newly built tool elsewhere. 
#
# In most cases, including the most important case where we are
# building the tree from scratch, in a checked out directory,
# STARLINK, STARCONF_DEFAULT_STARLINK and STARCONF_DEFAULT_PREFIX will
# all be the same.  That's OK because a separate aspect of the build
# process, respecting the various dependencies expresses in source
# directories, ensures that we don't use (and install) any Starlink
# tools in one component before that component has been build and
# installed. 

AC_PREFIX_DEFAULT(per_dir_PREFIX)dnl

test -n "$STARLINK" || STARLINK=per_dir_STARLINK

# Handle the --with-starlink option.  If --with-starlink is present
# with no argument (the default), we do nothing as this simply
# indicates that this is part of a Starlink tree.  If it has an
# argument, then this overrides the location of the Starlink tree.
# Option --without-starlink or --with-starlink=no indicates that this
# is being built _not_ as part of a Starlink build (that is, it's
# being distributed as something other than a Starlink package).  In
# this case, the variable STARLINK is unset.
AC_ARG_WITH(starlink,
            AS_HELP_STRING([--with-starlink],
                           [Starlink tree to use (default ${STARLINK:=per_dir_STARLINK})]),
            [if test -z "$withval" -o "$withval" = yes; then
                 : nothing needs to be done
             elif test "X$withval" = Xno; then
                 unset STARLINK
             elif test -d "$withval"; then
                 STARLINK="$withval"
             else
                 AC_MSG_WARN([--with-starlink given nonexistent directory; ignored: using default $STARLINK instead])
             fi])
if test -n "$STARLINK"; then
    AC_MSG_NOTICE([Starlink tree located at $STARLINK])
else
    AC_MSG_NOTICE([Not being built as part of the Starlink tree])
fi

# Handle --without-stardocs.  Don't build and install documentation.
# Default is --with-stardocs.
_star_build_docs=:
AC_ARG_WITH(stardocs,
            AS_HELP_STRING([--without-stardocs],
                           [Do not install built documentation (default --with)]),
            [if test -z "$withval"; then
                 _star_build_docs=: # default
             elif test "X$withval" = Xno; then
                 _star_build_docs=false
             elif test "X$withval" = Xyes; then
                 _star_build_docs=:
             else
                 AC_MSG_WARN([bad arg to --with-stardocs: using yes])
                 _star_build_docs=:
             fi])

if $_star_docs_only; then
    if $_star_build_docs; then
        : OK
    else
        AC_MSG_WARN([Building without documentation in a docs-only directory])
    fi
fi

# Everything depends on where /star is.  Declare STARLINK as a
# `precious variable'.  Amongst other things, this will make
# ./configure squeal if the package is re-configured with an
# inconsistent value of this variable.
AC_ARG_VAR(STARLINK, [Location of a current Starlink tree (used if necessary)])dnl

# AC_SUBST the STARLINK variable.  Macro AC_ARG_VAR does this anyway,
# but automake doesn't know that (in 1.6 at least): however any
# variable that automake finds has been AC_SUBSTed, it includes in
# Makefile.in, and we need that.
AC_SUBST(STARLINK)

# Use the above information: $STARLINK indicates a preexisting
# Starlink tree.
#
# Avoid doing anything if $STARLINK was unset above.
#
# Add library search paths using STAR_LDFLAGS.  Do it this way, rather than
# by defining LIBS (which is also a non-user variable): (a) these are
# really options to the linker, rather than adjustments to the set of
# libraries, so this makes sense; also (b) adding them to LIBS is too
# late, since that adds -L _after_ any -l options found in *_LDADD.
if test -n "$STARLINK"; then
    STAR_CPPFLAGS="-I$STARLINK/include"
    STAR_FCFLAGS="-I$STARLINK/include"
    STAR_FFLAGS="-I$STARLINK/include"
    STAR_LDFLAGS="-L$STARLINK/lib"
else
    STAR_CPPFLAGS=
    STAR_FCFLAGS=
    STAR_FFLAGS=
    STAR_LDFLAGS=
fi
AC_SUBST(STAR_CPPFLAGS)
AC_SUBST(STAR_FCFLAGS)
AC_SUBST(STAR_FFLAGS)
AC_SUBST(STAR_LDFLAGS)

# Installation directory options (these are no longer handled
# by _STAR_EXTRADIR_COMMON).  There should be an entry here for each of
# Starlink's special installation locations.
AC_SUBST([stardocsdir],     ['${prefix}/docs'])dnl     documentation
AC_SUBST([staretcdir],      ['${prefix}/etc'])dnl
AC_SUBST([starexamplesdir], ['${prefix}/examples'])dnl
AC_SUBST([starfacsdir],     ['${prefix}/help'])dnl     facilities files
AC_SUBST([starhelpdir],     ['${prefix}/help'])dnl     other help files
AC_SUBST([starnewsdir],     ['${prefix}/news'])dnl

# Certain directories are affected by the $_star_per_package_dir variable;
# if it's true, then add the $PACKAGE_NAME to the directory.
# The directories currently adjusted by this are bin and help;
# there are others: see PWD's message of 2004-02-16
# <http://www.jiscmail.ac.uk/cgi-bin/wa.exe?A2=ind0402&L=stardev&T=0&F=&S=&P=5153>
if $_star_per_package_dirs; then
    bindir="$bindir/$PACKAGE_NAME"
    starhelpdir="$starhelpdir/$PACKAGE_NAME"
    staretcdir="$staretcdir/$PACKAGE_NAME"
    AC_MSG_NOTICE([[STAR_DEFAULTS] has option per-package-dirs:])
    AC_MSG_NOTICE([    bindir=$bindir starhelpdir=$starhelpdir staretcdir=$staretcdir])
    # Note that starfacsdir is unaffected by per-package-dirs -- facility
    # files must always be installed in .../help (this also facilitates
    # changing this installation location in future, to somewhere with a
    # more logical name than .../help).
fi


# Dependency declarations and checks.
# Everything is dependent on starconf, so we don't have to declare that 
# for each package separately.
# STAR_DEPENDENCIES_ATTRIBUTES is currently not used.
STAR_DEPENDENCIES_ATTRIBUTES=''
STAR_DEPENDENCIES_CHILDREN=''
AC_SUBST(STAR_DEPENDENCIES_ATTRIBUTES)
AC_SUBST(STAR_DEPENDENCIES_CHILDREN)

# List of documentation.  See [STAR_LATEX_DOCUMENTATION].
# STAR_DOCUMENTATION is a list of document codes,
STAR_DOCUMENTATION=
AC_SUBST([STAR_DOCUMENTATION])

# Create a PACKAGE_VERSION_INTEGER variable, which contains the
# package's version number as an integer major*1e6+minor*1e3+release.
eval [`echo $VERSION | sed -e 's/\([0-9]*\)[^0-9]*\([0-9]*\)[^0-9]*\([0-9]*\).*/PACKAGE_VERSION_MAJOR=\1; PACKAGE_VERSION_MINOR=\2; PACKAGE_VERSION_RELEASE=\3;/'`]
test -n "$PACKAGE_VERSION_MAJOR"   || PACKAGE_VERSION_MAJOR=0
test -n "$PACKAGE_VERSION_MINOR"   || PACKAGE_VERSION_MINOR=0
test -n "$PACKAGE_VERSION_RELEASE" || PACKAGE_VERSION_RELEASE=0
PACKAGE_VERSION_INTEGER=`expr $PACKAGE_VERSION_MAJOR \* 1000000 + $PACKAGE_VERSION_MINOR \* 1000 + $PACKAGE_VERSION_RELEASE`
AC_SUBST(PACKAGE_VERSION_MAJOR)
AC_SUBST(PACKAGE_VERSION_MINOR)
AC_SUBST(PACKAGE_VERSION_RELEASE)
AC_SUBST(PACKAGE_VERSION_INTEGER)
dnl Don't put this into config.h -- subst a .h file if required.
dnl May change this in future
dnl AC_DEFINE_UNQUOTED([PACKAGE_VERSION_INTEGER], $PACKAGE_VERSION_INTEGER,
dnl                    [Integer version number, in the form major*1e6+minor*1e3+release])

# When we do dependency checking, using the dependencies declared in
# the package's configure.ac, we do so by looking at what tools have
# already been installed in the Starlink tree.  The tree in question
# is to be found under $STARLINK (see above), so we check that a
# package is installed by checking that its manifest can be found in
# $STARLINK/manifests.  We don't AC_SUBST this.
current_MANIFESTS=$STARLINK/manifests

# When we install manifests, however, they should go in the
# installation directory.  Allow this to be defaulted from the environment.
# In particular, if it is set to null in the environment, this will
# suppress the installation of manifests.
: ${STAR_MANIFEST_DIR='$(prefix)/manifests'}
AC_SUBST(STAR_MANIFEST_DIR)

# Each package updates the "starlink.version" file installed into the
# manifests directory. This tracks the last git sha1 checkin for
# the current code state by running the git show on the HEAD.
# Define GIT as the program to run, but allow it to be overridden 
# (most likely by ":" to avoid the overhead).
# Also requires that STAR_SOURCE_ROOT_DIR is defined to locate the
# head of the source tree.
: ${GIT='git'}
if test "${GIT}" = "git"; then
   AC_PATH_PROG(GIT, git)
fi
AC_SUBST(GIT)

: ${STAR_SOURCE_ROOT_DIR=''}
AC_SUBST(STAR_SOURCE_ROOT_DIR)

# Although PACKAGE_VERSION is a default output variable, it isn't
# added as a Makefile variable by default.  We need it below, however,
# so add it now.
AC_SUBST(PACKAGE_VERSION)

# Initialise state of predist/postdist flags (see STAR_PREDIST_SOURCES).
# The value of _star_predist_status must be inherited by any
# ./configure run in a subdirectory, so that we there avoid the predist
# test of starconf.status: in a pre-distribution state, this file must
# be present in the component directory (where we are running
# ./configure), but must not be present in any subdirectory.
_star_predist_status=unknown
PREDIST='#'  # safe default
AC_SUBST(PREDIST)

# pax and/or tar are used in some install targets.
# Note: value-if-not-found should be blank, so this can be tested for.
AC_PATH_PROG(PAX, pax)
AC_PATH_PROGS(TAR, [gnutar tar])

ALL_TARGET=all-am-normal

# Default $prefix.  This is done by the standard autoconf configure, but at
# a slightly later stage than this.  Doing it here, as part of STAR_[]DEFAULTS
# means that the defaulted value of $prefix can be used within the body of
# the configure.ac, for example to pass it to a ./configure in a subdirectory.
test "x$prefix" = xNONE && prefix=$ac_default_prefix
# Let make expand exec_prefix.
test "x$exec_prefix" = xNONE && exec_prefix='${prefix}'
])# STAR_DEFAULTS



# STAR_MESSGEN([msgfile-list])
# ----------------------------
#
# Handle generating message, error, and facility files.
#
# Declare that we will need to use the messgen utility.  This macro
# does not by itself cause the messgen rules to be included in the
# makefile -- that is done by automake, when it sees a
# 'include_MESSAGES' or 'noinst_MESSAGES' variable.
#
# The optional argument is a space-separated list of files, each of
# which has a set of message declarations in it, in the format
# prescribed by the messgen utility.  If this is present, then the
# named files are declared as pre-distribution files (the macro calls
# STAR_PREDIST_SOURCES on them), and so the resulting configure script
# should expect not to find them in an unpacked distribution.  This is
# useful as documentation or as a shortcut for calling the latter
# macro, but recall that it is the presence of the automake
# 'include_MESSAGES' variable which does the work.
#
# The macro may be called more than once if you have more than one
# .msg file in the directory.
#
# The files listed in the '_MESSAGES' variable will often have to be 
# declared as `BUILT_SOURCES'.  
#
# The macro also implicitly declares a `sourceset' dependency on the
# messgen package.
AC_DEFUN([STAR_MESSGEN],
   [#
    $_star_docs_only &&
        AC_MSG_ERROR([STAR[]_MESSGEN in docs-only directory])
    STAR_DECLARE_DEPENDENCIES([sourceset], [messgen])
    m4_ifval([$1], [STAR_PREDIST_SOURCES($1)])
    STAR_CHECK_PROGS(messgen)
])# STAR_MESSGEN


# STAR_PREDIST_SOURCES(source-files)
# ----------------------------------
#
# Give a (space-separated) list of files which should exist only in
# the pre-distribution (ie, repository checkout) state.  If one of
# these is found, then the substitution variable PREDIST is set to a
# blank.  We should find either all of the marker files or none of
# them; if only some of the marker files are found, this is probably
# an error of some type, so warn about it.  This means, by the way,
# that it is the presence or absence of the first marker file which
# determines whether we are in the predist or postdist state, with the
# rest providing consistency checks.
#
# The macro may be called more than once.  Multiple calls are
# equivalent to a single call with all the marker files in the list.
# Automake checks that the files listed here are not in the list of
# distributed files, and issues a warning if they are.
AC_DEFUN([STAR_PREDIST_SOURCES],
[m4_ifval([$1], [], [AC_FATAL([$0: called with no stamp file])])dnl
_star_tmp='$1'
for marker in $_star_tmp
do
    if test -f $marker; then
        _star_predist_marker_present=:
        AC_MSG_NOTICE([found predist marker file $marker])
    else
        _star_predist_marker_present=false
    fi
    case $_star_predist_status in
        unknown)
            if $_star_predist_marker_present; then
                # we do want to build sourceset files
                _star_predist_status=predist
                PREDIST=
                AC_MSG_NOTICE([in pre-distribution state])
            else
                _star_predist_status=postdist
                PREDIST='#'
                AC_MSG_NOTICE([in post-distribution state])
            fi
            ;;
        predist)
            if $_star_predist_marker_present; then
                : OK
            else
                AC_MSG_WARN([Building predist, but marker file $marker is not present])
            fi
            ;;
        postdist)
            if $_star_predist_marker_present; then
                AC_MSG_WARN([In postdistribution state, but predist marker file $marker is present])
            fi
            ;;
        *)
            AC_MSG_ERROR([impossible predist status $_star_predist_status])
            ;;
    esac
done
])# STAR_PREDIST_SOURCES


# STAR_CNF_COMPATIBLE_SYMBOLS
# ---------------------------
#
# Work out what is required to have the Fortran compiler produce
# library symbols which are compatible with those expected by the CNF
# package.  If you are building a library in which C code refers to
# Fortran libraries, then you should call this macro, which possibly
# adjusts the AM_FCFLAGS variable.  That is, if you include cnf.h, you
# should have this macro in the configure.ac.
#
# This macro deals with the following issue.  The cnf.h header
# includes a macro F77_EXTERNAL_NAME which mangles a C name into the
# corresponding name the Fortran compiler would generate; this
# generally means no more than appending a single underscore.  As the
# autoconf documentation for AC_FC_WRAPPERS points out, this is less
# general than it could be, as some Fortrans fold symbols to
# uppercase, and some (in particular g77) add two underscores to
# symbols which already contain one (thus mangling 'ab' to 'ab_', but
# 'a_b' to 'a_b__').  This behaviour would break the F77_EXTERNAL_NAME
# macro, which is used throughout the Starlink code in both cases,
# unless we compiled all the Starlink Fortran libraries in a mode which
# suppressed this second underscore.  Working out how to do that --
# if it's necessary at all -- is what this macro does.
#
# The more restricted interface of F77_EXTERNAL_NAME is, by the way,
# the reason why we cannot simply copy the FC_FUNC definition to the
# cnf.h file as F77_EXTERNAL_NAME: the latter macro is used for
# symbols both with and without an underscore.
#
# If we ever have to migrate the Starlink software to a Fortran which
# does more complicated name mangling, we'll almost certainly have to
# perform more serious surgery on cnf.h, using the results of
# AC_FC_WRAPPERS, along with similar surgery on the code which invokes
# it.
#
# This macro is designed to work with CNF, however it does _not_
# require the cnf.h headers to be installed, because it should remain
# callable at configuration time before _anything_ has been installed.
# In the test code below, we therefore emulate the definition of
# F77_EXTERNAL_NAME in cnf.h, which appends a single underscore.
# to the end of C symbols.
#
AC_DEFUN([STAR_CNF_COMPATIBLE_SYMBOLS],
   [$_star_docs_only &&
        AC_MSG_ERROR([STAR[]_CNF_COMPATIBLE_SYMBOLS in docs-only dir])
    AC_CACHE_CHECK([how to make Fortran and C play nicely],
       [star_cv_cnf_compatible_symbols],
       [dnl AC_REQUIRE([AC_PROG_FC])dnl
        dnl AC_REQUIRE([AC_PROG_CC])dnl
        AC_LANG_PUSH([C])
        AC_LANG_CONFTEST([AC_LANG_SOURCE([
void funcone_() { return; }
void func_two_() { return; }
])])
        if (eval $ac_compile) 2>&5
        then
            mv conftest.$ac_objext c-conftest.$ac_objext
        else
            AC_MSG_ERROR([cannot compile a C program!])
        fi
        AC_LANG_POP(C)
        AC_LANG_PUSH([Fortran])
        AC_LANG_CONFTEST([AC_LANG_SOURCE([
      PROGRAM conftest
      CALL funcone
      CALL func_two
      END
])])
        star_cv_cnf_compatible_symbols=cantlink
        # The only Fortran we (need to) handle at present is
        # g77, which has a -fno-second-underscore option for
        # simplifying the mangling here.  Other Fortrans we've
        # used do only the single-underscore mangling.
        for opt in "" "-fno-second-underscore"
        do
            if $FC $FCFLAGS $opt -o conftest conftest.f c-conftest.$ac_objext 2>&5
            then
                star_cv_cnf_compatible_symbols=$opt
                break
            fi
        done
        AC_LANG_POP([Fortran])
        rm -f conftest* c-conftest*
])
    if test "$star_cv_cnf_compatible_symbols" = cantlink
    then
        AC_MSG_ERROR([cannot work out how])
    else
        STAR_FCFLAGS="$STAR_FCFLAGS $star_cv_cnf_compatible_symbols"
        STAR_FFLAGS="$STAR_FFLAGS $star_cv_cnf_compatible_symbols"
    fi
])# STAR_CNF_COMPATIBLE_SYMBOLS


# STAR_CNF_F2C_COMPATIBLE
# -----------------------
#
# Work out if the compiler is using 'f2c' compatible calling conventions.
#
# The `f2c' calling conventions, used by GNU Fortran compilers, require
# functions that return type REAL to actually return the C type 'double'
# (there is also special handling of COMPLEX returns, but that's not supported
# by CNF). When operating in 'non-f2c' mode such functions return the expected
# C type 'float'.
#
# The effect of this macro is subsitute the variable REAL_FUNCTION_TYPE
# to either float or double as required.
#
# This function is not infallable and will usually return float for GNU
# compilers, as the calling convention seems to not matter on 32-bit platforms
# for the test in use. A stronger test would be to attempt calling a intrinsic
# function, which is supposed to fail. Non-GNU compilers should always
# return float. However, this test is used as it is all that is required.
#
AC_DEFUN([STAR_CNF_F2C_COMPATIBLE],
   [$_star_docs_only &&
        AC_MSG_ERROR([STAR[]_CNF_F2C_SYMBOLS in docs-only dir])
    AC_CACHE_CHECK([if $FC is in strict f2c compatible mode],
       [star_cv_cnf_f2c_compatible],
       [AC_REQUIRE([AC_PROG_FC])dnl
        if test "$ac_cv_fc_compiler_gnu" = yes; then
           AC_REQUIRE([AC_PROG_CC])dnl
           AC_LANG_PUSH([C])
           AC_LANG_CONFTEST([AC_LANG_SOURCE([
float fred_() {
   return 1.0f;
}
])])
           if (eval $ac_compile) 2>&5
           then
               mv conftest.$ac_objext c-conftest.$ac_objext
           else
               AC_MSG_ERROR([cannot compile a C function!])
           fi
           AC_LANG_POP(C)
           AC_LANG_PUSH([Fortran])
           AC_LANG_CONFTEST([AC_LANG_SOURCE([
      PROGRAM F2CTEST
      REAL FRED
      REAL R
      R = FRED()
      IF ( R .NE. 0.0 ) THEN
         WRITE(*,*) 'no'
      ELSE
         WRITE(*,*) 'yes'
      ENDIF
      END
])])
           star_cv_cnf_f2c_compatible=yes
           $FC $FCFLAGS $opt -o conftest conftest.f c-conftest.$ac_objext 2>&5
           if test -r conftest
           then
              star_cv_cnf_f2c_compatible=`eval ./conftest | sed 's/\ //g'` > /dev/null
           else
              AC_MSG_ERROR([failed to link program]) 
           fi
           AC_LANG_POP([Fortran])
           rm -f conftest* c-conftest*
      else
         # Not a GNU compiler.
         star_cv_cnf_f2c_compatible=no
      fi
])
    if test "$star_cv_cnf_f2c_compatible" = "yes"
    then
        AC_SUBST(REAL_FUNCTION_TYPE, double)
    else
        AC_SUBST(REAL_FUNCTION_TYPE, float)
    fi
])# STAR_CNF_F2C_COMPATIBLE

# STAR_CNF_BLANK_COMMON
# ---------------------
# Define the global symbol used to access the Fortran blank common block.
# Usually under UNIX this is _BLNK__, but gfortran uses __BLNK__, so we
# need to check for that. Gfortran is just detected by being a GNU compiler
# and having "Fortran (GCC) 4.x[x].x[x]" as part of its --version output.
#
# The effect of this macro is to substitute BLANK_COMMON_SYMBOL with
# the expected value.
#
AC_DEFUN([STAR_CNF_BLANK_COMMON],
   [AC_CACHE_CHECK([symbol used for blank common in Fortran],
       [star_cv_blank_common_symbol],
       [AC_REQUIRE([AC_PROG_FC])
       star_cv_blank_common_symbol=_BLNK__
       if test "$ac_cv_fc_compiler_gnu" = yes; then
            if "$FC" --version 2>&1 < /dev/null | grep 'GNU Fortran.*[[4-9]]\.[[0-9]][[0-9]]*\.[[0-9]][[0-9]]*' > /dev/null; then
                star_cv_blank_common_symbol=__BLNK__
            fi
       fi])
    AC_SUBST([BLANK_COMMON_SYMBOL], $star_cv_blank_common_symbol )
])# STAR_CNF_BLANK_COMMON

# STAR_PRM_COMPATIBLE_SYMBOLS
# ---------------------------
#
#  See if any special flags are required to support PRM and the use of the
#  PRM_PAR constants. If a typeless BOZ descriptor is available (usually 'X)
#  then this macro will have no effect, however, if there's no typeless BOZ
#  support any special Fortran compiler flags that are required when using
#  PRM_PAR will be defined as part of the STAR_FCFLAGS and STAR_FFLAGS
#  variables.
#
#  In fact this macro is only currently used for the gfortran and Solaris f95
#  compilers. Gfortran has no typeless BOZ support, so requires that the
#  -fno-range-check flag is set so that assigments to integers can silently
#  overflow (BOZ constants are replaced with their plain integer and floating
#  point equivalents). The Solaris f95 compiler doesn't allow assignments to
#  LOGICAL parameters, so we need to use the -f77 flag.
#
#  In general this macro should be used by all packages that include PRM_PAR,
#  all monoliths are assumed to use this by default. 
#
AC_DEFUN([STAR_PRM_COMPATIBLE_SYMBOLS],
   [$_star_docs_only &&
        AC_MSG_ERROR([STAR[]_PRM_COMPATIBLE_SYMBOLS in docs-only dir])
    AC_CACHE_CHECK([how to make compiler accept PRM constants],
       [star_cv_prm_compatible_symbols],
       [star_cv_prm_compatible_symbols="nocheck"
        AC_MSG_NOTICE([ ])
        AC_FC_HAVE_TYPELESS_BOZ 2>&5
        if test $ac_cv_fc_have_typeless_boz = no; then
           AC_FC_HAVE_OLD_TYPELESS_BOZ 2>&5
           if test $ac_cv_fc_have_old_typeless_boz = no; then
              #  Test if -f77 works. Note need to clear the cached variables
              #  for these tests.
              unset ac_cv_fc_have_typeless_boz
              unset ac_cv_fc_have_old_typeless_boz
              old_FCFLAGS="$FCFLAGS"
              FCFLAGS="-f77 $FCFLAGS"
              AC_FC_HAVE_TYPELESS_BOZ 2>&5
              if test $ac_cv_fc_have_typeless_boz = no; then
                 AC_FC_HAVE_OLD_TYPELESS_BOZ 2>&5
                 if test $ac_cv_fc_have_old_typeless_boz = no; then
                    star_cv_prm_compatible_symbols="nocheck"
                 else
                    star_cv_prm_compatible_symbols="-f77"
                 fi
              else
                 star_cv_prm_compatible_symbols="-f77"
              fi
              FCFLAGS="$old_FCFLAGS"
              if test "$star_cv_prm_compatible_symbols" = "nocheck"; then
                 #  Test if "-fno-range-check" works.
                 AC_REQUIRE([AC_PROG_FC])dnl
                 AC_LANG_PUSH([Fortran])
                 AC_LANG_CONFTEST([AC_LANG_SOURCE([
      PROGRAM conftest
      INTEGER*2 VAL__BADUW
      PARAMETER ( VAL__BADUW = 65535 )
      BYTE VAL__BADUB
      PARAMETER ( VAL__BADUB = 255 )
      END
])])
                 if $FC -c $FCFLAGS -fno-range-check -o conftest conftest.f 2>&5
                 then
                    star_cv_prm_compatible_symbols="-fno-range-check"
                 fi              
                 AC_LANG_POP([Fortran])
                 rm -f conftest.f
              fi
           else
              star_cv_prm_compatible_symbols=""
           fi
         else
            star_cv_prm_compatible_symbols=""
         fi])
         if test "$star_cv_prm_compatible_symbols" = "nocheck"; then
            AC_MSG_ERROR([cannot work out how])
         else
            STAR_FCFLAGS="$STAR_FCFLAGS $star_cv_prm_compatible_symbols"
            STAR_FFLAGS="$STAR_FFLAGS $star_cv_prm_compatible_symbols"
         fi
])# STAR_PRM_COMPATIBLE_SYMBOLS

# STAR_CNF_TRAIL_TYPE
# -------------------
#
# Work out what type to use for the trailing lengths of character strings
# passed from Fortran to C. See the "TRAIL" descriptions in SUN/209.
#
# For most compilers the maximum length of a string is limited to a 32bit
# unsigned int, but for others, this can be a 64bit unsigned long. Currently
# the only compilers with 64bit strings are 64bit Intel fortran and
# Solaris studio12 with -m64.
#
# The test is only performed for 64bit compilers, all others are assumed
# to use 32bit lengths. Various attempts to trap this issue permanently 
# using a test program have failed (especially for the Intel compiler), so the
# actual test is to check for a known 64 bit compiler first and then try a
# program that has had some success. Note no GNU compilers seem to have this
# problem so they are never tested.
#
# The side-effect of this macro is to substitute TRAIL_TYPE with
# the derived value and define TRAIL_TYPE. See "f77.h" in CNF.
#
AC_DEFUN([STAR_CNF_TRAIL_TYPE],
   [AC_CHECK_SIZEOF(void*)dnl
    AC_FC_HAVE_PERCENTLOC dnl
    AC_CACHE_CHECK([type used for Fortran string lengths],
       [star_cv_cnf_trail_type],
       [if test "$ac_cv_sizeof_voidp" = 8 -a "$ac_cv_fc_compiler_gnu" = no; then
           if "$FC" -V 2>&1 < /dev/null | grep 'Intel.*64' > /dev/null; then
              star_cv_cnf_trail_type=long
           elif "$FC" -V 2>&1 < /dev/null | grep 'Sun.*Fortran' > /dev/null; then
              star_cv_cnf_trail_type=long
           else
              AC_REQUIRE([AC_PROG_FC])dnl
              AC_LANG_PUSH([Fortran])
              if test "$ac_cv_fc_have_percentloc" = yes; then
                 FORTRAN_GETLOC='%loc'
              else 
                 FORTRAN_GETLOC='loc'
              fi
              AC_LANG_CONFTEST([AC_LANG_SOURCE([
      program conftest

C  checks passing 4 byte character string lengths on 64bit compiler.

      integer*8 ip1, ip2
      integer*4 l1, l2
      integer dummy1, dummy2
      real dummy3, dummy4
      double precision dummy5, dummy6

      character str1*(1024)
      character str2*(2048)

      ip1 = $FORTRAN_GETLOC (str1)
      ip2 = $FORTRAN_GETLOC (str2)

      l1 = 1024
      l2 = 2048

      call report( dummy1, dummy2, %val(ip1), dummy3, dummy4,
     :             %val(ip2), dummy5, dummy6, 
     :             %val(l1), %val(l2) )

      end

      subroutine report( dummy1, dummy2, str1, dummy3, dummy4,
     :                   str2, dummy5, dummy6 )
      integer dummy1, dummy2
      real dummy3, dummy4
      double precision dummy5, dummy6

      character*(*) str1
      character*(*) str2

      if ( [len(str1)] .eq. 1024 .and. [len(str2)] .eq. 2048 ) then
         print *, 'int'
      else
         print *, 'long'
      endif
      end
])])
              star_cv_cnf_trail_type=int
              $FC $FCFLAGS $opt -o conftest conftest.f 2>&5
              if test -r conftest
              then
                 star_cv_cnf_trail_type=`eval ./conftest | sed 's/\ //g'` > /dev/null
              else
                 AC_MSG_ERROR([failed to link program]) 
              fi
              rm -f conftest*
              AC_LANG_POP([Fortran])
           fi
        else
dnl  sizeof(void *) != 8 or GNU so no problems.
           star_cv_cnf_trail_type=int
        fi
])
    AC_SUBST([TRAIL_TYPE], $star_cv_cnf_trail_type )
    AC_DEFINE_UNQUOTED([TRAIL_TYPE], $star_cv_cnf_trail_type, 
                       [Type of Fortran CNF TRAIL argument] )
])# STAR_CNF_TRAIL_TYPE

# STAR_PATH_TCLTK([minversion=0], [options=''])
# ---------------------------------------------
#
# Finds a tclsh and wish, and the associated libraries.  Sets output variable
# TCL_CFLAGS to the C compiler flags necessary to compile with Tcl, TCL_LIBS
# to the required library flags, and TCLSH to the full path of the tclsh
# executable, TCL_PREFIX to the installation root and TCL_LD_SEARCH_FLAGS
# to the default search path for loading the shareable library; if Tk is  
# requested, it similarly sets TK_CFLAGS, TK_LIBS and WISH.  Define the 
# cpp variable TCL_MISSING to 1 if Tcl is not available.  Similar to 
# macro AC_PATH_XTRA.
#
# If argument MINVERSION is present, it specifies the minimum Tcl/Tk
# version number required.
#
# The macro searches first in the path, and
# then in a selection of platform-specific standard locations.  The
# configure option --with-tcl allows you to provide a path to a tclsh
# binary, which is put at the head of the list of locations to search.
# Option --without-tcl suppresses the search, and results in no
# variables being substituted.
#
# If the argument OPTIONS is present, it is a space-separated list of
# the words 'tk' or 'itcl'.  If one or both of these is present, then
# the macro will find a Tcl location which also has Tk or itcl
# installed (note that the itcl test doesn't do anything at present).
AC_DEFUN([STAR_PATH_TCLTK],
    [_star_use_tcl=:
     AC_ARG_WITH([tcl],
                 AS_HELP_STRING([--with-tcl],
                                [give path to tclsh (dir which contains binary)]),
                 [if test "X$withval" = Xno; then
                      _star_use_tcl=false
                  elif test "X$withval" = Xyes; then
                      _star_use_tcl=:
                  else
                      _star_use_tcl=:
                      _star_try_tcldir=$withval
                  fi])
     if $_star_use_tcl; then
         _star_searchfor=Tcl
         if expr "x m4_ifval([$2], [$2], []) " : 'x.* tk ' >/dev/null; then
             search_tk=:
             _star_searchfor="$_star_searchfor/Tk"
         else
             search_tk=false
         fi
         if expr "x m4_ifval([$2], [$2], []) " : 'x.* itcl ' >/dev/null; then
             search_itcl=:
             _star_searchfor="$_star_searchfor/itcl"
             echo "Searching for itcl does nothing so far!"
         else
             search_itcl=false
         fi
         AC_MSG_CHECKING([where to find $_star_searchfor m4_ifval([$1], [$1+], [(any version)])])
         AC_CACHE_VAL([star_cv_settcldir],
             [star_cv_settcldir=unknown
              reqversint=`echo m4_ifval([$1], [$1], 0.0)-0-0 | [sed 's/\([0-9]*\)[^0-9]*\([0-9]*\)[^0-9]*\([0-9]*\).*/10000 \1* 100 \2*+ \3+p/']|dc`
              tclsources=`echo $PATH | sed "s/$PATH_SEPARATOR/ /g"`
              stdsources='
dnl  Search in /usr and /usr/local at least
/usr/bin
/usr/local/bin
dnl  /opt/local and /sw are the default installation locations for OpenDarwin
dnl  and Fink on OSX
/opt/local/bin
/sw/bin'
              for d in $_star_try_tcldir $STARCONF_DEFAULT_STARLINK/bin $tclsources $stdsources
              do
                  locok=:
                  if test -d $d; then
                      tcldir=`cd $d/..; pwd`
                      test -f $d/tclsh -a -f $tcldir/include/tcl.h || locok=false
                  else
                      locok=false
                  fi
                  if $locok && $search_tk; then
                      test -f $d/wish -a -f $tcldir/include/tk.h || locok=false
                  fi
                  if $locok && $search_itcl; then
                      test -f $tcldir/lib/libitcl.aXXX || locok=false
                  fi
                  if $locok; then
                       if test ! -f $tcldir/lib/tclConfig.sh; then
                           echo "$tcldir/lib/tclConfig.sh unexpectedly missing"
                           break
                       fi
                       if $search_tk && test ! -f $tcldir/lib/tkConfig.sh; then
                           echo "$tcldir/lib/tkConfig.sh unexpectedly missing"
                           break
                       fi
                       rm -f conftest.results
                       # Run in a subshell, to isolate settings in tclConfig.sh
                       # Send output to conftest.results, and return
                       # 0 if all is ok
                       (
    . $tcldir/lib/tclConfig.sh
    if $search_tk; then
        . $tcldir/lib/tkConfig.sh
    fi
    tclversint=`[echo $TCL_VERSION$TCL_PATCH_LEVEL-0-0 | sed 's/\([0-9]*\)[^0-9]*\([0-9]*\)[^0-9]*\([0-9]*\).*/10000 \1* 100 \2*+ \3+p/'|dc]`
    if test $tclversint -gt $reqversint; then
        # New enough version.

        # Dereference the tclsh and wish links -- the "->" _is_ standard,
        # mandated by POSIX.
        lslink=`ls -l $tcldir/bin/tclsh`
        tclsh_loc=`expr "x$lslink" : "x.*-> *\(.*\)"`
        if test -n "$tclsh_loc" -a -x "$tclsh_loc"; then
           : OK
        elif test -x "$tcldir/bin/tclsh"; then
            # Odd: either .../bin/tclsh isn't a link, or it doesn't point to an
            # executable.  But .../bin/tclsh is OK, so use that.
            tclsh_loc="$tcldir/bin/tclsh"
        else
            # This really shouldn't happen, since we checked above that
            # $d/tclsh was executable.  Still, it clearly has happened,
            # so don't go mad.
            echo "Warning: found Tcl libraries, but not tclsh!" >&2
            tclsh_loc=
        fi

        res="_star_tcldir=$tcldir;"

        # Make the TCL version number available.
        res="$res TCL_VERSION=\"$TCL_VERSION\";"

        # Export the TCL_PREFIX value.
        res="$res TCL_PREFIX=\"$TCL_PREFIX\";"

        # Export the TCL_LD_SEARCH_FLAGS value (need LIB_RUNTIME_DIR
        # which is part of the symbol).
        res="$res LIB_RUNTIME_DIR=\"$TCL_PREFIX/lib\";"
        res="$res TCL_LD_SEARCH_FLAGS=\"$TCL_LD_SEARCH_FLAGS\";"

        # These envs include $TCL_DBGX -- expand this out.
        eval "I=\"$TCL_INCLUDE_SPEC\"; L=\"$TCL_LIB_SPEC\""
        res="$res TCL_CFLAGS=\"$I\"; TCL_LIBS=\"$L\"; TCLSH=\"$tclsh_loc\";"

        if $search_tk; then
            # Same for wish
            lslink=`ls -l $tcldir/bin/wish`
            wish_loc=`expr "x$lslink" : "x.*-> *\(.*\)"`
            if test -n "$wish_loc" -a -x "$wish_loc"; then
                : OK
            elif test -x "$tcldir/bin/wish"; then
                wish_loc="$tcldir/bin/wish"
            else
                echo "Warning: found Tk libraries, but not wish!" >&2
                wish_loc=
            fi
            # These envs potentially include $TK_DBGX -- expand this out.
            eval "I=\"$TK_XINCLUDES\"; L=\"$TK_LIB_SPEC\""
            res="$res TK_CFLAGS=\"$I\"; TK_LIBS=\"$L\"; WISH=\"$wish_loc\";"
        fi

        # similarly for $search_itcl

        echo $res >conftest.results
        status=0
    else
        msg="$tcldir: found Tcl-$TCL_VERSION$TCL_PATCH_LEVEL"
        if $search_tk; then
            msg="$msg, Tk-$TK_VERSION$TK_PATCH_LEVEL"
        fi
        echo "$msg: older than required" >&2
        status=1
    fi
    exit $status
                       )
                       teststat=$?
                       if test $teststat = 0; then
                           star_cv_settcldir=`cat conftest.results`
                       fi
                       if test "$star_cv_settcldir" != unknown; then
                           break
                       fi
                  fi # $locok
              done])

        if test "$star_cv_settcldir" = unknown; then
            AC_MSG_RESULT(unknown)
        else
            eval $star_cv_settcldir
            AC_MSG_RESULT($_star_tcldir)
        fi
    else # $_star_use_tcl
        AC_MSG_WARN(Compiling without Tcl/Tk)
    fi # $_star_use_tcl

    if $_star_use_tcl && test "$star_cv_settcldir" != unknown; then
        :
    else
        AC_DEFINE(TCL_MISSING, 1,
                  [Define to 1 if no Tcl/Tk libraries can be found])
    fi

    AC_SUBST(TCL_VERSION)

    AC_SUBST(TCL_PREFIX)

    AC_SUBST(TCL_LD_SEARCH_FLAGS)
    AC_SUBST(TCL_CFLAGS)
    AC_SUBST(TCL_LIBS)
    AC_SUBST(TCLSH)

    AC_SUBST(TK_CFLAGS)
    AC_SUBST(TK_LIBS)
    AC_SUBST(WISH)

    # add itcl variables here

])# STAR_PATH_TCLTK


# STAR_LATEX_DOCUMENTATION(documentcode, [targets])
# -------------------------------------------------
# Generate the standard makefile targets to handle LaTeX documentation
# source.  The parameter documentcode should be something like
# `sun123' -- it should not include any .tex extension.
#
# The second, optional, argument gives an explicit list of the targets
# which are build.  If this is _not_ specified, then a standard list
# is used (.tex, .ps and .tar_htx) and corresponding rules added to
# the generated makefile.  If it is specified, it must be non-null,
# and its value is a list of files which are to be added to the
# distribution, and no extra Makefile rules are added.  Thus if users need
# anything complicated done, they should use this second argument and
# provide rules for satisfying the given targets.
#
# In the latter case, the .tex -> htx_tar rule is still emitted, so
# you can use it, but it requires the substitution variable
# @STAR[]2HTML@, and so if you _do_ use it, you will have to make that
# available, either through [STAR_CHECK_PROGS(star2html)] or otherwise.
AC_DEFUN([STAR_LATEX_DOCUMENTATION],
   [m4_ifval([$1], [], [AC_FATAL([$0: called with no documentcode])])dnl
    m4_if(m4_bregexp([$1], [^ *\([a-z][a-z]*[0-9]*/? *\)*$]),
          [0],
          [],
          [AC_FATAL([$0: bad doccode in $1 -- must be eg sun123 or sun123/])])
    STAR_DOCUMENTATION="$STAR_DOCUMENTATION m4_bpatsubst([$1],[/])"
    m4_ifval([$2],
       [dnl non-empty second argument -- just add to variable
        m4_if(m4_bregexp([$1], [/]), -1,
              [],
              [AC_FATAL([$0: do not mix non-null second argument and .../ syntax])])
        if $_star_build_docs; then
            STAR@&t@_LATEX_DOCUMENTATION="$2"
        fi
        ],
       [dnl second arg empty -- use defaults
        if $_star_build_docs; then
            AC_FOREACH([DocCode], [$1],
               [m4_if(m4_bregexp(DocCode,[/]), -1,
                      [STAR@&t@_LATEX_DOCUMENTATION="$STAR@&t@_LATEX_DOCUMENTATION DocCode.tex DocCode.pdf DocCode.htx_tar"
],
                      [m4_define([_T], m4_bpatsubst(DocCode,[/]))dnl
                       STAR_LATEX_DOCUMENTATION_[]_STAR_UPCASE(_T)="_T.tex _T.pdf _T.htx_tar"
                       AC_SUBST(STAR_LATEX_DOCUMENTATION_[]_STAR_UPCASE(_T))])])
        fi
        STAR_DECLARE_DEPENDENCIES([sourceset], [star2html])
        STAR_CHECK_PROGS([star2html])
       ])
    if $_star_build_docs; then
        : ${LATEX2DVI='$$LATEX "\\batchmode\\input $$[]1" && $$LATEX "\\batchmode\\input $$[]1"'}
        AC_SUBST(LATEX2DVI)
    else
        AC_MSG_WARN([not installing docs $1])
    fi
    AC_SUBST([STAR@&t@_LATEX_DOCUMENTATION])dnl
])# STAR_LATEX_DOCUMENTATION

# STAR_XML_DOCUMENTATION(documentcode, [targets])
# -----------------------------------------------
# Generate the standard makefile targets to handle XML documentation
# source.  The parameter documentcode should be something like
# `sun123' -- it should not include any .xml extension.  For each of the
# documentcodes which does not end with a slash, append
# <documentcode>.{texml_tar,htx_tar,ps} to STAR_XML_DOCUMENTATION;
# for each which does end with a slash, define instead the
# variable STAR_XML_DOCUMENTATION_<documentcode>.  In either case,
# append the documentcode to STAR_DOCUMENTATION
#
# The second, optional, argument gives an explicit list of the targets
# which are build.  If this is _not_ specified, then a standard list
# is used (.texml_tar, .ps and .htx_tar) and corresponding rules added to
# the generated makefile.  If it is specified, it must be non-null,
# and its value is a list of files which are to be added to the
# distribution, and no extra Makefile rules are added.  Thus if users need
# anything complicated done, they should use this second argument and
# provide rules for satisfying the given targets.
#
# In the latter case, the .tex -> htx_tar rule is still emitted, so
# you can use it, but it requires the substitution variables JADE, SGMLNORM,
# and SGMLKIT_HOME.  This is rather inconvenient, and it is fortunate that
# you almost certainly won't need to use this.
AC_DEFUN([STAR_XML_DOCUMENTATION],
   [m4_ifval([$1], [], [AC_FATAL([$0: called with no documentcode])])dnl
    m4_if(m4_bregexp([$1], [^ *\([a-z][a-z]*[0-9]*/? *\)*$]),
          [0],
          [],
          [AC_FATAL([$0: bad doccode in $1 -- must be eg sun123 or sun123/])])
    STAR_DOCUMENTATION="$STAR_DOCUMENTATION m4_bpatsubst([$1],[/])"
    m4_ifval([$2],
       [dnl non-empty second argument -- just add to variable
        m4_if(m4_bregexp([$1], [/]), -1,
              [],
              [AC_FATAL([$0: do not mix non-null second argument and .../ syntax])])
        if $_star_build_docs; then
            STAR@&t@_XML_DOCUMENTATION="$2"
        fi
        ],
       [dnl second arg empty -- use defaults
        if $_star_build_docs; then
            do_the_build=  # blank if we're to go ahead, string expl. otherwise
            AC_PATH_PROGS(JADE, [openjade jade], NOJADE)
            AC_PATH_PROGS(SGMLNORM, [osgmlnorm sgmlnorm], NOSGMLNORM)
            STAR_CHECK_PROGS([sgml2docs])
            if test "$JADE" = NOJADE -o "$SGMLNORM" = NOSGMLNORM -o "$SGML2DOCS" = "sgml2docs"; then
                if $_star_docs_only; then
                    # Building documentation is all we're supposed to do,
                    # and we can't, so suppress further building.
                    do_the_build=\
"This docs-only component requires Jade, sgmlnorm and sgml2docs.  
        All I could find were:
        $JADE for Jade, 
        $SGMLNORM for sgmlnorm and 
        $SGML2DOCS for sgml2docs (requires full path).
        Your system may have a way to install Jade and sgmlnorm as a package,
        sgml2docs is part of the SGMLKIT package."
                else
                    AC_MSG_WARN([can't find (open)jade + (o)sgmlnorm + sgml2docs -- skipping XML documentation $1])
                fi
            else
                # Test Jade version
                AC_MSG_CHECKING([version of $JADE (need 1.3.2 or better)])
                $JADE -v </dev/null >conftest.version 2>&1
                JADEVERS=[`sed -n '/:I:.*[Jj]ade.*version/{
    s/.*:I://
    s/[^0-9][^0-9]*/ /gp
}' conftest.version`]
                # The following converts space-separated integers to a single
                # one.  It's perhaps a leeettle funkier than necessary...
                VERSINT=[`echo "[Ss[z0<a]x]sa $JADEVERS 0 0 0 lax Ls100* Ls+100* Ls+p" | dc`]
                if test $VERSINT -ge 10302; then
                  AC_MSG_RESULT([ok])
                  AC_FOREACH([DocCode], [$1],
                   [m4_if(m4_bregexp(DocCode,[/]), -1,
                          [STAR@&t@_XML_DOCUMENTATION="$STAR@&t@_XML_DOCUMENTATION DocCode.texml_tar DocCode.htx_tar DocCode.ps DocCode.pdf"
],
                          [m4_define([_T], m4_bpatsubst(DocCode,[/]))dnl
                           STAR_XML_DOCUMENTATION_[]_STAR_UPCASE(_T)="_T.texml_tar _T.htx_tar _T.ps _T.pdf"
                           AC_SUBST(STAR_XML_DOCUMENTATION_[]_STAR_UPCASE(_T))])])
                else
                    AC_MSG_RESULT([too old])
                    do_the_build="Your openjade is version $JADEVERS; need 1.3.2 or better"
                fi
                SGMLKIT_HOME=$prefix/lib/sgmlkit
                AC_SUBST(SGMLKIT_HOME)
            fi
            STAR_SUPPRESS_BUILD_IF(test -n "$do_the_build", [$do_the_build])
        fi
        STAR_DECLARE_DEPENDENCIES([sourceset], [sgmlkit])
       ])
    if $_star_build_docs; then
        : ${LATEX2DVI='$$LATEX "\\batchmode\\input $$[]1" && $$LATEX "\\batchmode\\input $$[]1"'}
        AC_SUBST(LATEX2DVI)
    else
        AC_MSG_WARN([not installing docs $1])
    fi
    AC_SUBST([STAR@&t@_XML_DOCUMENTATION])dnl
])# STAR_XML_DOCUMENTATION
            


# STAR_CHECK_PROGS(progs-to-check-for, [component=''])
# --------------------------------------------------
#
# For each of the programs in PROGS-TO-CHECK-FOR, define a variable
# whose name is the upcased version of the program name, and whose
# value is the full path to that program, or the expected installation
# location of that program if no absolute path can be found.  Because
# of this default behaviour, this macro should _only_ be used for
# locating Starlink programs such as messgen or alink, and not as a
# general replacement for AC_CHECK_PROG.  Any characters in the
# program outside of the set of alphanumerics and underscores are
# normalised to underscores.
#
# The optional second argument gives the name of the component containing
# the program in question.  Some packages install their binaries in
# package-specific directories, and this argument allows this macro to
# look there as well.
#
# For example:
#     STAR_CHECK_PROGS(messgen)
# would define the variable MESSGEN to have the full path to the
# messgen application, and 
#     STAR_CHECK_PROGS(prolat, sst)
# would define the variable PROLAT to have the path to the prolat
# application within the sst component.
#
# Calls AC_SUBST and AC_ARG_VAR on the generated variable name.  This
# macro does _not_ automatically declare a configure dependency on any
# component specified in the second argument.  These dependencies should
# be kept to an absolute minimum, and therefore any such dependencies
# must be declared obviously and explicitly, with rationale.
#
# The behaviour described below, for the result when the required program
# is not found, is not final, and may change.  The documentation below is
# contradictory, and should be regarded merely as a rather confused
# discussion of the issues.  The current behaviour is that when the progam
# is not found, the variable is defined to be the program's name without
# any path at all.
#
# This is the analogue of AC_CHECK_PROG, except that: (1) the variable
# name defaults to the program name, (2) the variable value if the
# program is not found is the path to the anticipated installation
# location of the program, so that the macro does not fail in this
# case.  This is useful for locating Starlink programs, as it means we
# can use this macro to produce absolute paths to programs, even
# before they have been installed (in this case we are presumably
# doing a top-level configure of the Starlink tree, and the Makefile
# will ensure that the required files are installed before the current
# package actually uses it.  NB: (2) is not true at present.
#
# The current value of the PATH variable is augmented by the location
# of the binary installation directory, using the current default
# value of the prefix (not ideal, since this may in principle change
# when the component being configured is installed, but it's the best
# we can do at configure time); and by the $STARLINK/bin directory.
#
# The default, if the program isn't in the augmented path, is the path
# to the starconf-finder program if that's available, and the bare
# program-name otherwise.  Is this the best default?  Would just 
# program-name be better?  The program may not be in the augmented
# path for two reasons: (1) we are doing the global configuration done
# during bootstrapping, and noting has been installed yet; or (2) the
# program is one of those installed in a subdirectory of the
# `bindir'.  In case (2), there's not a lot we can do, short of
# grubbing round manifest files at some point, but the
# starconf-finder, which is the eventual default, knows about this
# case, and could take care of it.
#
# No, I've changed my mind again.  If the program isn't found, then
# simply have the AC_PATH_PROG default to bare ProgramName.  This is
# probably adequate, and if so probably more robust than relying on
# more and more layers of indirection.  We probably will need to
# revisit this.  Again.
AC_DEFUN([STAR_CHECK_PROGS],
         [eval default_bindir=`echo $bindir | sed 's,\${exec_prefix},$ac_default_prefix,'`
          AC_FOREACH([ProgramName], [$1],
                     [m4_define([star_prog],
                                _STAR_UPCASE(m4_bpatsubst(ProgramName,
                                                          [[^0-9a-zA-Z_]], 
                                                          [_])))
                      AC_PATH_PROG(star_prog,
                                   ProgramName,
                                   ProgramName,
[$STARLINK/Perl/bin:]dnl
[$STARLINK/starjava/bin:]dnl
[$STARLINK/bin:]m4_ifval([$2],[$STARLINK/bin/$2:],)dnl
[$default_bindir:]m4_ifval([$2],[$default_bindir/$2:],)dnl
[$PATH])
                      AC_ARG_VAR(star_prog,
                                 [Location of the ]ProgramName[ application])])
])# STAR_CHECK_PROGS


# STAR_SPECIAL_INSTALL_COMMAND(cmd)
# ---------------------------------
# Declare a special install command.  Note that we do not examine the
# actual command here -- that is done by automake.  All we do is find
# a way of copying a directory tree, preserving symlinks, as used by
# the install targets in automake/lib/am/install.am.  Try 'cp -R' and
# variants, then pax, and if both fail, collapse.
dnl Link test is `test -h': more portable than -L, according to autoconf notes.
dnl `cp --no-dereference' is GNU cp: -P gives a compatibility warning.
dnl Include broken link in test: some cp fail to copy these (OSX 10.2, Sol9).
dnl Option -f is probably a good plan, but no failures spotted so far.
dnl In pax, `-p e' fails with broken links; `-p p' is OK.
AC_DEFUN([STAR_SPECIAL_INSTALL_COMMAND],
   [AC_REQUIRE([AC_PROG_LN_S])dnl
    AC_PATH_PROG(CP, cp)dnl
    AC_PATH_PROG(PAX, pax)
    AC_CACHE_CHECK([how to do a recursive directory copy],
                   [star_cv_cp_r],
                   [rm -Rf conftest*
                    mkdir conftest-d1 conftest-d2
                    mkdir conftest-d1/d
                    date >conftest-d1/d/f
                    (cd conftest-d1/d; $LN_S f l; $LN_S x broken)
                    if test ! -h conftest-d1/d/l; then
                        # We don't have links!  So plain cp -R will do
                        star_cv_cp_r="$CP -R"
                    else
                        star_cv_cp_r=
                        for try in "$CP -R --no-dereference -p -f" "$CP -R -P -p -f" "$CP -R -P -p" "$CP -R -p" "${PAX-false} -r -w -p p"
                        do
                            rm -Rf conftest-d2/*
                            if (cd conftest-d1; $try . ../conftest-d2 2>/dev/null); then
                                if test -h conftest-d2/d/l -a -h conftest-d2/d/broken; then
                                    star_cv_cp_r="$try"
                                    break
                                fi
                            fi
                        done
                    fi
                    rm -Rf conftest*])
    if test -z "$star_cv_cp_r"; then
        AC_MSG_ERROR([unable to find working cp or pax])
    fi
    AC_SUBST(CP_RECURSIVE, $star_cv_cp_r)dnl
])# STAR_SPECIAL_INSTALL_COMMAND
    

# STAR_MONOLITHS
# --------------
# Declare that we will be creating monoliths.  This does whatever
# configuration is necessary to handle these.
#
# Note that the declarations done in the Makefile.am, declaring the
# name of the monolith and the names and source files of the tasks,
# are slightly redundant inasmuch as some of that information could be
# implied.  However, this is required to be explicit for clarity and
# consistency, and so accomodate the (currently unexploited)
# possibility that the tasks and .ifl files longer have the
# one-task-per-file relationship they have now.
AC_DEFUN([STAR_MONOLITHS],
         [$_star_docs_only &&
             AC_MSG_ERROR([STAR[]_MONOLITHS in docs-only directory])
          dnl Installation in monoliths.am uses $(LN_S)
          AC_REQUIRE([AC_PROG_LN_S])dnl

          # To build monoliths, we need both compifl to build the .ifc
          # files (in the parsecon component), and alink
          # to link the monoliths (in dtask).  Both are now part of
          # the pcs component.
          STAR_DECLARE_DEPENDENCIES(build, [pcs])

          # So try to find alink and compifl.
          STAR_CHECK_PROGS([compifl alink])

          # When we're building monoliths, we will almost certainly be
          # using Fortran, and so we might as well include this,
          # partly in case the user forgets, but also because this is
          # reasonably part of the default setup required for monoliths.
          STAR_CNF_COMPATIBLE_SYMBOLS
          STAR_PRM_COMPATIBLE_SYMBOLS
])# STAR_MONOLITHS


# STAR_HELP_FILES(helpfiles)
# --------------------------
# Declare a list of files to be installed into the Starlink help
# directory.  This can be used both internally and in user
# configure.ac files.
AC_DEFUN([STAR_HELP_FILES],
	 [_STAR_EXTRADIR_COMMON([help], [$1])])


# STAR_ETC_FILES(etcfiles)
# ------------------------
# Declare a list of files to be installed into the Starlink etc
# directory.  This can be used both internally and in user
# configure.ac files.
AC_DEFUN([STAR_ETC_FILES],
         [_STAR_EXTRADIR_COMMON([etc], [$1])])


# STAR_DOCS_FILES(docfiles)
# -------------------------
# Declare a list of files to be installed into the Starlink
# documentation directory.  This can be used both internally and in
# user configure.ac files.
AC_DEFUN([STAR_DOCS_FILES],
         [_STAR_EXTRADIR_COMMON([docs], [$1])])


# STAR_EXAMPLES_FILES(examplesfiles)
# ----------------------------------
# Declare a list of files to be installed into the Starlink
# examples directory.  This can be used both internally and in
# user configure.ac files.
AC_DEFUN([STAR_EXAMPLES_FILES],
         [_STAR_EXTRADIR_COMMON([examples], [$1])])


# STAR_DECLARE_DEPENDENCIES(type, deplist, option='')
# ---------------------------------------------------
#
# Declare dependencies of this component.  The TYPE is one of
# `sourceset', `build', `link', `use', `test' or `configure', and the
# DEPLIST is a space separated list of component names, which this
# component depends on in the given way.
#
# -- Sourceset dependencies are those components which must be
# installed in order to build the complete set of sources, either for
# building or for distribution.  This includes documentation, so it
# would include star2html as well as messgen.
#
# -- Build dependencies are those which are required in order to build
# this component.  This typically means include files, but if part of
# the component is an executable file (such as compifl within the
# parsecon component), then that's a build dependence also (but see
# the discussion of `option', below).  You may not have two components
# which have a build dependency on each other, since that would mean
# that each would have to be built before the other, which is
# impossible.
#
# -- Link dependencies are those required to link against the
# libraries in a component.  That means all the libraries that this
# component's libraries use.  These are not necessarily build
# dependencies, since if you are building a library, any called
# libraries don't have to be present in order to build this library;
# you can have two components which have mutual link dependencies.  If
# you are building an application, however, then all its link
# dependencies will actually be build dependencies and should be
# declared as such.  In other words, the distinction between build and
# link dependencies is important only for library components.
#
# -- Use dependencies are those which are required in order for the
# component to be used by something else, after it has been built and
# installed.  For example a library which called another application
# as part of its functionality would have only a use dependency on the
# component which contained that application.  If no use dependencies
# are declared, we take the use dependencies to be the same as the
# link dependencies.
#
# -- Test dependencies are those which are required in order to run
# any regression tests which come with the component.  It's generally
# a good idea to avoid making this a larger set than the use
# dependencies, but sometimes this is unavoidable.  If no test
# dependencies are declared, we take the test dependencies to be the
# same as the use dependencies.
#
# -- Configure dependencies are those which must be satisfied before
# this component can be successfully configured.  In this case, we
# also check that the corresponding manifest files have been installed
# in current_MANIFESTS, and if not exit with a message, and the suggestion
# that the user runs 'make configure-deps'.
#
# The point of this is that different dependencies are required at
# different times.  The set of dependencies in the master makefile is
# composed of all the `sourceset' and `build' dependencies, but not
# `link' or `use' dependencies, and since the core Starlink libraries
# are closely interdependent, the set of `build' dependencies needs to
# be kept as small as possible in order to avoid circularities (that
# is, A depending on B, which depends, possibly indirectly, on A).
#
# All these relationships are transitive: if A has a build dependency
# on B, and B has one on C, then A has a build dependency on C.  You
# can augment this by using the final `option' argument: if, in
# component A's declaration element you say
# STAR_DECLARE_DEPENDENCIES(build, B, link), then you declare that A
# has a build-time dependency on B, but that (presumably because you
# are building an application within a component which is mostly
# libraries) you need to link against B, so component A has a
# dependency on all of B's _link_ dependencies, not just its build
# dependencies.  This is (I believe) the only case where this `option'
# attribute is useful, though it is legal for each of the dependency types.
#
# You need only declare direct dependencies.  If package A depends on
# package B, which depends in turn on package C, then package A need
# not declare a dependency on C.
#
# The macro may be called more than once.  The results of this macro
# are expressed in the file component.xml in the component directory.
AC_DEFUN([STAR_DECLARE_DEPENDENCIES],
 [m4_ifval([$1], [], [AC_FATAL([$0: no type given])])dnl
  m4_if(m4_bregexp([$1], 
                   [^\(sourceset\|build\|link\|use\|test\|configure\)$]),
        [0],
        [],
        [AC_FATAL([$0: unrecognised dependency type: $1])])dnl
  m4_ifval([$2], [], [AC_FATAL([$0: no deplist given])])dnl
  for _star_tmp in $2
  do
    STAR_DEPENDENCIES_CHILDREN="$STAR_DEPENDENCIES_CHILDREN<[$1]m4_ifval([$3], [ option='$3'], [])>$_star_tmp</$1>"
  done
  m4_if([$1], [configure], [# check that configure-deps ran...
  for _star_tmp in $2
  do
    echo "$as_me:$LINENO: checking for configure-deps/$_star_tmp" >&5
    echo $ECHO_N "checking for configure-deps/$_star_tmp... $ECHO_C" >&6
    if test -f $current_MANIFESTS/$_star_tmp; then
      echo "$as_me:$LINENO: result: ok" >&5
      echo "${ECHO_T}ok" >&6
    else
      echo "$as_me:$LINENO: result: not found!" >&5
      echo "${ECHO_T}not found" >&6
      echo "*** This package has a configure dependency on $_star_tmp" >&6
      echo "    but that component doesn't appear to be installed." >&6
      echo "    (I can't find $current_MANIFESTS/$_star_tmp:" >&6
      echo "    have you forgotten to run 'make configure-deps'?)" >&6
      echo "    Giving up!" >&6
      exit 1
    fi
  done
])dnl
])# STAR_DECLARE_DEPENDENCIES


# STAR_PLATFORM_SOURCES(target-file-list, platform-list)
# ------------------------------------------------------
#
# Generate the given target-file for each of the files in the list
# TARGET-FILE-LIST, by selecting the appropriate element of the
# PLATFORM-LIST based on the value of [AC_CANONICAL_BUILD].  Both
# lists are space-separated lists.
#
# For each of the platforms, <p>, in platform-list, there should be a
# file `<target-file><p>'.  There should always be a file
# `<target-file>default', and if none of the platform-list strings
# matches, this is the file which is used.  If the `default' file is
# listed in the `platform-list', then it is matched in the normal run
# of things; if it is not listed, it still matches, but a warning is
# issued.
#
# If you wish no match _not_ to be an error -- perhaps because there
# is a platform-dependent file which is redundant on unlisted platforms
# -- then end the platform-list with `NONE'.  In this case, if no file
# matches, then no link is made, with no error or warning.
#
# This macro uses the results of ./config.guess to determine the
# current platform.  That returns a triple consisting of
# cpu-vendor-os, such as `i686-pc-linux-gnu' (OS=linux-gnu),
# `sparc-sun-solaris2.9', or `alphaev6-dec-osf5.1'
#
# The extensions <p> in platform-list should all have the form
# `cpu_vendor[_os]', where each of the components `cpu', `vendor' and
# `os' may be blank.  If not blank, they are matched as a prefix of
# the corresponding part of the config.guess value.  Thus
# `_sun_solaris' would match `sparc-sun-solaris2.9' but not
# `sparc-sun-sunos', and `_sun' would match both.  For a <target-file>
# file foo.c, this would result in `ln -s foo.c_sun foo.c'
#
# Calls AC_LIBSOURCE for each of the implied platform-specific files.
#
AC_DEFUN([STAR_PLATFORM_SOURCES],
         [
$_star_docs_only && AC_MSG_ERROR([STAR_[]PLATFORM_SOURCES in docs-only dir])
AC_REQUIRE([AC_CANONICAL_BUILD])dnl
m4_ifval([$1], [], [AC_FATAL([$0: no target-file-list given])])dnl
m4_ifval([$2], [], [AC_FATAL([$0: no platform-list given])])dnl
AC_FOREACH([TargetFile], [$1],
  [AC_FOREACH([Ext], [$2], 
    [m4_if(Ext, [NONE], , [AC_LIBSOURCE(TargetFile[]Ext)])])])dnl
AC_MSG_CHECKING([platform-specific source for file(s) $1])
_star_tmp=
for platform in $2
do
    if test $platform = NONE; then
        # Special case -- no file required
        _star_tmp=NONE
        break;
    fi
    if test $platform = default; then
        _star_tmp=default
        break;
    fi
    if expr $build : `echo $platform | sed 's/_/.*-/g'` >/dev/null; then
        _star_tmp=$platform
        break;
    fi
done
if test -z "$_star_tmp"; then
    # Use default, but it wasn't listed in the platform-list
    # (though it should have been)
    AC_MSG_WARN([build platform $build does not match any of ($2): using `default'])
    _star_tmp=default
fi    
if test $_star_tmp = NONE; then
    AC_MSG_RESULT([none required])
else
    AC_MSG_RESULT([using $_star_tmp])
    for _t in $1
    do
        if test -f $srcdir/$_t$_star_tmp; then
            (cd $srcdir; rm -f $_t; cp -p $_t$_star_tmp $_t)
        else
            AC_MSG_WARN([platform $_star_tmp matched, but no file $_t$_star_tmp found])
        fi
    done
fi
])# STAR_PLATFORM_SOURCES


# STAR_INITIALISE_FORTRAN_RTL
# ---------------------------
#
# Define a macro which can be used in a C main program to initialise the
# Fortran RTL, including, for example, doing whatever work is required so that
# the Fortran getarg() function works.  This defines the macro
# STAR_INITIALISE_FORTRAN(argc,argv).  The implementation necessarily uses
# functions which are specific to the Fortran implementation, and the body of
# this macro is basically a switch to determine the compiler and thus the
# appropriate compiler-specific magic.  If no implementation is available,
# then the macro should expand to nothing.
#
# Note that the Starlink functions wrapping getarg() are robust against
# getarg() failing because this information is not available.  This function
# is nonetheless necessary because some platforms have link problems otherwise
# (specifically OSX, on which the most readily available compiler is g77,
# cannot link properly if the getarg() function is referenced by a library,
# but there is a C main function, so that the Fortran main function's call of
# f_setarg is omitted).  Thus it is generally harmless to leave this function
# unimplemented on those platforms which do not have these link problems, and
# it is harmless that the test below is extremely compiler specific (though we
# would probably have to add implementations for any other compilers used on
# OSX).  It's also generally harmless not to call the defined function, or
# invoke this macro, if your application doesn't have the link problems which
# makeit necessary, though of course calling it will make getarg() work where
# it otherwise wouldn't, which may be an advantage.
#
# All was well until g95 and gfortran, these are "gnu" compilers, but use
# different semantics. In the case of g95 the calling the startup code is not
# optional (docs say that heap initialisation relies on the startup call).
#
# The test for g95 relies on the output from `g95 --version' containing the
# string "G95". Gfortran requires "GNU Fortran (GCC) 4+.x[x].x[x]".  Note that
# this whole area probably needs rethinking as g95 also has a g95_runtime_stop()
# function, that should be called.
#
# At gfortran 4.6 the call sequence stopped allowing a NULL argv, so a dummy
# version had to be added. The argv[0] value is always de-referenced in an
# an attempt to get the program name.
#
# Intel Fortran needs the for_rtl_init_ function, there is also a
# for_rtl_finish_ to run during closedown. The intel compiler signature
# is to have "IFORT" in the --version string.
#
# Under Solaris and the studio compilers the argc and argv values are no
# longer automatically shared, so we test for "Sun Fortran" and have a 
# code section that copies the given argc and argv directly to the global
# variable __xargc and __xargv, this may need fixing from time to time.
# Doesn't seem to be a function for doing this job.
#
AC_DEFUN([STAR_INITIALISE_FORTRAN_RTL],
   [AC_CACHE_CHECK([how to initialise the Fortran RTL],
       [star_cv_initialise_fortran],
       [AC_REQUIRE([AC_PROG_FC])
       if test "$ac_cv_fc_compiler_gnu" = yes; then
            if "$FC" --version 2>&1 < /dev/null | grep 'G95' > /dev/null; then
                star_cv_initialise_fortran=g95-start
            elif "$FC" --version 2>&1 < /dev/null | grep 'GNU Fortran.*[[4-9]]\.[[0-9]][[0-9]]*\.[[0-9]][[0-9]]*' > /dev/null; then
                star_cv_initialise_fortran=gfortran-setarg
            else
                star_cv_initialise_fortran=g77-setarg
            fi
        else
            if "$FC" --version 2>&1 < /dev/null | grep 'IFORT' > /dev/null; then
                star_cv_initialise_fortran=ifort-setarg
            elif "$FC" -V 2>&1 < /dev/null | grep 'Sun Fortran' > /dev/null; then
                star_cv_initialise_fortran=sunstudio-setarg
            else
                star_cv_initialise_fortran=
            fi
        fi])
    AH_TEMPLATE([STAR_INITIALISE_FORTRAN],
       [Define to a function call which will initialise the Fortran RTL])
    case "$star_cv_initialise_fortran" in
      g77-setarg)
        AC_DEFINE([STAR_INITIALISE_FORTRAN(argc,argv)],
                  [{extern void f_setarg(int,char**); f_setarg(argc, argv);}])
        ;;
      g95-start)
        AC_DEFINE([STAR_INITIALISE_FORTRAN(argc,argv)],
                  [{extern void g95_runtime_start(int,char**); g95_runtime_start(argc, argv);}])
        ;;
      gfortran-setarg)
        AC_DEFINE([STAR_INITIALISE_FORTRAN(argc,argv)],
                  [{extern void _gfortran_set_args(int,char**); if (argv == NULL) {static char *sc_dummy[[]]={NULL};_gfortran_set_args(0,sc_dummy);} else {_gfortran_set_args(argc,argv);}}])
        ;;
      ifort-setarg)
        AC_DEFINE([STAR_INITIALISE_FORTRAN(argc,argv)],
                  [{extern void for_rtl_init_(int*,char**); for_rtl_init_(&argc, argv);}])
        ;;
      sunstudio-setarg)
        AC_DEFINE([STAR_INITIALISE_FORTRAN(argc,argv)],
                  [{extern int __xargc; extern char **__xargv;__xargc = argc;__xargv = argv;}])
        ;;
      *) 
        AC_DEFINE([STAR_INITIALISE_FORTRAN(argc,argv)],[])
        ;;
    esac
dnl    AC_DEFINE_UNQUOTED([STAR_INITIALISE_FORTRAN(argc,argv)],
dnl                       $star_cv_initialise_fortran)
])# STAR_INITIALISE_FORTRAN


# STAR_SUPPRESS_BUILD_IF(test, message)
# -------------------------------------
# Call once at the end of the configure script.
#
# If the given shell test evaluates to true, then suppress the build,
# without having ./configure fail.  The test is any command which
# returns true if the build should be suppressed, and may be shell
# commands `true' or `false', or might be a more complicated test,
# such as `test -n "$SOMEENV"'.
#
# The macro communicates with the generated Makefile.in by creating a file
# STAR_SUPPRESS_BUILD if the test evaluates to true.  The file contains
# the text of the explanation.
AC_DEFUN([STAR_SUPPRESS_BUILD_IF],
   [m4_ifval([$1], [], [AC_FATAL([$0: needs two arguments])])dnl
    m4_ifval([$2], [], [AC_FATAL([$0: needs two arguments])])dnl
    rm -f STAR_SUPPRESS_BUILD
    if [$1]; then
        AC_MSG_WARN([Build inhibited:
        $2])
        echo "$2" >STAR_SUPPRESS_BUILD
        ALL_TARGET=all-am-suppress
    else
        ALL_TARGET=all-am-normal
    fi
    AC_SUBST(ALL_TARGET)
])# STAR_SUPPRESS_BUILD_IF


# starconf internal macros


# _STAR_UPCASE(string)
# --------------------
# Expands to STRING with all letters translated to uppercase.
AC_DEFUN([_STAR_UPCASE],
         [m4_translit([$1], [a-z], [A-Z])])


# _STAR_EXTRADIR_COMMON(dir-type, file-list)
# ------------------------------------------
#
# Common handler for STAR_HELP_FILES, etc.  DIR-TYPE is one of
#
#    help, etc, docs, examples
#
# and `FILE-LIST' is a list of files to be installed in
# the directory STAR_[DIR-TYPE]_DIR.  This works by defining and
# AC_SUBSTing the variables `starX_DATA for X=dir-type (eg, `stardocs_DATA').
#
# This is now obsolete -- components should use star<dir-type>_DATA in
# the Makefile.am file instead.  Don't use AC_[]DIAGNOSE([obsolete],...),
# since those warnings aren't turned on by default.
AC_DEFUN([_STAR_EXTRADIR_COMMON],
   [AC_FATAL([Macro STAR_]_STAR_UPCASE($1)[_FILES($2) is obsolete -- use star$1_DATA in Makefile.am instead])
    AC_FATAL([For STAR@&t@_LATEX_DOCUMENTATION, use stardocs_DATA=@STAR@&t@_LATEX_DOCUMENTATION@ instead])]
)# _STAR_EXTRADIR_COMMON


# STAR_LARGEFILE_SUPPORT
# ----------------------
#
# Set C macros for compiling C routines that want to make use of large file 
# support. This is a joining of AC_SYS_LARGEFILE and AC_FUNC_FSEEKO
# so defines the macros _FILE_OFFSET_BITS, _LARGEFILE_SOURCE and _LARGE_FILES,
# along with HAVE_FSEEKO. To use large file support you need to use fseeko and
# ftello when HAVE_FSEEKO is defined (and use off_t for offsets) and compile
# all C code with the other defines. 
#
# This function also gathers the values of _FILE_OFFSET_BITS, _LARGEFILE_SOURCE
# and _LARGE_FILES and sets the STAR_LARGEFILE_CFLAGS variable (this in useful
# for passing to packages which are not directly part of the starconf system).
#
AC_DEFUN([STAR_LARGEFILE_SUPPORT],
[dnl Enable autoconf largefile support.
AC_SYS_LARGEFILE
AC_FUNC_FSEEKO

# Gather state into a single variable for passing to other packages.
STAR_LARGEFILE_CFLAGS=
if test "$ac_cv_sys_file_offset_bits" != "no"; then
   STAR_LARGEFILE_CFLAGS="-D_FILE_OFFSET_BITS=$ac_cv_sys_file_offset_bits"
fi

if test "$ac_cv_sys_large_files" != "no"; then
   STAR_LARGEFILE_CFLAGS="-D_LARGE_FILES_=$ac_cv_sys_large_files $STAR_LARGEFILE_CFLAGS"
fi

if test "$ac_cv_sys_largefile_source" != "no"; then
   STAR_LARGEFILE_CFLAGS="-D_LARGEFILE_SOURCE=$ac_cv_sys_largefile_source $STAR_LARGEFILE_CFLAGS"
fi
])# STAR_LARGEFILE_SUPPORT


# Obsolete macros
# ===============

# STAR_HAVE_FC_OPEN_READONLY
# ---------------------------
#
# Tests if the Fortran compiler supports the READONLY option on the
# OPEN command.  If it does, it defines HAVE_FC_OPEN_READONLY to 1.
AC_DEFUN([STAR_HAVE_FC_OPEN_READONLY],
   [AC_FATAL([Macro STAR_HAVE_FC_OPEN_READONLY is obsolete; use AC_FC_OPEN_SPECIFIERS(readonly) instead])])


# STAR_FC_LIBRARY_LDFLAGS
# -----------------------
#
# This was once a wrapper for AC_[]FC_LIBRARY_LDFLAGS which added
# functionality, use AC_[]FC_LIBRARY_LDFLAGS instead.
AC_DEFUN([STAR_FC_LIBRARY_LDFLAGS],
   [AC_FATAL([Macro STAR_FC_LIBRARY_LDFLAGS is obsolete: if necessary, use standard AC_FC_LIBRARY_LDFLAGS instead])])


# end of starconf macros

# Copyright (C) 2002-2013 Free Software Foundation, Inc.
#
# This file is free software; the Free Software Foundation
# gives unlimited permission to copy and/or distribute it,
# with or without modifications, as long as this notice is preserved.

# AM_AUTOMAKE_VERSION(VERSION)
# ----------------------------
# Automake X.Y traces this macro to ensure aclocal.m4 has been
# generated from the m4 files accompanying Automake X.Y.
# (This private macro should not be called outside this file.)
AC_DEFUN([AM_AUTOMAKE_VERSION],
[am__api_version='1.14'
dnl Some users find AM_AUTOMAKE_VERSION and mistake it for a way to
dnl require some minimum version.  Point them to the right macro.
m4_if([$1], [1.14.1-starlink], [],
      [AC_FATAL([Do not call $0, use AM_INIT_AUTOMAKE([$1]).])])dnl
])

# _AM_AUTOCONF_VERSION(VERSION)
# -----------------------------
# aclocal traces this macro to find the Autoconf version.
# This is a private macro too.  Using m4_define simplifies
# the logic in aclocal, which can simply ignore this definition.
m4_define([_AM_AUTOCONF_VERSION], [])

# AM_SET_CURRENT_AUTOMAKE_VERSION
# -------------------------------
# Call AM_AUTOMAKE_VERSION and AM_AUTOMAKE_VERSION so they can be traced.
# This function is AC_REQUIREd by AM_INIT_AUTOMAKE.
AC_DEFUN([AM_SET_CURRENT_AUTOMAKE_VERSION],
[AM_AUTOMAKE_VERSION([1.14.1-starlink])dnl
m4_ifndef([AC_AUTOCONF_VERSION],
  [m4_copy([m4_PACKAGE_VERSION], [AC_AUTOCONF_VERSION])])dnl
_AM_AUTOCONF_VERSION(m4_defn([AC_AUTOCONF_VERSION]))])

# AM_AUX_DIR_EXPAND                                         -*- Autoconf -*-

# Copyright (C) 2001-2013 Free Software Foundation, Inc.
#
# This file is free software; the Free Software Foundation
# gives unlimited permission to copy and/or distribute it,
# with or without modifications, as long as this notice is preserved.

# For projects using AC_CONFIG_AUX_DIR([foo]), Autoconf sets
# $ac_aux_dir to '$srcdir/foo'.  In other projects, it is set to
# '$srcdir', '$srcdir/..', or '$srcdir/../..'.
#
# Of course, Automake must honor this variable whenever it calls a
# tool from the auxiliary directory.  The problem is that $srcdir (and
# therefore $ac_aux_dir as well) can be either absolute or relative,
# depending on how configure is run.  This is pretty annoying, since
# it makes $ac_aux_dir quite unusable in subdirectories: in the top
# source directory, any form will work fine, but in subdirectories a
# relative path needs to be adjusted first.
#
# $ac_aux_dir/missing
#    fails when called from a subdirectory if $ac_aux_dir is relative
# $top_srcdir/$ac_aux_dir/missing
#    fails if $ac_aux_dir is absolute,
#    fails when called from a subdirectory in a VPATH build with
#          a relative $ac_aux_dir
#
# The reason of the latter failure is that $top_srcdir and $ac_aux_dir
# are both prefixed by $srcdir.  In an in-source build this is usually
# harmless because $srcdir is '.', but things will broke when you
# start a VPATH build or use an absolute $srcdir.
#
# So we could use something similar to $top_srcdir/$ac_aux_dir/missing,
# iff we strip the leading $srcdir from $ac_aux_dir.  That would be:
#   am_aux_dir='\$(top_srcdir)/'`expr "$ac_aux_dir" : "$srcdir//*\(.*\)"`
# and then we would define $MISSING as
#   MISSING="\${SHELL} $am_aux_dir/missing"
# This will work as long as MISSING is not called from configure, because
# unfortunately $(top_srcdir) has no meaning in configure.
# However there are other variables, like CC, which are often used in
# configure, and could therefore not use this "fixed" $ac_aux_dir.
#
# Another solution, used here, is to always expand $ac_aux_dir to an
# absolute PATH.  The drawback is that using absolute paths prevent a
# configured tree to be moved without reconfiguration.

AC_DEFUN([AM_AUX_DIR_EXPAND],
[dnl Rely on autoconf to set up CDPATH properly.
AC_PREREQ([2.50])dnl
# expand $ac_aux_dir to an absolute path
am_aux_dir=`cd $ac_aux_dir && pwd`
])

# Do all the work for Automake.                             -*- Autoconf -*-

# Copyright (C) 1996-2013 Free Software Foundation, Inc.
#
# This file is free software; the Free Software Foundation
# gives unlimited permission to copy and/or distribute it,
# with or without modifications, as long as this notice is preserved.

# This macro actually does too much.  Some checks are only needed if
# your package does certain things.  But this isn't really a big deal.

dnl Redefine AC_PROG_CC to automatically invoke _AM_PROG_CC_C_O.
m4_define([AC_PROG_CC],
m4_defn([AC_PROG_CC])
[_AM_PROG_CC_C_O
])

# AM_INIT_AUTOMAKE(PACKAGE, VERSION, [NO-DEFINE])
# AM_INIT_AUTOMAKE([OPTIONS])
# -----------------------------------------------
# The call with PACKAGE and VERSION arguments is the old style
# call (pre autoconf-2.50), which is being phased out.  PACKAGE
# and VERSION should now be passed to AC_INIT and removed from
# the call to AM_INIT_AUTOMAKE.
# We support both call styles for the transition.  After
# the next Automake release, Autoconf can make the AC_INIT
# arguments mandatory, and then we can depend on a new Autoconf
# release and drop the old call support.
AC_DEFUN([AM_INIT_AUTOMAKE],
[AC_PREREQ([2.65])dnl
dnl Autoconf wants to disallow AM_ names.  We explicitly allow
dnl the ones we care about.
m4_pattern_allow([^AM_[A-Z]+FLAGS$])dnl
AC_REQUIRE([AM_SET_CURRENT_AUTOMAKE_VERSION])dnl
AC_REQUIRE([AC_PROG_INSTALL])dnl
if test "`cd $srcdir && pwd`" != "`pwd`"; then
  # Use -I$(srcdir) only when $(srcdir) != ., so that make's output
  # is not polluted with repeated "-I."
  AC_SUBST([am__isrc], [' -I$(srcdir)'])_AM_SUBST_NOTMAKE([am__isrc])dnl
  # test to see if srcdir already configured
  if test -f $srcdir/config.status; then
    AC_MSG_ERROR([source directory already configured; run "make distclean" there first])
  fi
fi

# test whether we have cygpath
if test -z "$CYGPATH_W"; then
  if (cygpath --version) >/dev/null 2>/dev/null; then
    CYGPATH_W='cygpath -w'
  else
    CYGPATH_W=echo
  fi
fi
AC_SUBST([CYGPATH_W])

# Define the identity of the package.
dnl Distinguish between old-style and new-style calls.
m4_ifval([$2],
[AC_DIAGNOSE([obsolete],
             [$0: two- and three-arguments forms are deprecated.])
m4_ifval([$3], [_AM_SET_OPTION([no-define])])dnl
 AC_SUBST([PACKAGE], [$1])dnl
 AC_SUBST([VERSION], [$2])],
[_AM_SET_OPTIONS([$1])dnl
dnl Diagnose old-style AC_INIT with new-style AM_AUTOMAKE_INIT.
m4_if(
  m4_ifdef([AC_PACKAGE_NAME], [ok]):m4_ifdef([AC_PACKAGE_VERSION], [ok]),
  [ok:ok],,
  [m4_fatal([AC_INIT should be called with package and version arguments])])dnl
 AC_SUBST([PACKAGE], ['AC_PACKAGE_TARNAME'])dnl
 AC_SUBST([VERSION], ['AC_PACKAGE_VERSION'])])dnl

_AM_IF_OPTION([no-define],,
[AC_DEFINE_UNQUOTED([PACKAGE], ["$PACKAGE"], [Name of package])
 AC_DEFINE_UNQUOTED([VERSION], ["$VERSION"], [Version number of package])])dnl

# Some tools Automake needs.
AC_REQUIRE([AM_SANITY_CHECK])dnl
AC_REQUIRE([AC_ARG_PROGRAM])dnl
AM_MISSING_PROG([ACLOCAL], [aclocal-${am__api_version}])
AM_MISSING_PROG([AUTOCONF], [autoconf])
AM_MISSING_PROG([AUTOMAKE], [automake-${am__api_version}])
AM_MISSING_PROG([AUTOHEADER], [autoheader])
AM_MISSING_PROG([MAKEINFO], [makeinfo])
AC_REQUIRE([AM_PROG_INSTALL_SH])dnl
AC_REQUIRE([AM_PROG_INSTALL_STRIP])dnl
AC_REQUIRE([AC_PROG_MKDIR_P])dnl
# For better backward compatibility.  To be removed once Automake 1.9.x
# dies out for good.  For more background, see:
# <http://lists.gnu.org/archive/html/automake/2012-07/msg00001.html>
# <http://lists.gnu.org/archive/html/automake/2012-07/msg00014.html>
AC_SUBST([mkdir_p], ['$(MKDIR_P)'])
# We need awk for the "check" target.  The system "awk" is bad on
# some platforms.
AC_REQUIRE([AC_PROG_AWK])dnl
AC_REQUIRE([AC_PROG_MAKE_SET])dnl
AC_REQUIRE([AM_SET_LEADING_DOT])dnl
_AM_IF_OPTION([tar-ustar], [_AM_PROG_TAR([ustar])],
	      [_AM_IF_OPTION([tar-pax], [_AM_PROG_TAR([pax])],
			     [_AM_PROG_TAR([v7])])])
_AM_IF_OPTION([no-dependencies],,
[AC_PROVIDE_IFELSE([AC_PROG_CC],
		  [_AM_DEPENDENCIES([CC])],
		  [m4_define([AC_PROG_CC],
			     m4_defn([AC_PROG_CC])[_AM_DEPENDENCIES([CC])])])dnl
AC_PROVIDE_IFELSE([AC_PROG_CXX],
		  [_AM_DEPENDENCIES([CXX])],
		  [m4_define([AC_PROG_CXX],
			     m4_defn([AC_PROG_CXX])[_AM_DEPENDENCIES([CXX])])])dnl
AC_PROVIDE_IFELSE([AC_PROG_OBJC],
		  [_AM_DEPENDENCIES([OBJC])],
		  [m4_define([AC_PROG_OBJC],
			     m4_defn([AC_PROG_OBJC])[_AM_DEPENDENCIES([OBJC])])])dnl
AC_PROVIDE_IFELSE([AC_PROG_OBJCXX],
		  [_AM_DEPENDENCIES([OBJCXX])],
		  [m4_define([AC_PROG_OBJCXX],
			     m4_defn([AC_PROG_OBJCXX])[_AM_DEPENDENCIES([OBJCXX])])])dnl
])
AC_REQUIRE([AM_SILENT_RULES])dnl
dnl The testsuite driver may need to know about EXEEXT, so add the
dnl 'am__EXEEXT' conditional if _AM_COMPILER_EXEEXT was seen.  This
dnl macro is hooked onto _AC_COMPILER_EXEEXT early, see below.
AC_CONFIG_COMMANDS_PRE(dnl
[m4_provide_if([_AM_COMPILER_EXEEXT],
  [AM_CONDITIONAL([am__EXEEXT], [test -n "$EXEEXT"])])])dnl

# POSIX will say in a future version that running "rm -f" with no argument
# is OK; and we want to be able to make that assumption in our Makefile
# recipes.  So use an aggressive probe to check that the usage we want is
# actually supported "in the wild" to an acceptable degree.
# See automake bug#10828.
# To make any issue more visible, cause the running configure to be aborted
# by default if the 'rm' program in use doesn't match our expectations; the
# user can still override this though.
if rm -f && rm -fr && rm -rf; then : OK; else
  cat >&2 <<'END'
Oops!

Your 'rm' program seems unable to run without file operands specified
on the command line, even when the '-f' option is present.  This is contrary
to the behaviour of most rm programs out there, and not conforming with
the upcoming POSIX standard: <http://austingroupbugs.net/view.php?id=542>

Please tell bug-automake@gnu.org about your system, including the value
of your $PATH and any error possibly output before this message.  This
can help us improve future automake versions.

END
  if test x"$ACCEPT_INFERIOR_RM_PROGRAM" = x"yes"; then
    echo 'Configuration will proceed anyway, since you have set the' >&2
    echo 'ACCEPT_INFERIOR_RM_PROGRAM variable to "yes"' >&2
    echo >&2
  else
    cat >&2 <<'END'
Aborting the configuration process, to ensure you take notice of the issue.

You can download and install GNU coreutils to get an 'rm' implementation
that behaves properly: <http://www.gnu.org/software/coreutils/>.

If you want to complete the configuration process using your problematic
'rm' anyway, export the environment variable ACCEPT_INFERIOR_RM_PROGRAM
to "yes", and re-run configure.

END
    AC_MSG_ERROR([Your 'rm' program is bad, sorry.])
  fi
fi])

dnl Hook into '_AC_COMPILER_EXEEXT' early to learn its expansion.  Do not
dnl add the conditional right here, as _AC_COMPILER_EXEEXT may be further
dnl mangled by Autoconf and run in a shell conditional statement.
m4_define([_AC_COMPILER_EXEEXT],
m4_defn([_AC_COMPILER_EXEEXT])[m4_provide([_AM_COMPILER_EXEEXT])])

# When config.status generates a header, we must update the stamp-h file.
# This file resides in the same directory as the config header
# that is generated.  The stamp files are numbered to have different names.

# Autoconf calls _AC_AM_CONFIG_HEADER_HOOK (when defined) in the
# loop where config.status creates the headers, so we can generate
# our stamp files there.
AC_DEFUN([_AC_AM_CONFIG_HEADER_HOOK],
[# Compute $1's index in $config_headers.
_am_arg=$1
_am_stamp_count=1
for _am_header in $config_headers :; do
  case $_am_header in
    $_am_arg | $_am_arg:* )
      break ;;
    * )
      _am_stamp_count=`expr $_am_stamp_count + 1` ;;
  esac
done
echo "timestamp for $_am_arg" >`AS_DIRNAME(["$_am_arg"])`/stamp-h[]$_am_stamp_count])

# Copyright (C) 2001-2013 Free Software Foundation, Inc.
#
# This file is free software; the Free Software Foundation
# gives unlimited permission to copy and/or distribute it,
# with or without modifications, as long as this notice is preserved.

# AM_PROG_INSTALL_SH
# ------------------
# Define $install_sh.
AC_DEFUN([AM_PROG_INSTALL_SH],
[AC_REQUIRE([AM_AUX_DIR_EXPAND])dnl
if test x"${install_sh}" != xset; then
  case $am_aux_dir in
  *\ * | *\	*)
    install_sh="\${SHELL} '$am_aux_dir/install-sh'" ;;
  *)
    install_sh="\${SHELL} $am_aux_dir/install-sh"
  esac
fi
AC_SUBST([install_sh])])

# Copyright (C) 2003-2013 Free Software Foundation, Inc.
#
# This file is free software; the Free Software Foundation
# gives unlimited permission to copy and/or distribute it,
# with or without modifications, as long as this notice is preserved.

# Check whether the underlying file-system supports filenames
# with a leading dot.  For instance MS-DOS doesn't.
AC_DEFUN([AM_SET_LEADING_DOT],
[rm -rf .tst 2>/dev/null
mkdir .tst 2>/dev/null
if test -d .tst; then
  am__leading_dot=.
else
  am__leading_dot=_
fi
rmdir .tst 2>/dev/null
AC_SUBST([am__leading_dot])])

# Fake the existence of programs that GNU maintainers use.  -*- Autoconf -*-

# Copyright (C) 1997-2013 Free Software Foundation, Inc.
#
# This file is free software; the Free Software Foundation
# gives unlimited permission to copy and/or distribute it,
# with or without modifications, as long as this notice is preserved.

# AM_MISSING_PROG(NAME, PROGRAM)
# ------------------------------
AC_DEFUN([AM_MISSING_PROG],
[AC_REQUIRE([AM_MISSING_HAS_RUN])
$1=${$1-"${am_missing_run}$2"}
AC_SUBST($1)])

# AM_MISSING_HAS_RUN
# ------------------
# Define MISSING if not defined so far and test if it is modern enough.
# If it is, set am_missing_run to use it, otherwise, to nothing.
AC_DEFUN([AM_MISSING_HAS_RUN],
[AC_REQUIRE([AM_AUX_DIR_EXPAND])dnl
AC_REQUIRE_AUX_FILE([missing])dnl
if test x"${MISSING+set}" != xset; then
  case $am_aux_dir in
  *\ * | *\	*)
    MISSING="\${SHELL} \"$am_aux_dir/missing\"" ;;
  *)
    MISSING="\${SHELL} $am_aux_dir/missing" ;;
  esac
fi
# Use eval to expand $SHELL
if eval "$MISSING --is-lightweight"; then
  am_missing_run="$MISSING "
else
  am_missing_run=
  AC_MSG_WARN(['missing' script is too old or missing])
fi
])

# Helper functions for option handling.                     -*- Autoconf -*-

# Copyright (C) 2001-2013 Free Software Foundation, Inc.
#
# This file is free software; the Free Software Foundation
# gives unlimited permission to copy and/or distribute it,
# with or without modifications, as long as this notice is preserved.

# _AM_MANGLE_OPTION(NAME)
# -----------------------
AC_DEFUN([_AM_MANGLE_OPTION],
[[_AM_OPTION_]m4_bpatsubst($1, [[^a-zA-Z0-9_]], [_])])

# _AM_SET_OPTION(NAME)
# --------------------
# Set option NAME.  Presently that only means defining a flag for this option.
AC_DEFUN([_AM_SET_OPTION],
[m4_define(_AM_MANGLE_OPTION([$1]), [1])])

# _AM_SET_OPTIONS(OPTIONS)
# ------------------------
# OPTIONS is a space-separated list of Automake options.
AC_DEFUN([_AM_SET_OPTIONS],
[m4_foreach_w([_AM_Option], [$1], [_AM_SET_OPTION(_AM_Option)])])

# _AM_IF_OPTION(OPTION, IF-SET, [IF-NOT-SET])
# -------------------------------------------
# Execute IF-SET if OPTION is set, IF-NOT-SET otherwise.
AC_DEFUN([_AM_IF_OPTION],
[m4_ifset(_AM_MANGLE_OPTION([$1]), [$2], [$3])])

# Check to make sure that the build environment is sane.    -*- Autoconf -*-

# Copyright (C) 1996-2013 Free Software Foundation, Inc.
#
# This file is free software; the Free Software Foundation
# gives unlimited permission to copy and/or distribute it,
# with or without modifications, as long as this notice is preserved.

# AM_SANITY_CHECK
# ---------------
AC_DEFUN([AM_SANITY_CHECK],
[AC_MSG_CHECKING([whether build environment is sane])
# Reject unsafe characters in $srcdir or the absolute working directory
# name.  Accept space and tab only in the latter.
am_lf='
'
case `pwd` in
  *[[\\\"\#\$\&\'\`$am_lf]]*)
    AC_MSG_ERROR([unsafe absolute working directory name]);;
esac
case $srcdir in
  *[[\\\"\#\$\&\'\`$am_lf\ \	]]*)
    AC_MSG_ERROR([unsafe srcdir value: '$srcdir']);;
esac

# Do 'set' in a subshell so we don't clobber the current shell's
# arguments.  Must try -L first in case configure is actually a
# symlink; some systems play weird games with the mod time of symlinks
# (eg FreeBSD returns the mod time of the symlink's containing
# directory).
if (
   am_has_slept=no
   for am_try in 1 2; do
     echo "timestamp, slept: $am_has_slept" > conftest.file
     set X `ls -Lt "$srcdir/configure" conftest.file 2> /dev/null`
     if test "$[*]" = "X"; then
	# -L didn't work.
	set X `ls -t "$srcdir/configure" conftest.file`
     fi
     if test "$[*]" != "X $srcdir/configure conftest.file" \
	&& test "$[*]" != "X conftest.file $srcdir/configure"; then

	# If neither matched, then we have a broken ls.  This can happen
	# if, for instance, CONFIG_SHELL is bash and it inherits a
	# broken ls alias from the environment.  This has actually
	# happened.  Such a system could not be considered "sane".
	AC_MSG_ERROR([ls -t appears to fail.  Make sure there is not a broken
  alias in your environment])
     fi
     if test "$[2]" = conftest.file || test $am_try -eq 2; then
       break
     fi
     # Just in case.
     sleep 1
     am_has_slept=yes
   done
   test "$[2]" = conftest.file
   )
then
   # Ok.
   :
else
   AC_MSG_ERROR([newly created file is older than distributed files!
Check your system clock])
fi
AC_MSG_RESULT([yes])
# If we didn't sleep, we still need to ensure time stamps of config.status and
# generated files are strictly newer.
am_sleep_pid=
if grep 'slept: no' conftest.file >/dev/null 2>&1; then
  ( sleep 1 ) &
  am_sleep_pid=$!
fi
AC_CONFIG_COMMANDS_PRE(
  [AC_MSG_CHECKING([that generated files are newer than configure])
   if test -n "$am_sleep_pid"; then
     # Hide warnings about reused PIDs.
     wait $am_sleep_pid 2>/dev/null
   fi
   AC_MSG_RESULT([done])])
rm -f conftest.file
])

# Copyright (C) 2009-2013 Free Software Foundation, Inc.
#
# This file is free software; the Free Software Foundation
# gives unlimited permission to copy and/or distribute it,
# with or without modifications, as long as this notice is preserved.

# AM_SILENT_RULES([DEFAULT])
# --------------------------
# Enable less verbose build rules; with the default set to DEFAULT
# ("yes" being less verbose, "no" or empty being verbose).
AC_DEFUN([AM_SILENT_RULES],
[AC_ARG_ENABLE([silent-rules], [dnl
AS_HELP_STRING(
  [--enable-silent-rules],
  [less verbose build output (undo: "make V=1")])
AS_HELP_STRING(
  [--disable-silent-rules],
  [verbose build output (undo: "make V=0")])dnl
])
case $enable_silent_rules in @%:@ (((
  yes) AM_DEFAULT_VERBOSITY=0;;
   no) AM_DEFAULT_VERBOSITY=1;;
    *) AM_DEFAULT_VERBOSITY=m4_if([$1], [yes], [0], [1]);;
esac
dnl
dnl A few 'make' implementations (e.g., NonStop OS and NextStep)
dnl do not support nested variable expansions.
dnl See automake bug#9928 and bug#10237.
am_make=${MAKE-make}
AC_CACHE_CHECK([whether $am_make supports nested variables],
   [am_cv_make_support_nested_variables],
   [if AS_ECHO([['TRUE=$(BAR$(V))
BAR0=false
BAR1=true
V=1
am__doit:
	@$(TRUE)
.PHONY: am__doit']]) | $am_make -f - >/dev/null 2>&1; then
  am_cv_make_support_nested_variables=yes
else
  am_cv_make_support_nested_variables=no
fi])
if test $am_cv_make_support_nested_variables = yes; then
  dnl Using '$V' instead of '$(V)' breaks IRIX make.
  AM_V='$(V)'
  AM_DEFAULT_V='$(AM_DEFAULT_VERBOSITY)'
else
  AM_V=$AM_DEFAULT_VERBOSITY
  AM_DEFAULT_V=$AM_DEFAULT_VERBOSITY
fi
AC_SUBST([AM_V])dnl
AM_SUBST_NOTMAKE([AM_V])dnl
AC_SUBST([AM_DEFAULT_V])dnl
AM_SUBST_NOTMAKE([AM_DEFAULT_V])dnl
AC_SUBST([AM_DEFAULT_VERBOSITY])dnl
AM_BACKSLASH='\'
AC_SUBST([AM_BACKSLASH])dnl
_AM_SUBST_NOTMAKE([AM_BACKSLASH])dnl
])

# Copyright (C) 2001-2013 Free Software Foundation, Inc.
#
# This file is free software; the Free Software Foundation
# gives unlimited permission to copy and/or distribute it,
# with or without modifications, as long as this notice is preserved.

# AM_PROG_INSTALL_STRIP
# ---------------------
# One issue with vendor 'install' (even GNU) is that you can't
# specify the program used to strip binaries.  This is especially
# annoying in cross-compiling environments, where the build's strip
# is unlikely to handle the host's binaries.
# Fortunately install-sh will honor a STRIPPROG variable, so we
# always use install-sh in "make install-strip", and initialize
# STRIPPROG with the value of the STRIP variable (set by the user).
AC_DEFUN([AM_PROG_INSTALL_STRIP],
[AC_REQUIRE([AM_PROG_INSTALL_SH])dnl
# Installed binaries are usually stripped using 'strip' when the user
# run "make install-strip".  However 'strip' might not be the right
# tool to use in cross-compilation environments, therefore Automake
# will honor the 'STRIP' environment variable to overrule this program.
dnl Don't test for $cross_compiling = yes, because it might be 'maybe'.
if test "$cross_compiling" != no; then
  AC_CHECK_TOOL([STRIP], [strip], :)
fi
INSTALL_STRIP_PROGRAM="\$(install_sh) -c -s"
AC_SUBST([INSTALL_STRIP_PROGRAM])])

# Copyright (C) 2006-2013 Free Software Foundation, Inc.
#
# This file is free software; the Free Software Foundation
# gives unlimited permission to copy and/or distribute it,
# with or without modifications, as long as this notice is preserved.

# _AM_SUBST_NOTMAKE(VARIABLE)
# ---------------------------
# Prevent Automake from outputting VARIABLE = @VARIABLE@ in Makefile.in.
# This macro is traced by Automake.
AC_DEFUN([_AM_SUBST_NOTMAKE])

# AM_SUBST_NOTMAKE(VARIABLE)
# --------------------------
# Public sister of _AM_SUBST_NOTMAKE.
AC_DEFUN([AM_SUBST_NOTMAKE], [_AM_SUBST_NOTMAKE($@)])

# Check how to create a tarball.                            -*- Autoconf -*-

# Copyright (C) 2004-2013 Free Software Foundation, Inc.
#
# This file is free software; the Free Software Foundation
# gives unlimited permission to copy and/or distribute it,
# with or without modifications, as long as this notice is preserved.

# _AM_PROG_TAR(FORMAT)
# --------------------
# Check how to create a tarball in format FORMAT.
# FORMAT should be one of 'v7', 'ustar', or 'pax'.
#
# Substitute a variable $(am__tar) that is a command
# writing to stdout a FORMAT-tarball containing the directory
# $tardir.
#     tardir=directory && $(am__tar) > result.tar
#
# Substitute a variable $(am__untar) that extract such
# a tarball read from stdin.
#     $(am__untar) < result.tar
#
AC_DEFUN([_AM_PROG_TAR],
[# Always define AMTAR for backward compatibility.  Yes, it's still used
# in the wild :-(  We should find a proper way to deprecate it ...
AC_SUBST([AMTAR], ['$${TAR-tar}'])

# We'll loop over all known methods to create a tar archive until one works.
_am_tools='gnutar m4_if([$1], [ustar], [plaintar]) pax cpio none'

m4_if([$1], [v7],
  [am__tar='$${TAR-tar} chof - "$$tardir"' am__untar='$${TAR-tar} xf -'],

  [m4_case([$1],
    [ustar],
     [# The POSIX 1988 'ustar' format is defined with fixed-size fields.
      # There is notably a 21 bits limit for the UID and the GID.  In fact,
      # the 'pax' utility can hang on bigger UID/GID (see automake bug#8343
      # and bug#13588).
      am_max_uid=2097151 # 2^21 - 1
      am_max_gid=$am_max_uid
      # The $UID and $GID variables are not portable, so we need to resort
      # to the POSIX-mandated id(1) utility.  Errors in the 'id' calls
      # below are definitely unexpected, so allow the users to see them
      # (that is, avoid stderr redirection).
      am_uid=`id -u || echo unknown`
      am_gid=`id -g || echo unknown`
      AC_MSG_CHECKING([whether UID '$am_uid' is supported by ustar format])
      if test $am_uid -le $am_max_uid; then
         AC_MSG_RESULT([yes])
      else
         AC_MSG_RESULT([no])
         _am_tools=none
      fi
      AC_MSG_CHECKING([whether GID '$am_gid' is supported by ustar format])
      if test $am_gid -le $am_max_gid; then
         AC_MSG_RESULT([yes])
      else
        AC_MSG_RESULT([no])
        _am_tools=none
      fi],

  [pax],
    [],

  [m4_fatal([Unknown tar format])])

  AC_MSG_CHECKING([how to create a $1 tar archive])

  # Go ahead even if we have the value already cached.  We do so because we
  # need to set the values for the 'am__tar' and 'am__untar' variables.
  _am_tools=${am_cv_prog_tar_$1-$_am_tools}

  for _am_tool in $_am_tools; do
    case $_am_tool in
    gnutar)
      for _am_tar in tar gnutar gtar; do
        AM_RUN_LOG([$_am_tar --version]) && break
      done
      am__tar="$_am_tar --format=m4_if([$1], [pax], [posix], [$1]) -chf - "'"$$tardir"'
      am__tar_="$_am_tar --format=m4_if([$1], [pax], [posix], [$1]) -chf - "'"$tardir"'
      am__untar="$_am_tar -xf -"
      ;;
    plaintar)
      # Must skip GNU tar: if it does not support --format= it doesn't create
      # ustar tarball either.
      (tar --version) >/dev/null 2>&1 && continue
      am__tar='tar chf - "$$tardir"'
      am__tar_='tar chf - "$tardir"'
      am__untar='tar xf -'
      ;;
    pax)
      am__tar='pax -L -x $1 -w "$$tardir"'
      am__tar_='pax -L -x $1 -w "$tardir"'
      am__untar='pax -r'
      ;;
    cpio)
      am__tar='find "$$tardir" -print | cpio -o -H $1 -L'
      am__tar_='find "$tardir" -print | cpio -o -H $1 -L'
      am__untar='cpio -i -H $1 -d'
      ;;
    none)
      am__tar=false
      am__tar_=false
      am__untar=false
      ;;
    esac

    # If the value was cached, stop now.  We just wanted to have am__tar
    # and am__untar set.
    test -n "${am_cv_prog_tar_$1}" && break

    # tar/untar a dummy directory, and stop if the command works.
    rm -rf conftest.dir
    mkdir conftest.dir
    echo GrepMe > conftest.dir/file
    AM_RUN_LOG([tardir=conftest.dir && eval $am__tar_ >conftest.tar])
    rm -rf conftest.dir
    if test -s conftest.tar; then
      AM_RUN_LOG([$am__untar <conftest.tar])
      AM_RUN_LOG([cat conftest.dir/file])
      grep GrepMe conftest.dir/file >/dev/null 2>&1 && break
    fi
  done
  rm -rf conftest.dir

  AC_CACHE_VAL([am_cv_prog_tar_$1], [am_cv_prog_tar_$1=$_am_tool])
  AC_MSG_RESULT([$am_cv_prog_tar_$1])])

AC_SUBST([am__tar])
AC_SUBST([am__untar])
]) # _AM_PROG_TAR

