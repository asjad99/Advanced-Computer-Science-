
using Colors, ColorVectorSpace, ImageShow, FileIO, ImageIO
using PlutoUI
using HypertextLiteral


url = "https://user-images.githubusercontent.com/6933510/107239146-dcc3fd00-6a28-11eb-8c7b-41aaf6618935.png" 

doggo_filename = download(url)

philip = load(doggo_filename)

philip_size = size(philip)