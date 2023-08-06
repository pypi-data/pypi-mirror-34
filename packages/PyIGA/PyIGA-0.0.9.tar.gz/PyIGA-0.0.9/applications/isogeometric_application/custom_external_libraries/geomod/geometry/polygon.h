#pragma once

#include "../geomodcore.h"

namespace geomodcore {

	/**
	* Ein Polygon ist eine doppelt verkettete Liste von Zeigern auf ver�nderbare Punkte.
	*/
	class Polygon : public std::vector<GPoint>
	{
	public:

		// Konstruktor f�r std-vektor-�bergabe mit �nderbaren Punkten
		Polygon(const std::vector<GPoint>& points);

		// Standard-Konstruktor
		Polygon(void);
		// Copy-Konstruktor
		Polygon(const Polygon& curve);
		// Destruktor
		~Polygon(void);
		// Assignment operator
		Polygon& operator= (const Polygon& curve);
		
	public:

		/*
		* Ermittelt die Laenge des Polygonzugs
		*/
		double getPolygonLength(void) const;

	};
}