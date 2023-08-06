#pragma once
#include "../../geometry/polygon.h"

namespace geomodcore {

	class Curve 
	{

	public:
		/**
		* Erzeugt eine �quidistante Diskretisierung der Kurve.
		* Die Sampling-Gr��e darf nicht negativ sein. 
		* \param n Abtastschritte
		*/
		virtual Polygon* getDiscretization(const unsigned int n) const = 0;

		/**
		* Berechnet eine N�herung f�r die L�nge der Kurve anhand einer Diskretisierung der Kurve
		* mit Parameterbereich L und der daraus resultierenden chordalen L�nge.
		* Die Methode kann �berschrieben werden, sofern eine vollst�ndige Berechnung der Bogenl�nge m�glich ist.
		* \param n Anzahl der Schritte
		*/
		virtual double getLength(const unsigned int n) const = 0;

		/**
		* Bestimmung der abgeleiteten Kurve.
		*/
		Curve* getDerivation(void) const { };

		/**
		* Berechnet die Bogenl�nge der Kurve aus der Ableitung.
		*/
		virtual double getArcLength(void) const = 0;
					
	};
}