import pydicom

def dicom_to_array(file_path,file_name):

    full_file = file_path+file_name

    image = pydicom.dcmread(full_file)

    return image.pixel_array
