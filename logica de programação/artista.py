artista = ["Billie Eilish", "Lana Del Rey", "Melanie Martinez", "Taylor Swift"]

print(artista)
antigo=input("Qual artista deseja substituir?")
outro_artista = input("Quem vai substituir o artista? ")
indice = artista.index(antigo)
artista[indice] = outro_artista


print("Artista substituido. A lista agora é: ", artista )
