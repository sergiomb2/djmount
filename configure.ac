# -*- Autoconf -*-
# $Id$
#
# Top-level configure.ac file for djmount
#
# Process this file with autoconf to produce a configure script.
#
# (C) Copyright 2005 Rémi Turboult <r3mi@users.sourceforge.net>
#

AC_PREREQ(2.59)
AC_INIT(djmount, 0.71, r3mi@users.sourceforge.net)

# share auxiliary files with sub-configure in "libupnp"
#AC_CONFIG_AUX_DIR([m4])
AC_CONFIG_MACRO_DIR([m4])
AC_CONFIG_MACRO_DIRS([m4])

AC_CONFIG_SRCDIR(djmount/djfs.c)

AM_INIT_AUTOMAKE([1.9 -Wall std-options gnu])

AC_CONFIG_HEADERS(config.h)

AC_COPYRIGHT([Copyright (C) 2005 Rémi Turboult])
AC_REVISION([$Revision$])


#
# --enable-FEATURE flags
# ----------------------
#

#
# Checks for programs
#
AC_PROG_CC

# build static libraries by default (for bundled libupnp and talloc)
#AC_DISABLE_SHARED

LT_INIT
AC_PROG_INSTALL
AC_PROG_MAKE_SET
AC_PROG_LN_S

AC_PATH_PROG(PERL,perl)

# Arrange for large-file support / large off_t
# Define _FILE_OFFSET_BITS and _LARGE_FILES if necessary
# See also http://unix.freshmeat.net/articles/view/709/
AC_SYS_LARGEFILE


#
# Checks for header files
#
AC_HEADER_DIRENT
AC_HEADER_STDC
AC_CHECK_HEADERS([inttypes.h stddef.h stdint.h stdarg.h])
if test x"$enable_charset" = xyes; then
	AC_CHECK_HEADERS([locale.h langinfo.h])
fi


#
# Checks for typedefs, structures, and compiler characteristics
#
AC_HEADER_STDBOOL
AC_C_CONST
AC_C_INLINE


#
# Checks for library functions
#
AC_CHECK_FUNCS([setxattr mktime])
if test x"$enable_charset" = xyes; then
	AC_CHECK_FUNCS([setlocale])
fi
AC_FUNC_FSEEKO

# Optional GNU extensions
AH_TEMPLATE([_GNU_SOURCE],[Define to 1 to get GNU extensions])
AC_CHECK_FUNCS([open_memstream], [AC_DEFINE([_GNU_SOURCE])])



#
# talloc 
# ------
#

#
# readline (option)
# -----------------
# Checks for readline and history compatible libraries
#

#
# iconv & langinfo
# ----------------
#


#
# POSIX Threads
# -------------
#
# We are only building threads programs so we add the pthread flags directly
# to the default compilation variables. This will also allow the tests below
# (fuse, libupnp, ...) to pick these flags.

#
# FUSE 
# ----
#

FUSE_CFLAGS="$FUSE_CFLAGS -DFUSE_USE_VERSION=22"


#
# libupnp 
# -------
#

#
# Output Makefiles
#

AC_CONFIG_FILES([Makefile po/Makefile.in
		 gl/Makefile
                 djmount/Makefile
                 ])

AC_OUTPUT

