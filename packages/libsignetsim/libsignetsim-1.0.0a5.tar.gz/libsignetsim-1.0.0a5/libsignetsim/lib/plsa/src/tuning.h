/******************************************************************************
 *                                                                            *
 *   mixing.h                                                                 *
 *                                                                            *
 ******************************************************************************
 *                                                                            *
 *   Written by Vincent Noel                                                 *
 *                                                                            *
 ******************************************************************************
 *                                                                            *
 *   This file...											                  *
 *                                                                            *
 ******************************************************************************
 *                                                                            *
 *   Copyright (C) 2016 Vincent Noel (vincent.noel@butantan.gov.br)           *
 *                                                                            *
 *   plsa is free software: you can redistribute it and/or modify             *
 *   it under the terms of the GNU General Public License as published by     *
 *   the Free Software Foundation, either version 3 of the License, or        *
 *   (at your option) any later version.                                      *
 *                                                                            *
 *   plsa is distributed in the hope that it will be useful,                  *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of           *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            *
 *   GNU General Public License for more details.                             *
 *                                                                            *
 *   You should have received a copy of the GNU General Public License        *
 *   along with plsa. If not, see <http://www.gnu.org/licenses/>.             *
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include "types.h"

#define MAX_MIX         10000      /* max number of mixes during a tuning run */
					/* set this to a lower number if you run out of memory */
#define GROUP_SIZE         10       /* group size for calculating upper bound */

#define STOP_TUNE_CNT      20                              /* stop tune count */
#define STOP_TUNE_CRIT   0.05                        /* tuning stop criterion */

#define LSTAT_LENGTH_TUNE  28          /* length of Lam msg array when tuning */

 /* tuning functions */

 /*** InitTuning: sets up/restores structs and variables for tuning runs ****
 ***************************************************************************/
void 		InitTuning					(SAType * state);
void 		InitLocalStatsTuning		(double mean, double vari, int success);
void 		Init2LocalStatsTuning		(int proc_init);
void 		UpdateLocalSTuning			(double S);
void 		UpdateLocalStatsTuning		(int proc_tau);


void 		RestoreLocalLogTuning		(int max_saved_count);
void 		CalculateLocalStats			(double energy);
int 		UpdateTuning				(char * logfile);
void 		InitLocalTuningFilenames();
