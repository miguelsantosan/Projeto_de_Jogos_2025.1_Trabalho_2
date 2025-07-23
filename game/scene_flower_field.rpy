default has_looked_at_flowers = False
default has_looked_at_buterflies = False
default has_looked_at_field = False

define senhora1 = Character("Senhora")
define senhora2 = Character("Mary")

label flower_field:
    scene bg flower field with Dissolve(1)
    show jack_surprised at left

    if has_visited_flower_field == False: # Primeira vez visitando
        $ has_looked_at_flowers = False
        $ has_looked_at_buterflies = False
        $ has_looked_at_field = False
        $ CheckCandle()
        jack "Nossa, como esse campo é bonito."
        jack "As flores são tão coloridas, e há várias borboletas voando de uma flor a outra. Há uma paz nesse lugar, é diferente da cidade movimentada."
        jack "Imagino o que possa haver no final do campo."
        hide jack_surprised
        $ has_visited_flower_field = True

    #show jack_neutral at left
    jump flower_field_choices
    
label flower_field_choices:
    scene bg flower field with Dissolve(1)
    menu:
        "Olhar as flores." if has_looked_at_flowers == False:
            $ has_looked_at_flowers = True
            $ SpendEnergy()
            jump flower_field_flowers
        "Olhar as borboletas" if has_looked_at_buterflies == False:
            $ has_looked_at_buterflies = True
            $ SpendEnergy()
            jump flower_field_butterflies
        "Caminhar pelo campo." if has_looked_at_field == False:
            $ has_looked_at_field = True
            $ SpendEnergy()
            jump flower_field_house
        "Voltar para a praça.":
            $ SpendEnergy()
            jump main_square

label flower_field_flowers:
    scene bg flower field flowers with Dissolve(1)
    jack "As flores são muito bonitas. E há tantas delas. Deve ter levado bastante tempo pro jardim ter ficado assim."
    jack "\"Tempo\"... Justamente o que eu não tenho."
    jack "Ugh..."
    jack "Não consigo tirar meu livro da cabeça... Preciso me esforçar mais se eu quiser me distrair com alguma coisa e obter inspiração."

    #jump flower_field_choices
    $ CheckEnergyJump("flower_field_choices")

label flower_field_butterflies:
    scene bg flower field butterflies with Dissolve(1)
    jack "Nossa, como essas borboletas são bonitas. Fica até difícil decidir o que é mais bonito, elas ou as flores onde elas pousam."
    jack "Elas ficam voando de uma flor a outra. Tão livres."
    jack "Quem me dera eu tivesse essa liberdade... Mas estou preso tentando escrever meu -"
    jack "Ugh. Agora meu livro me veio à cabeça. Isso não me ajudou em nada."

    #jump flower_field_choices
    $ CheckEnergyJump("flower_field_choices")

