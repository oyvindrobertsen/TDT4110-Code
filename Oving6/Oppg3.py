def coords():
    x, y, z = int(input('Skriv inn x-koordinaten')), int(input('Skriv inn y-koordinaten')), int(input('Skriv inn z-koordinaten'))
    coordinates = [x, y, z]
    return coordinates

def main():
    coords()
    
main()