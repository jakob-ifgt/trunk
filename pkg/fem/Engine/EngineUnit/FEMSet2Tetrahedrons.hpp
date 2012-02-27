/*************************************************************************
*  Copyright (C) 2004 by Janek Kozicki                                   *
*  cosurgi@berlios.de                                                    *
*                                                                        *
*  This program is free software; it is licensed under the terms of the  *
*  GNU General Public License v2 or later. See file LICENSE for details. *
*************************************************************************/

#pragma once

#include<yade/pkg-common/GeometricalModelEngineUnit.hpp>

class FEMSet2Tetrahedrons : public GeometricalModelEngineUnit
{
	public :
		void go(	  const shared_ptr<PhysicalParameters>&
				, shared_ptr<GeometricalModel>&
				, const Body*);
	FUNCTOR2D(FEMSetParameters,FEMSetGeometry);
	REGISTER_CLASS_NAME(FEMSet2Tetrahedrons);
	REGISTER_BASE_CLASS_NAME(GeometricalModelEngineUnit);

};

REGISTER_SERIALIZABLE(FEMSet2Tetrahedrons);

