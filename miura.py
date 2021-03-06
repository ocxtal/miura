#! /usr/bin/env python
# encoding: utf-8

from dxfwrite import DXFEngine as dxf

def plot(drawing, x, y, xdiv, ydiv, tan, ofs):

	x = float(x)
	y = float(y)
	tan = float(tan)

	def pos(x, y):
		return([float(ofs[0])+x, float(ofs[1])+y])

	# draw vertical boundaries
	drawing.add(dxf.line(pos(0, 0), pos(0, y), color = 7))
	drawing.add(dxf.line(pos(x, 0), pos(x, y), color = 7))

	# draw horizontal lines
	for i in range(ydiv + 1):
		drawing.add(dxf.line(pos(0, i * y / ydiv), pos(x, i * y / ydiv), color = 7))

	# draw vertical lines
	t = (y/ydiv) * tan
	p = (x - t) / xdiv
	for i in range(ydiv):
		for j in range(1, xdiv):
			drawing.add(dxf.line(
				pos(j * p + (t if i % 2 == 1 else 0), i * y / ydiv),
				pos(j * p + (t if i % 2 == 0 else 0), (i + 1) * y / ydiv),
				color = 7))


if __name__ == '__main__':
	import sys

	import sys
	from optparse import OptionParser
	p = OptionParser(usage = "python miura.py <width> <height> > out.dxf # all dimensions are in millimeters")
	p.add_option("-t", "--tan", dest = "t", help = "tangent", type = "float", default = 0.1)
	p.add_option("-x", "--xcnt", dest = "xcnt", help = "x (width) splitting count", type = "int", default = 5)
	p.add_option("-y", "--ycnt", dest = "ycnt", help = "y (height) splitting count", type = "int", default = 3)
	p.add_option("-o", "--output", dest = "o", help = "output file name")

	(opt, args) = p.parse_args()
	if len(args) < 2:
		p.error("width and height must be given as positional arguments.")

	x = float(args[0])		# width
	y = float(args[1])		# height
	filename = opt.o

	drawing = dxf.drawing()
	plot(drawing, x, y, opt.xcnt, opt.ycnt, opt.t, [10, 10])
	drawing.save_to_fileobj(open(opt.o, "w") if opt.o is not None else sys.stdout)


