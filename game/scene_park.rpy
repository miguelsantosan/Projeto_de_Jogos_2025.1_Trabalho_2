default has_looked_at_park_people = False
default has_looked_at_picnic = False
default has_looked_at_birds = False
default has_looked_at_lake = False
default has_looked_at_kids = False

define man = Character("Rapaz")
define guillaumin = Character("Armand Guillaumin")

label park:
    scene bg park with Dissolve(1)
    show jack_neutral at left

    if has_visited_park == False:
        $ has_looked_at_park_people = False
        $ has_looked_at_picnic = False
        $ has_looked_at_birds = False
        $ has_looked_at_lake = False
        $ has_looked_at_kids = False
        $ CheckCandle()
        jack "O parque da cidade. Grande e movimentado como sempre."
        jack "Tenho passado tanto tempo isolado em minha casa que eu havia me esquecido em como ele podia ser movimentado."
        jack "Tem gente andando de um lado para o outro, crianças brincando, o cantar dos pássaros..."
        jack "É um bom lugar pra matar o tempo."
        $ has_visited_park = True

    jump park_choices

label park_choices:
    scene bg park with Dissolve(1)
    menu:
        "Olhar as pessoas conversando." if has_looked_at_park_people == False:
            $ has_looked_at_park_people = True
            $ SpendEnergy()
            jump park_people
        "Olhar as pessoas em pique-nique." if has_looked_at_picnic == False:
            $ has_looked_at_picnic = True
            $ SpendEnergy()
            jump park_picnic
        "Olhar as crianças brincando." if has_looked_at_kids == False:
            $ has_looked_at_kids = True
            $ SpendEnergy()
            jump park_kids
        "Olhar os pássaros." if has_looked_at_birds == False:
            $ has_looked_at_birds = True
            $ SpendEnergy()
            jump park_birds
        #"Olhar o lago." if has_looked_at_lake == False:
        #    $ has_looked_at_lake = True
        #    $ SpendEnergy()
        #    jump park_lake
        "Voltar para a praça.":
            $ SpendEnergy()
            jump main_square

label park_people:
    scene bg park people with Dissolve(1)

    show jack_neutral at left
    jack "Tem várias pessoas no parque, como era de se esperar."
    jack "Elas parecem estar se divertindo batendo papo e fofocando."
    hide jack_neutral
    show jack_sad at left
    jack "Queria eu ter tempo pra gastar com lazer assim."
    jack "Acho que isso não está me ajudando, é melhor eu ir embo-"
    "Ei!"
    hide jack_sad
    show jack_confused at left
    jack "Alguém acabou de gritar? O que será que foi?"
    "Você mesmo!"
    jack "Aquele senhor está falando comigo?"
    show man2 at right
    man "Caramba! É você mesmo!"
    jack "Hã? A gente se conhece?"
    man "Você é o Jack Williams, não é? Escritor daqui da cidade."
    jack "Sim, sou eu mesmo."
    man "Bem que eu desconfiei. Lembro de ter te visto em uma feira de livros alguns anos atrás. Tenho uma ótima memória para gravar rostos."
    man "E bem, não é todo dia que se encontra um escritor."
    hide jack_confused
    show jack_surprised at left
    jack "Ah... Então você chegou a ler algum de meus livros?"
    man "Li alguns."
    man "Um pouco curtos para meu gosto, mas as histórias eram agradáveis."
    hide jack_surprised
    show jack_smile at left
    jack "Fico feliz em saber de alguém que goste de meus livros."
    man "E então, já está escrevendo seu próximo livro?"
    hide jack_smile
    show jack_disgust at left
    jack "Beeeem... Posso dizer que sim..."
    jack "Mas tenho andado por um bloqueio ultimamente, então a história está travada no momento."
    man "Entendo."
    man "Sou pintor, e às vezes passo por isso também."
    hide jack_disgust
    show jack_surprised at left
    jack "Jura?"
    man "Sim, inclusive estava pintando um quadro agora mesmo. Gostaria de ver?"
    jack "Claro, agora fiquei curioso."
    man "Venha, vou lhe mostrar o quadro"
    #scene bg dark with Fade(1, 3.0, 1)
    scene bg park guillaumin painting with Dissolve(1)
    show jack_surprised at left
    show man2 at right
    jack "Nossa, é um quadro bonito."
    man "Obrigado."
    man "Meus professores de artes falavam que antigamente eles tinhas que pintar o quadro todo no atelier, inclusive para preparar as tintas."
    man "Mas hoje há bisnagas de tinta prontas em embalagens que podem ser levadas para onde quisermos. Com isso, podemos levar nossos quadros para pintar ao ar livre."
    man "Entretanto, no atelier, as pessoas ficavam paradas para servir de modelo para a pintura."
    man "Aqui, as pessoas vão seguindo com seus dias conforme vou pintando, então para capturar o momento devo dar pinceladas rápidas para não levar muito tempo com meu trabalho e \"perder o momento\" com elas indo embora."
    if has_looked_at_gallery_artists == True:
        jack "Sim, capturar o calor do momento. Encontrei com Monet na exposição da cidade e ele me contou sobre."
        man "Ah sim, estive com ele também esses últimos dias. Um grande pintor. Nos conhecemos na Académie Suisse."
        man "Mas estou apenas de viagem, então não estou expondo nenhum de meus quadros."
        jack "Nossa, você estudou com Monet? Qual seu nome?"
    else:
        jack "Entendi. Parece bem prático. A propósito, qual seu nome?"
    guillaumin "Me chamo Armand Guillaumin. Sou da França, mas vim para a Inglaterra para procurar paisagens novas para pintar."
    guillaumin "Tenho gostado da região, mas também anseio para voltar para casa e exibir meus quadros."
    jack "Imagino, por mais que um lugar seja agradável, nada como o conforto de casa."
    guillaumin "A conversa está boa, mas, se me dá licença, preciso acabar este quadro. Não quero perder o momento e deixar meu quadro inacabado."
    jack "Sem problemas, não quero atrapalhar."
    #scene bg dark with Fade(1, 3.0, 1)
    scene bg park with Dissolve(1)
    show jack_smile at left
    jack "\"Capturar o momento.\" Isso me deu uma ideia..."
    jack "Uma vez que uma ideia vir, não posso deixá-la escapar. Devo aproveitá-la de imediato para não correr o risco de perdê-la depois e eu não conseguir desenvolvê-la."
    jack "Isso deve me ajudar com meu livro."
    $ GainInspiration(1)
    if has_looked_at_gallery_artists == True: # Se tiver falado com Monet
        $ GainInspiration(1)
    
    #jump park_choices
    $ CheckEnergyJump("park_choices")

