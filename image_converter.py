from PIL import Image # Class for manipulating images.
import os # Module for interacting witht the operating system.

class ImageConverter:
    '''Class containing functionality for converting images.'''
    def __init__(self, size=(0,0), format='jpg'):
        '''Initializes the specified size and format of the converted images,
        as well as the path they will be located.
        '''
        self.size = size # Dimensions (i.e. width and height) of the converted images.
        self.format = format # Format of the converted images.

        self.images_path = 'images' # Path where the images are located.
        self.converted_images_path = 'converted_images' # Path to store the converted images.

        self.image_names = self.get_image_names() # Obtains a list of the image names (with extension).

    def get_image_names(self):
        '''Returns a list of the files in the  directory.'''
        if os.path.exists(self.images_path): # Checks if the path exists.
            image_names = os.listdir(self.images_path) # Creates a list of the files present in the directory.
            return image_names
        else:
            print(f'The \'{self.images_path}\' directory does not exist.')

    def convert_images(self):
        '''Converts the images to the specified dimensions and format, and store them in the specified path.'''
        for image_name in self.image_names:
            image, ext = os.path.splitext(image_name) # Split the filename from the extension.
            try:
                with Image.open(f'{self.images_path}/{image_name}').convert('RGB') as im: # Opens the image to be processed.
                    # Resizes and saves the image with the specified format.
                    im.resize(self.size).save(f'{self.converted_images_path}/{image}.{self.format}')
            except OSError:
                print(f'{image_name} could not be converted.') # Displays an error message if the file could not be converted.
            except:
                print('Some other error occured.')
        print('\nConversion finished.')
