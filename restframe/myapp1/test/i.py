from PIL import Image
import io
from io import StringIO
from django.core.files.base import ContentFile
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile

def create_image(storage, filename, size=(100, 100), image_mode='RGB', image_format='PNG'):
    """
    Generate a test image, returning the filename that it was saved as.

    If ``storage`` is ``None``, the BytesIO containing the image data
    will be passed instead.
    """
    data = io.BytesIO()
    Image.new(image_mode, size).save(data, image_format)
    data.seek(0)
    if not storage:
        return data
    image_file = ContentFile(data.read())
    return storage.save(filename, image_file)



myimage = create_image(None, 'fake.png')
print(myimage)
avatar_file = SimpleUploadedFile('front.png', myimage.getvalue())
print(avatar_file)
print(type(avatar_file))