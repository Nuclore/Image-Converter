from image_converter import ImageConverter # Imports the ImageConverter class from the image_converter module.

def get_dimension(dimension):
	'''Function to obtain the image dimensions.'''
	while True:
		try:
			number = int(input(f'Enter {dimension} for conversion: ')) 
			if number > 0:
				return number 
			else:
				print(f'Invalid value for {dimension}.\n') # Displays a message if the number is less than zero.
		except ValueError:
			print(f'You did not enter a number.\n') # Displays an error message if the input was not a number.
		except:
			print('Some other error occured.\n')


def get_format():
	'''Function to obtain the desired image format.'''
	formats = ['bmp', 'gif', 'jpg', 'png', 'tiff', ] # List of available formats.
	while True:
		print('\nAvailable Formats: ')
		for format in formats:
			print(f'*{format}')

		format = input('\nSelect format for image conversion: ')
		if format.lower() in formats:
			return format.lower()
		else:
			print('Invalid format. Please try again.\n')


def convert_image(size, format):
	'''Function to create the ImageConverter object and convert the images.'''
	image_converter = ImageConverter(size, format)
	image_converter.convert_images()


if __name__ == '__main__':
	# Obtains the desired width and height for the images, and store them in a tuple.
	image_width = get_dimension('width')
	image_height = get_dimension('height')
	image_size = (image_width, image_height)

	# Obtains the conversion format for the images.
	image_format = get_format()

	# Converts the images to the specified dimensions and format.
	convert_image(image_size, image_format)


