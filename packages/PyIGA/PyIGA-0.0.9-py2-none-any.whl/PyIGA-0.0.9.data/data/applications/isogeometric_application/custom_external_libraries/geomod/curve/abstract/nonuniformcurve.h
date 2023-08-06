#include "../../geomodcore.h"

#pragma once

namespace geomodcore {

	class NonUniformCurve
	{
	protected:
		Knots knots;	/// f�r direkten Element-Zugriff

	public:

		~NonUniformCurve();

		/**
		* \brief konstante Referenz auf Knotenvektor
		* \return konstante Referenz auf Knotenvektor
		*/
		const Knots& getKnotValuesConstRef() const;

		/**
		* \brief Referenz auf Knotenvektor
		* \return Referenz auf Knotenvektor
		*/
		Knots& getKnotValuesRef();

		/**
		* \brief Knotenvektor
		* \return Knotenvektor
		*/
		Knots getKnotValues() const;

	};
}