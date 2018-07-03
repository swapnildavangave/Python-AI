from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation
breeds = """Indian Pariah Dog
,Chippiparai dog
,Mudhol Hound
,Rajapalayam dog
,Indian Spitz dog
,Kanni dog
,Gaddi Kutta dog
,Kombai dog
,Bakharwal dog
,Rampur Greyhound
,Kumaon Mastiff dog
,Pandikona dog
,Banjara Hound
,Bully Kutta dog
Himalayan Sheepdog"""
arguments = {"keywords":breeds,"limit":20,"print_urls":True}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)