label park_picnic:
    scene bg park picnic with Dissolve(1)

    show jack_neutral at left
    jack "Tem várias pessoas pelo parque fazendo pique-nique. Elas parecem alegres."
    hide jack_neutral
    show jack_confused at left
    jack "Parando pra pensar, faz tempo que não vou a um pique-nique."
    hide jack_confused
    show jack_sad at left
    jack "Desde que meu pai morreu e eu comprei aquela casa eu acabei me isolando para me dedicar ao meu sonho de ser escritor."
    jack "E agora com minha situação atual, nem tenho tempo direito de ver ninguém."
    jack "Depois que tudo isso passar, vou tentar me reconectar com meus amigos."
    hide jack_sad
    
    #jump park_choices
    $ CheckEnergyJump("park_choices")

label park_birds:
    scene bg park birds with Dissolve(1)

    show jack_surprised at left
    jack "Nossa, tem tantos pássaros voando sobre o parque."
    hide jack_surprised
    show jack_smile at left
    jack "Eles devem estar de olho nas sobras de comida dos pique-niques."
    jack "É relaxante assisti-los voando de uma lado para outro, sem rumo. Com total liberdade de onde eles querem ir."
    hide jack_smile
    show jack_sad at left
    jack "Quem me dera eu tivesse essa liberdade. Mas tenho que terminar meu livro para não perder minha casa..."
    jack "Talvez ficar um pouco e observar os pássaros me anime um pouco."
    hide jack_sad
    show jack_neutral at left
    menu:
        "Observar os pássaros.":
            scene bg park birds 2 with Dissolve(1)
            show jack_neutral at left
            jack "Os pássaros voam de maneira despreocupada no céu do parque."
            hide jack_neutral
            show jack_smile at left
            jack "Dá uma certa tranquilidade ficar assistindo os pássaros assim. É bom lembrar de como a natureza pode ser tão simples, mas tão bela. É... terapêutico."
            jack "Isso pode não me dar ideias pro livro, mas ajuda a relaxar um pouco."
            $ ReplenishEnergy(3)
            $ GainInspiration(0.5)
        "Não tenho tempo para isso.":
            hide jack_neutral
            show jack_sad at left
            jack "Melhor não, não tenho muito tempo sobrando. Talvez eu deva procurar inspiração em algum outro lugar."
    
    #jump park_choices
    $ CheckEnergyJump("park_choices")

label park_lake:
    scene bg park lake with Dissolve(1)

    jack ""
    
    #jump park_choices
    $ CheckEnergyJump("park_choices")

label park_kids:
    scene bg park kids with Dissolve(1)

    show jack_neutral at left
    jack "Tem várias crianças brincando pelo parque."
    jack "Elas ficam brincando com seus brinquedos e andando de bicicleta, sem nenhuma preocupação."
    hide jack_neutral
    show jack_smile at left
    jack "Isso me lembra quando eu era criança. Meu pai me levava a um parque que tinha perto de casa."
    hide jack_smile
    show jack_happy at left
    jack "Eu ficava brincando com as árvores, subia nelas e imaginava que estava no topo de uma torre de castelo."
    jack "Chega a ser impressionante a criatividade das crianças. Elas simplesmente vão imaginando coisas uma atrás da outra, sem se preocupar com um destino, criando coisas que elas gostem sem se importar se faz sentido ou não."
    hide jack_happy
    show jack_neutral at left
    jack "Mas, em algum momento quando crescemos, essa criatividade parece ficar confinada."
    jack "Talvez por pressão da sociedade para que sejamos \"normais\" e não chamemos muita atenção, ou para não causar incômodo aos outros que estão por perto."
    hide jack_neutral
    show jack_confused at left
    jack "Talvez seja isso que eu precise. Preciso deixar minha criatividade florescer, sem me preocupar com o quão \"estranha\" minha história se pareça."
    jack "Não posso deixar que o medo de parecer estranho ou fora do normal limite minha imaginação. Se uma ideia surgir, devo usá-la e permitir que ela cresça em minha mente ou sirva de auxílio para outras ideias."
    hide jack_confused
    show jack_smile at left
    jack "Em outras palavras, preciso me reconectar com minha criança interior e deixar que ela vá me dando ideias caso eu não consiga sozinho."
    jack "Acho que isso vai me ajudar com meu livro."
    $ GainInspiration(.5)
    
    #jump park_choices
    $ CheckEnergyJump("park_choices")