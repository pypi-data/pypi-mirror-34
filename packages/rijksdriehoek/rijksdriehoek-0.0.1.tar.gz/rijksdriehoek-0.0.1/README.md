# python-rijksdriehoek

Converts Rijksdriehoek coordinates to WGS'84, and vice versa.

Example usage:

``
from rijksdriehoek import rijksdriehoek
rd = rijksdriehoek.Rijksdriehoek()
print("Original coordinates in WGS'84: {},{}".format(str(52.3761973), str(4.8936216)))
rd.from_wgs(52.3761973, 4.8936216)
print("Rijksdriehoek: {},{}".format(str(rd.rd_x), str(rd.rd_y)))
lat, lon = rd.to_wgs()
print("WGS'84 coordinates converted from RD: {},{}".format(str(lat), str(lon)))
``

Please be aware that every conversion from WGS->RD->WGS has shown to introduce a inaccuracy of up to 0.0000001 degrees. Please take that into consideration when deciding whether this tool is useful for usage in your project.