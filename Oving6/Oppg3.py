import math

def vector_input():
    x, y, z = int(input('Skriv inn x-koordinaten: ')), int(input('Skriv inn y-koordinaten: ')), int(input('Skriv inn z-koordinaten: '))
    coordinates = [x, y, z]
    return coordinates

def print_vector(vector):
    print('[', vector[0] ,',', vector[1] ,',', vector[2] ,']')
    
def s_multi(scalar, vector):
    s_vector = vector
    for i in range(3):
        s_vector[i] = s_vector[i] * scalar
    return s_vector

def vector_length(vector):
    length = format(math.sqrt( ((vector[0])**2) + ((vector[1])**2) + ((vector[2])**2)), '.2f')
    return length

def vector_prod(vector1, vector2):
    prod = vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]
    return prod

def main():
    vec1 = vector_input()
    print_vector(vec1)
    vec_l1 = float(vector_length(vec1))
    vec2 = vector_input()
    print('vektor-produkt av vec1 og vec2:', vector_prod(vec1, vec2))
    scal1 = int(input('Skriv inn skalaren: '))
    s_vec1 = s_multi(scal1, vec1)
    print_vector(s_vec1)
    s_vec_l1 = float(vector_length(s_vec1))
    print(vec_l1, s_vec_l1, vec_l1/s_vec_l1)
main()