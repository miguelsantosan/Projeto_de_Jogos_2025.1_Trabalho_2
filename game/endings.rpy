# A
# Inspiração para terminar o livro
label ending_A:
    hide screen StatsUI
    scene bg writing room with Fade(1, 3.0, 1)

    # Debug
    #jack "Final A"

    show jack_smile at left
    jack "Finalmente de volta em casa."
    jack "Essa saída acabou me sendo bem útil. Consegui encontrar inspiração para desenvolver uma boa história para meu livro. Agora só preciso colocá-la em prática."
    hide jack_smile
    show jack_happy at left
    jack "Mesmo que esse livro não seja o suficiente para me livrar da dívida por completo, pelo menos poderei continuar com minha casa por um bom tempo."
    jack "E agora que sei o que fazer quando passo por um bloqueio criativo, será mais fácil de lidar com isso caso aconteça novamente com algum livro futuro."
    #hide jack_happy
    #show jack_smile at left
    jack "Agora, é hora de escrever e terminar esse livro!"
    scene ending a with Dissolve(1)
    pause

    jump credits
    #return

# B
# Inspiração para escrever parte do livro, mas não terminá-lo
label ending_B:
    hide screen StatsUI
    scene bg writing room with Fade(1, 3.0, 1)

    # Debug
    #jack "Final B"

    show jack_sad at left
    jack "Não consegui inspiração suficiente para escrever o resto de meu livro."
    hide jack_sad
    show jack_neutral at left
    jack "Mas pelo menos consegui alguma coisa, o que já é melhor do que nada. Espero que isso sirva de pontapé para eu conseguir desenvolver o resto para terminar a história."
    hide jack_neutral
    show jack_smile at left
    jack "Então, não tenho tempo a perder. Uma página de cada vez."
    scene ending b with Dissolve(1)
    pause

    jump credits
    #return

# C
# Sem inspiração suficiente para escrever alguma coisa
label ending_C:
    hide screen StatsUI
    scene bg writing room with Fade(1, 3.0, 1)

    # Debug
    #jack "Final C"

    show jack_sad at left
    jack "Não consegui inspiração nenhuma... Essa miha saída acabou sendo uma perda de tempo."
    jack "Não sei mais o que fazer. Tentar sair novamente amanhã?"
    jack "Mas o que eu poderia fazer de diferente? Ir a algum outro lugar?"
    jack "Bem... acho que vou ter que descobrir isso amanhã. Um dia de cada vez."
    scene ending c with Dissolve(1)
    pause

    jump credits
    #return

label ending_smoke_root:
    hide screen StatsUI
    scene bg house smoke far with Fade(1, 3.0, 1)

    show jack_surprised at left
    jack "Mas o que!? É a direção da minha casa? Será que é dela que está saindo fumaça?"
    jack "Eu preciso ir lá verificar o que está acontecendo!"
    
    scene bg dark with Fade(1, 3.0, 1)
    scene bg house smoke with Dissolve(1)

    show jack_surprised at left
    jack "Mas o que está acontecendo? O que houve com minha casa?"
    "Você mora aí?"
    show man1 at right
    jack "Sim, é a minha casa!"
    man "Começou a sair fumaça de sua casa. Alguns moradores da região viram e trouxeram baldes com água para apagá-lo, mas não estamos dando conta sozinhos, precisamos de ajuda."
    jack "Sim! Eu vou ajudar a apagar o fogo!"
    
    scene bg dark with Fade(1, 3.0, 1)
    scene bg house aftermath with Dissolve(1)
    
    show jack_sad at left
    show man1 at right
    jack "Parece que conseguimos apagar o fogo."
    man "Sim. Sinto muito pela sua casa, mas pelo menos apenas uma parte dela ficou destruída."
    jack "Sim... Obrigado pela ajuda."
    hide man1
    scene bg dark with Fade(1, 3.0, 1)
    scene bg bedroom
    show jack_sad at left
    jack "Ao que tudo indica, as velas que eu esqueci acesas antes de sair atearam fogo no meu escritório, e daí ele começou a se espalhar."
    jack "Agora meu escritório está destruído, mas posso pegar algumas ferramentas antigas para escrever."

    if inspiration >= 3:
        jump ending_D
    else:
        jump ending_E

# D
# Apagou o fogo + inspiração para escrever alguma coisa
# inspiration >= 3
label ending_D:
    #scene bg bedroom with Fade(1, 3.0, 1)
    scene bg bedroom

    # Debug
    #jack "Final D"

    show jack_sad at left
    jack "Pelo menos eu consegui alguma inspiração, então ainda vou poder escrever alguma coisa."
    jack "Só espero não ficar muito abalado pelo que aconteceu com a casa e não conseguir me focar na escrita, me impedindo de terminar o livro."
    jack "Mas bem, uma página de cada vez..."
    hide jack_sad
    show jack_neutral at left
    jack "Não adianta ocupar minha mente com isso, devo focar no que eu posso fazer agora e escrever custe o que custar."
    scene ending d with Dissolve(1)
    pause

    jump credits
    #return

# E
# Apagou o fogo + sem inspiração para escrever
# inspiration < 3
label ending_E:
    #scene bg bedroom with Fade(1, 3.0, 1)
    scene bg bedroom

    # Debug
    #jack "Final E"

    show jack_cry at left
    jack "Mas não consegui nenhuma inspiração para meu livro..."
    hide jack_cry
    show jack_disgust at left
    jack "Bem, pelo menos poderia ter sido pior, eu podia ter perdido minha casa inteira."
    jack "Talvez eu consiga inspiração se der uma saída algum outro dia."
    jack "Só espero conseguir escrever alguma coisa. Tudo que não preciso agora é perder a casa ainda por cima..."
    scene ending e with Dissolve(1)
    pause

    jump credits
    #return

# F
# Não olhou a fumaça e voltou pra casa pegando fogo
label ending_F:
    hide screen StatsUI
    scene bg house fire turner with Fade(1, 3.0, 1)

    # Debug
    #jack "Final F"

    show jack_surprised at left
    jack "Não pode ser... É a direção da minha casa. Será que..."
    hide jack_surprised
    show jack_disgust at left
    jack "Não... por favor não seja a minha casa... Agora eu tenho que ir verificar."

    scene bg dark with Fade(1, 3.0, 1)
    scene bg house fire close

    show jack_surprised at left
    jack "MEU DEUS!!!"
    jack "É A MINHA CASA!"
    jack "COMO ISSO FOI ACONTECER?"
    "Senhor Williams!"
    show butler at right
    mordomo "Senhor Williams! Precisei dar uma saída e quando voltei a casa estava pegando fogo!"
    jack "Mas como isso foi acontecer?"
    mordomo "Pelo que me contaram, o fogo começou do lado de dentro da casa. Alguns moradores da região viram e tentaram apagá-lo com baldes de águas, mas não foi suficiente."
    jack "{i}(As velas de meu escritório! Saí com tanto pressa que esqueci de apagá-las. O fogo deve ter começado por lá e se espalhou pelo resto de minha casa.){/i}"
    hide jack_surprised
    show jack_cry at left
    jack "Não tem mais jeito, perdi minha casa, e ainda tenho minha dívida. Não tenho nem como escrever meu livro agora e me salvar. Acabou tudo para mim."
    scene ending f with Dissolve(1)
    pause

    jump credits
    #return