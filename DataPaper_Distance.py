#Seeing the distance of paper stack, if all digital data was printed
#Hayden Lakey
#17 February 2022

Zettabyte = 1024**7*8
Spaper = 37260    #Spaper = Storage per sheet
Pthick = 0.075 #mm
Apaper = 0.06237 #m^2
Aupper = 8700

Spoint = Aupper/Apaper
Totalbytes = 2.7*Zettabyte
Used = Spaper*Spoint
Remainder = Totalbytes - Used
Pneed = Remainder/Spaper
Layers = Pneed/Spoint
Heightmm = Layers*Pthick
Heightm = Heightmm/1000000

print(Heightm)


