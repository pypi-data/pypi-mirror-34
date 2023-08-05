/*+
 *  Name:
 *     emsSetu

 *  Purpose:
 *     Assign an unsigned int value to a message token (concise).

 *  Language:
 *     Starlink ANSI C

 *  Invocation:
 *     emsSetu( token, ivalue )

 *  Description:
 *     The given unsigned int value is encoded using a concise format and the
 *     result assigned to the named message token. If the token is already
 *     defined the result is appended to the existing token value.
 *     No Fortran-callable interface is provided.

 *  Arguments:
 *     token = const char * (Given)
 *        The message token name.
 *     ivalue = unsigned int (Given)
 *        The unsigned integer value to be assigned to the message token.

*  Copyright:
*     Copyright (C) 1990, 1991 Science & Engineering Research Council.
*     Copyright (C) 1999, 2001 Central Laboratory of the Research Councils.
*     Copyright (C) 2006 Particle Physics & Astronomy Research Council.
*     All Rights Reserved.

*  Licence:
*     This program is free software; you can redistribute it and/or
*     modify it under the terms of the GNU General Public License as
*     published by the Free Software Foundation; either version 2 of
*     the License, or (at your option) any later version.
*
*     This program is distributed in the hope that it will be
*     useful,but WITHOUT ANY WARRANTY; without even the implied
*     warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
*     PURPOSE. See the GNU General Public License for more details.
*
*     You should have received a copy of the GNU General Public License
*     along with this program; if not, write to the Free Software
*     Foundation, Inc., 51 Franklin Street,Fifth Floor, Boston, MA
*     02110-1301, USA

 *  Authors:
 *     PCTR: P.C.T. Rees (STARLINK)
 *     AJC: A.J. Chipperfield (STARLINK)
 *     RTP: R.T.Platon (STARLINK)
 *     TIMJ: Tim Jenness (JAC, Hawaii)
 *     {enter_new_authors_here}

 *  History:
 *     6-JUN-1990 (PCTR):
 *        Original version, coded as a C macro function.
 *     14-AUG-1990 (PCTR):
 *        C function code.
 *     21-JUN-1991 (PCTR):
 *        Made all given character strings type "const".
 *     13-MAY-1999 (AJC):
 *        Renamed from ems_setl_c
 *     14-FEB-2001 (RTP):
 *        Renamed from ems_setl_c
 *      3-MAR-2001 (AJC):
 *        Import token name
 *      3-MAR-2006 (TIMJ):
 *        Copy from emsSeti
 *     {enter_further_changes_here}

 *  Bugs:
 *     {note_any_bugs_here}

 *-
 */

/* Include Statements: */
#include <string.h>                    /* String handling library functions */
#include "ems_par.h"                   /* ems_ public constant definitions */
#include "ems_sys.h"                   /* ems_ private macro definitions */
#include "ems.h"                       /* ems_ function prototypes */
#include "ems1.h"                      /* ems_ internal function prototypes */

/* Function Definitons: */
void emsSetu( const char *token, unsigned int ivalue ){

/* Local Type Definitions: */
   char str[EMS__SZTOK+1];

   TRACE("emsSetu");
   DEBUG("emsSetu","emsSetu: %u", ivalue);

/*  Construct the message token string. */
   sprintf( str, "%u", ivalue );
   ems1Stok( token, str );

   return;
}
