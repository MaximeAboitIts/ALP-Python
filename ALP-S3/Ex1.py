import math

rayon = float(input("Entrez un rayon: "))
aire = math.pi * (rayon * rayon)
circonference = (rayon + rayon) * math.pi

print("Un cercle de rayon", rayon, "a une aire de",
      aire, "et une circonférence de", circonference)
