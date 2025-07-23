default has_looked_at_paintings = False
default has_looked_at_gallery_artists = False
default has_looked_at_gallery_people = False

define painter = Character("Pintor")
define monet = Character("Claude Monet")

label art_gallery:
    scene bg art gallery with Dissolve(1)

    if has_visited_art_gallery == False:
        $ has_visited_art_gallery = True
        $ CheckCandle()
        jack "A galeria de arte da cidade. Lugar onde vários artistas vem para mostrar suas artes e ver artes de outras pessoas."
        jack "Imagino que seja um ótimo lugar para procurar inspiração, ou pelo menos encontrar algum conselho para lidar com bloqueios."
        jack "Só espero não ficar incomodando os outros falando de meu bloqueio..."

    jump art_gallery_choices

label art_gallery_choices:
    scene bg art gallery with Dissolve(1)
    menu:
        "Olhar os quadros." if has_looked_at_paintings == False:
            $ has_looked_at_paintings = True
            $ SpendEnergy()
            jump art_gallery_paintings
        "Olhar os artistas." if has_looked_at_gallery_artists == False:
            $ has_looked_at_gallery_artists = True
            $ SpendEnergy()
            jump art_gallery_artists
        "Olhar as pessoas." if has_looked_at_gallery_people == False:
            $ has_looked_at_gallery_people = True
            $ SpendEnergy()
            jump art_gallery_people
        "Voltar para a praça.":
            $ SpendEnergy()
            jump main_square

label art_gallery_paintings:
    scene bg art gallery paintings with Dissolve(1)

    show jack_neutral at left
    jack "Tem vários quadros sendo expostos."
    jack "Nenhum deles me parece familiar. Mas também, faz tempo que não venho para a exposição, então já devem ter mudado os quadros desde a última vez."
    if has_looked_at_park_people == True: # Somente se já tiver encontrado com o Guillaumin no parque
        jack "Dá pra ver as pinceladas na tela, como se eles tivessem sido pintados às pressas."
        jack "É como Guillaumin falou, quadros pintados com pinceladas rápidas para não demorar com a pintura."
        jack "Espero que essa filosofia se adapte bem para a escrita quando eu voltar para casa."
    else:
        jack "Os quadros são bonitos, mas não sei se podem me ajudar muito."
        if has_looked_at_gallery_artists == False:
            jack "Talvez eu tenha mais sorte se eu tentar falar com algum dos artistas."

    #jump art_gallery_choices
    $ CheckEnergyJump("art_gallery_choices")

label art_gallery_artists:
    scene bg art gallery artists with Dissolve(1)

    show jack_neutral at left
    jack "Tem alguns artistas expondo seus quadros para os visitantes."
    jack "Eles parecem estar explicando o que se passava enquanto eles pintavam, ou as técnicas que eles usaram."
    jack "Acho que vou tentar falar com um deles."
    jack "Com licença."
    show monet at right
    painter "Pois não?"
    jack "Me chamo Jack Williams, sou um pequeno escritor da região."
    jack "Não pude deixar de perceber sua efusividade em defender sua arte. Qual seu nome?"
    monet "Me chamo Claude Monet, sou um pintor francês. Viajei até aqui para expor meus quadros mais recentes."
    jack "Estou escrevendo uma nova obra e busco novos ares artísticos. Eu poderia conhecer mais sobre seus quadros?"
    monet "Claro."
    #scene bg dark with Fade(1, 3.0, 1)
    scene bg art gallery monet varengeville 1 with Dissolve(1)
    monet "Este é um quadro que pintei da costa de Varengeville, na França."
    monet "Também pintei a costa do alto do penhasco."
    #scene bg dark with Fade(1, 3.0, 1)
    scene bg art gallery monet varengeville 2 with Dissolve(1)
    show jack_surprised at left
    show monet at right
    jack "Incrível. Você consegue passar a ideia do ambiente mesmo sem colocar muitos detalhes."
    if has_looked_at_park_people == True:
        monet "Isso mesmo, estou muito mais interessado em -"
        hide jack_surprised
        show jack_neutral at left
        jack "Capturar o momento?"
        monet "Isso mesmo. Parece que você já entende um pouco das pinturas."
        jack "É, encontrei com um pintor no parque, e ele seguia essa mesma filosofia."
        monet "Entendo. Bem, o importante é não se prender à forma exata e aos detalhes."
    else:
        monet "Isso mesmo, estou muito mais interessado em capturar o calor do momento."
    monet "Eu me preocupo com o que o Sol, a luz e o que ela me diz naquele instante, as emoções e sentimentos que sinto ao olhar para a paisagem."
    hide jack_surprised
    show jack_neutral at left
    jack "Faz sentido. Talvez isso me ajude com meu livro. Tenho passado por um bloqueio criativo e acho que essa filosofia pode me ser útil."
    jack "Ao invés de me preocupar com a forma exata da história, devo deixar as emoções me guiarem."
    hide jack_neutral
    show jack_smile at left
    jack "Obrigado pela discussão."
    monet "Não há de que."
    $ GainInspiration(1)
    if has_looked_at_park_people == True: # Se tiver falado com Guillaumin
        $ GainInspiration(1)

    #jump art_gallery_choices
    $ CheckEnergyJump("art_gallery_choices")

label art_gallery_people:
    scene bg art gallery with Dissolve(1)

    jack "Tem várias pessoas olhando os quadros da exposição."
    jack "A maioria delas não parece ser artista, devem ser só visitantes que vieram ver a exposição."
    jack "Não acho que eu vá conseguir muita ajuda delas."

    #jump art_gallery_choices
    $ CheckEnergyJump("art_gallery_choices")