# from rectpack import newPacker
#
# rectangles = [(100, 30), (40, 60), (30, 30),(70, 70), (100, 50), (30, 30)]
# bins = [(300, 450), (80, 40), (200, 150)]
#
# packer = newPacker()
#
# # Add the rectangles to packing queue
# for r in rectangles:
# 	packer.add_rect(*r)
#
# # Add the bins where the rectangles will be placed
# for b in bins:
# 	packer.add_bin(*b)
#
# # Start packing
# packer.pack()
#
# # Obtain number of bins used for packing
# nbins = len(packer)
# print("nbins", nbins)