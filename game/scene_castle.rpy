default has_looked_at_landscape = False
default has_looked_at_vegetation = False
default has_looked_at_ruins = False

label castle:
    scene bg castle with Dissolve(1)
    show jack_neutral at left

    if has_visited_castle == False:
        $ has_looked_at_landscape = False
        $ has_looked_at_vegetation = False
        $ has_looked_at_ruins = False
        $ CheckCandle()
        jack "Esse castelo... Ouvi histórias de que ele foi atacado séculos atrás. Ficou tão destruído que ninguém voltou pra morar nele, mesmo depois de todo esse tempo."
        jack "Uma estrutura solitária e esquecida, tão grande, mas também tão vazia."
        jack "Daria uma ótima paisagem para pintar. Mas como sou escritor, não vou me preocupar com isso."
        $ has_visited_castle = True
    
    jump castle_choices

label castle_choices:
    scene bg castle with Dissolve(1)
    menu:
        "Olhar a paisagem" if has_looked_at_landscape == False:
            $ has_looked_at_landscape = True
            $ SpendEnergy()
            jump castle_landscape
        "Olhar a vegetação" if has_looked_at_vegetation == False:
            $ has_looked_at_vegetation = True
            $ SpendEnergy()
            jump castle_vegetation
        "Olhar as ruínas" if has_looked_at_ruins == False:
            $ has_looked_at_ruins = True
            $ SpendEnergy()
            jump castle_ruins
        "Voltar para a praça.":
            $ SpendEnergy()
            jump main_square

label castle_landscape:
    scene bg castle with Dissolve(1)

    jack "Tem uma torre solitária do castelo sobrando."
    jack "Apesar do castelo ter sido destruído com o tempo, ela continua de pé."
    jack "Uma paisagem bonita, mas a torre solitária reflete como o castelo ficou esquecido com o tempo."
    if has_looked_at_ruins == False:
        jack "Será que tem algo de interessante dentro dela? Talvez valha a pena dar uma olhada, já que eu cheguei até aqui."
    else:
        jack "Acho que já gastei tempo depois nela, melhor eu ir andando."

    #jump castle_choices
    $ CheckEnergyJump("castle_choices")
    
label castle_vegetation:
    scene bg castle vegetation with Dissolve(1)
    
    show jack_confused at left
    jack "Esse castelo está abandonado há tanto tempo, já cresceu muita vegetação em seus arredores."
    jack "Há uma certa melancolia nessa vista. O abandono desse lugar em ruínas, deixando o mato crescer livremente."
    jack "Mas também tem uma certa beleza. A perseverança da vegetação, que continua a crescer, independente de tudo, sem se deixar abalar."
    jack "E os galhos... Se espalhando, como uma ideia que leva a outra, permitindo que todo o conjunto de uma história cresça em harmonia."
    jack "É estranho dizer isso mas... isso me anima um pouco."
    jack "De certa forma... acabo vendo a mim mesmo nessa vegetação. Eu perseverei até agora e, apesar dos pesares, consegui manter minha carreira de escritor até hoje."
    jack "Só preciso ser forte e continuar me dedicando. Não posso me deixar abalar. Uma hora virá uam ideia e, com ela, tenho o alicerce necessário para continuar escrevendo e deixar que outras ideias floresçam."
    hide jack_confused
    show jack_smile at left
    jack "Assim como essa vegetação e seus galhos que se espalharam."
    jack "É, isso me animou um pouco e me deixou um pouco mais confiante pra continuar escrevendo meu livro. Devo manter minha cabeça erguida e seguir em frente."
    $ GainInspiration(1)

    #jump castle_choices
    $ CheckEnergyJump("castle_choices")
    
label castle_ruins:
    scene bg castle inside with Dissolve(1)
    
    show jack_neutral at left
    jack "Não sobrou nada dentro do castelo, está completamente vazio. Só sobraram as ruínas da estrutura."
    jack "Há uma certa paz nessa vista, mas nada que me inspire com meu livro, apesar de parecer ser um lugar bem relaxante para passar o tempo."
    jack "Isolado, rodeado pela natureza, sem nada pra me perturbar."
    jack "Talvez eu possa ficar aqui um pouco e dar uma descansada."
    menu:
        "Ficar e descansar por um tempo.":
            scene bg dark with Fade(1, 3.0, 1)
            $ ReplenishEnergy(2)
            #$ GainInspiration(0.5)
            scene bg castle inside
            show jack_smile at left
            jack "Me sinto um pouco melhor agora. Mais leve, mais relaxado."
            hide jack_smile
            show jack_happy at left
            jack "Acho que valeu a pena. Mesmo que não me ajude com ideias pro livro, pelo menos eu desestressei um pouco."
        "Não tenho tempo pra isso.":
            jack "É, não tenho tempo pra isso, preciso manter o foco e tentar achar alguma coisa que me ajude com meu livro."

    #jump castle_choices
    $ CheckEnergyJump("castle_choices")