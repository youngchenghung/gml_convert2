# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GmlConverter
                                 A QGIS plugin
 GmlConverter
                             -------------------
        begin                : 2019-02-13
        copyright            : (C) 2019 by  
        email                :  
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GmlConverter class from file GmlConverter.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .gml_converter import GmlConverter
    return GmlConverter(iface)
