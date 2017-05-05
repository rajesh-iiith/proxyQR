from numpy import genfromtxt, transpose 
import scipy.misc
import argparse


def parse_inputs():
	parser = argparse.ArgumentParser(description='proxyQR: Grabs a 2D Matrix from a CSV file, plots binary version of its transpose')
	parser.add_argument('-i','--input', help='path to input csv file', default = "empty")
	parser.add_argument('-o','--output', help='path to output image file', default = "out.png")
	

	args = vars(parser.parse_args())

	input_file = args['input']
	output_image = args['output']

	return input_file, output_image

input_file, output_image = parse_inputs()


image_array = genfromtxt(input_file, delimiter=',').astype(int)
image_array = transpose(image_array)
for x in range(image_array.shape[0]):
    for y in range(image_array.shape[1]):
        if image_array[x,y] == 0: #convert zeros to 1
        	image_array[x,y] = 1
        else: #convert non zeros to zeros
        	image_array[x,y] = 0

scipy.misc.imsave(output_image, image_array)