label flower_field_house:
    scene bg flower field walk with Dissolve(1)

    show jack_surprised at left
    jack "Nossa, esse campo é maior do que eu achava."
    jack "Espera, aquilo é uma casa? Não sabia que morava alguém aqui. Achava que essa propriedade fazia parte do parque."

    scene bg flower field house

    show jack_surprised at left
    jack "Que casa bonita. Até a varanda é cheia de flores. Quem será que mora aqui?"
    jack "Tem alguém chegando na porta..."
    "Quem está aí?"
    show oldLady at right
    senhora1 "Quem é você?"
    jack "Uhh..."
    hide jack_surprised
    show jack_neutral at left
    jack "Me chamo Jack. Jack Williams, escritor."
    jack "Eu sempre tive curiosidade de andar por este campo cheio de flores, ver o que havia depois dele. Não sabia que tinha uma casa aqui."
    senhora1 "Sim, moro aqui desde que me casei."
    senhora1 "Sempre tive gosto por jardinagem, então comecei a comprar algumas mudas e trazer para cá para plantar."
    senhora1 "Com o tempo, o número de flores foi crescendo, e quando vi, tinha flores pra todos os lados."
    senhora1 "Este campo se tornou meu orgulho, cultivado durante muitos anos como um passatempo."
    hide jack_neutral
    show jack_smile at left
    jack "Sim, é muito bonito mesmo. As flores tem cores muito vibrantes."
    jack "Espero não estar incomodando."
    senhora1 "Que nada, meu jovem. Uma senhora da minha idade tem bastante tempo livre. Ainda mais agora que meus filhos já estão todos crescidos e casados."
    jack "A propósito, qual seu nome?"
    senhora2 "Me chamo Mary."
    senhora2 "Me diga meu jovem, o que te traz aqui?"
    jack "Bem, como já disse, minha curiosidade..."
    senhora2 "Não, além disso."
    jack "Hã?"
    senhora2 "Está escrito no seu rosto. Há alguma coisa te abalando."
    hide jack_smile
    show jack_disgust at left
    jack "Tá tão na cara assim?"
    senhora2 "Um pouco. Você tenta colocar uma cara de quem não está passando por nada, mas seus olhos não mentem. Você parece perdido, sem rumo. Imagino que seja isso que te fez andar até aqui."
    jack "Bem..."
    jack "Como eu disse, sou escritor. Mas tenho andado com um bloqueio criativo, as ideias não me vem à cabeça de jeito nenhum."
    jack "E ainda por cima, estou endividado e se eu não terminar meu livro logo não terei como manter minha casa."
    jack "Tenho ficado dias e noites tentando escrever, fico acordado até tarde na esperana de que as ideias apareçam, mas não me vem nada."
    jack "Então resolvi dar uma saída para procurar alguma coisa que me inspire a escrever."
    senhora2 "Meu jovem, parece que você está sofrendo de estresse. Suas preocupações tomam a sua cabeça e formam uma névoa, te impedindo de se concentrar."
    senhora2 "Já passei por isso. Quando tive meu primeiro filho fiquei um bom tempo sem poder pegar no meu jardim direito. Primeiro por conta da gravidez, depois porque precisava cuidar do meu bebê."
    senhora2 "Por causa disso, no pouco tempo que eu conseguia mexer no jardim, eu não conseguia me concentrar direito. De repente, algo tão natural se tornou uma tarefa muito complicada."
    senhora2 "E depois de um tempo, meu jardim estava cheio de falhas. Plantas morrendo porque eu não regava direito, mato crescendo porque não era podado. Nem parecia o jardim que eu conhecia antes."
    hide jack_disgust
    show jack_neutral at left
    jack "Nossa. Como a senhora conseguiu superar isso?"
    senhora2 "Depois de um tempo, percebi que minhas preocupações haviam tomado conta de mim."
    senhora2 "Mas eu precisava ser mais forte do que elas, então resolvi fazer alguma outra coisa. Pedi para minha irmã tomar conta do meu filho por um dia e saí para passear com meu marido."
    senhora2 "Fomos ver as paisagens e arquitetura da cidade. Vimos até uma peça de teatro."
    senhora2 "Essas distrações me ajudaram a recuperar meus eixos e ficar menos preocupada. No dia seguinte, eu já estava mais animada para meer no meu jardim."
    senhora2 "Não fiquei totalmente recuperada de um dia pro outro, mas só o fato de conseguir fazer o que eu fazia antes me deixou animada, e, com isso, consegui continuar com minha jardinagem."
    senhora2 "E assim, aos poucos fui melhorando. Quando vi, estava nova em folha."
    senhora2 "Tente se distrair com alguma outra coisa que você gosta por um dia ou dois. Isso deve ajudar a liberar sua mente e acabar com seu bloqueio."
    hide jack_neutral
    show jack_smile at left
    jack "É uma boa ideia. Não tenho muito tempo sobrando, mas acredito que um dia tentando algo diferente não vá fazer muita diferença."
    jack "Obrigado pelo conselho. Agora, se me dá licença, preciso continuar andando."
    $ GainInspiration(1)
    
    #jump flower_field_choices
    $ CheckEnergyJump("flower_field_choices")