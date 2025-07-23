label main_square:
    scene bg mainsquare with Dissolve(1)
    show screen StatsUI
    
    if has_visited_main_square == False:
        show jack_sad at left
        jack "Apesar da situação, é bom dar uma saída de casa. Espero que isso me ajude a achar alguma inspiração."
        jack "Mas há tantos lugares na cidade para visitar, e não tenho muito tempo para gastar."
        jack "Além disso, tenho dormido mal essas últimas noites, então também não tenho muita energia para ficar andando o dia inteiro."
        hide jack_sad
        show jack_neutral at left
        jack "Há um parque não muito longe daqui, talvez olhar as pessoas passando o tempo e se divertindo melhore meu astral."
        jack "Ou a catedral da cidade, cheia de quadros e vitrais muito bonitos, talvez animem meu lado artístico."
        jack "Ou o castelo antigo abandonado, talvez eu consigo imaginar alguma história boa vendo sua paisagem."
        jack "Tem também o campo florido que eu sempre tive a curiosidade de explorar e ver o que há depois dele."
        hide jack_neutral
        show jack_surprised at left
        jack "É mesmo! Acabo de lembrar que está tendo uma exposição de pinturas na cidade. Talvez eu possa pegar dicas com algum artista sobre como lidar com bloqueio criativo."
        jack "Apesar de pintura e escrita serem áreas diferentes, imagino que lidar com bloqueios não seja muito diferente entre elas."
        $ has_visited_main_square = True
        hide jack_surprised
    
    # Debug
    #$ burning = 2

    if burning >= 2 and has_seen_smoke == False:
        jump seeing_smoke
    
    if energy > 0:
        jump main_square_choices
    else:
        show jack_neutral at left
        jack "Já andei bastante hoje, estou ficando cansado."
        jack "Acho que é hora de eu voltar para casa."

        if has_seen_smoke == True:
            jump ending_F # Casa pegando fogo
        elif inspiration >= 5:
            jump ending_A # Inspiração para terminar o livro
        elif inspiration >= 3:
            jump ending_B # Inspiração para escrever parte do livro, mas não terminá-lo
        else:
            jump ending_C # Sem inspiração suficiente para escrever alguma coisa

    jump main_square_choices

label main_square_choices:
    scene bg mainsquare

    show jack_neutral at left 
    jack "E agora, onde devo ir?"
    menu:
        "Galeria de arte": #if has_visited_art_gallery == False
            $ SpendEnergy()
            jump art_gallery
        "Parque": #if has_visited_park == False
            $ SpendEnergy()
            jump park
        #"Catedral": #if has_visited_cathedral == False
        #    $ SpendEnergy()
        #    jump cathedral
        "Castelo em ruínas": #if has_visited_castle == False
            $ SpendEnergy()
            jump castle
        "Campo florido": #if has_visited_flower_field == False
            $ SpendEnergy()
            jump flower_field
        "Voltar para casa" if inspiration >= 4:
            if has_seen_smoke == True:
                jump ending_bad

label seeing_smoke:
    scene bg smoke

    show jack_confused at left
    jack "Hã? Tem uma fumaça escura no céu. Não lembro de ter visto fumaça no céu mais cedo."
    $ has_seen_smoke = True
    menu:
        "Não deve ser nada.":
            jack "Deve ser só uma dessas fábricas recentes da cidade. Não deve ser nada."
            hide jack_confused
            jump main_square
        "De onde será que vem essa fumaça?":
            jack "Talvez seja bom dar uma olhada."
            jump ending_smoke_root # Vai parar o incêndio