# ====================
# Personagens
# ====================
define jack = Character("Jack")
define jack_jovem = Character("Jack")
define pai = Character("Joseph")
define mordomo = Character("Alfred")
define policial = Character("Policial")

# ====================
transform half_size: 
    zoom 0.5 #adjust as required

screen candle():
    imagebutton:
        xalign 0.2
        yalign 0.4
        auto "prop candle_%s" at half_size action [ToggleScreen("candle"), Jump("writing room_lit")]

# ====================
# Variáveis
# ====================
default can_return_home = False # Para determinar se pode voltar pra casa ou não
default is_candle_lit = False # Determina se a vela ficou acesa ao sair de casa ou não

# Flags para verificar se cada lugar foi visitado
default has_visited_main_square = False
default has_visited_art_gallery = False
default has_visited_park = False
default has_visited_cathedral = False
default has_visited_castle = False
default has_visited_flower_field = False
default has_seen_smoke = False # Flags para verificar se a fumaça foi vista

# Variáveis
default inspiration = 0 # Contador da inspiração
default energy = 10 # Energia do personagem
default burning = 0 # Contador para o incêndio

# ====================
# Início
# ====================

label start:
    python:
        def SpendEnergy():
            global energy
            energy -= 1
        
        def ReplenishEnergy(n):
            global energy
            energy += n
        
        def GainInspiration(n):
            global inspiration
            inspiration += n
        
        def CheckCandle():
            global burning
            global is_candle_lit
            if is_candle_lit == True:
                burning += 1
        
        def CheckEnergyJump(label):
            import renpy.exports as renpy
            global energy
            if energy > 0:
                renpy.jump(label)
            else:
                renpy.jump("main_square")
        
    # Debug
    #$ inspiration = 5
    #$ has_visited_main_square = True
    #jump main_square
    #call screen candle # Fazer a vela aparecer na tela

    jack "Ugh..."
    jack "Que noite de sono péssima. Fiquei até tarde tentando pensar em algo para escrever em meu livro."

    scene bg old house with Dissolve(1)

    show dad at right
    show jack_young at left

    pai "Filho, já decidiu o que você quer ser quando crescer?"
    jack_jovem "Sim pai, quero virar um escritor!"
    pai "Um escritor? Hahaha."
    pai "Escrever livros é trabalho duro, meu filho. É preciso de criatividade para desenrolar as histórias. Além disso, você precisa se organizar para não se contradizer no meio do livro."
    pai "Tem certeza que é isso que você quer fazer?"
    jack_jovem "Sim pai, é o meu sonho."
    pai "Hahaha, boa sorte com isso meu filho. Você terá que se dedicar para conseguir escrever histórias que encantem as pessoas."
    pai "Mas se é o que você quer, irei confiar na sua decisão."

    hide dad
    hide jack_young
    with dissolve

    "Anos se passam, e o pai de Jack vem a falecer."
    "Jack herdou uma boa quantia de dinheiro, mas ainda assim estava aflito com a perda."
    "Desolado, Jack resolve pegar sua herança mais um empréstimo para comprar uma casa isolada, para poder se dedicar a seu sonho de escrever."
    "Apesar de ter conseguido publicar alguns livros, Jack não fez muito sucesso, e o dinheiro se esgota com o passar do tempo."
    "Sua última esperança é terminar seu último livro para poder pagar sua dívida e não perder a casa."

    scene bg dark with Dissolve(1)

    jack "Preciso levantar e voltar ao trabalho."
    menu:
        "Levantar.":
            scene bg bedroom with Dissolve(1)

    show jack_neutral at left

    jack "Mais um dia se passa, mais um dia se aproxima o prazo final para eu terminar meu livro."

    hide jack_neutral
    show jack_sad at left

    jack "Não acredito, fiquei uma semana inteira sem conseguir escrever uma página sequer."
    jack "Não importa o quanto eu tente, não consigo pensar em nada para continuar minha história. As ideias simplesmente não fluem na minha cabeça."
    jack "Preciso tentar escrever alguma coisa."

    "{i}Toc-toc{i}"

    hide jack_sad
    show jack_confused at left
    jack "O que foi?"
    show butler at right
    mordomo "Senhor, há um policial na entrada que quer vê-lo."
    jack "Diga a ele que já estou indo."
    hide butler
    hide jack_confused
    show jack_disgust at left
    jack "Acho que sei exatamente sobre o que ele quer falar."

    ## Falando com o policial
    scene bg dark with Dissolve(1)
    scene bg house front yard
    show jack_disgust at left
    show cop at right

    policial "Senhor Williams, acredito que já saiba o motivo de minha vinda."
    jack "Sim..."
    policial "Pois bem, como já sabe, seu prazo para pagar sua dívida está se aproximando do final. E como o senhor já vem atrasando algumas parcelas, o valor vem se acumulando. Devo lembrá-lo que, caso o senhor não pague a dívida, perderá a casa."
    policial "Esta carta diz o valor exato a ser pago."
    show letter
    hide jack_disgust
    show jack_confused at left
    jack "Como assim!? Esse valor é absurdo!"
    hide letter
    policial "Bem, infelizmente, a sua modalidade de empréstimo é a que possui a maior taxa de juros. E como o senhor já vem atrasando os pagamentos há um tempo..."
    hide jack_confused
    show jack_sad at left
    jack "Entendi..."
    jack "Obrigado pelo aviso. Passar bem."
    hide cop with dissolve
    jack "A situação é pior do que eu imaginava. Preciso ir para meu escritório e começar a escrever imediatamente."

    ## 
    scene bg writing room dark with Dissolve(1)
    show jack_neutral at left
    jack "Hmm..."
    jack "Está muito escuro aqui, preciso acender as velas para poder escrever."

    menu:
        "Acender as velas":
            scene bg writing room

    jack "Pronto, agora posso enxergar alguma coisa."
    jack "Hora de pegar no trabalho e escrever."

    scene bg writing desk

    show jack_neutral at left

    jack "..."
    jack "......"

    hide jack_neutral
    show jack_sad at left

    jack "........."

    hide jack_sad
    show jack_disgust at left

    jack "............"
    jack "Não adianta, não consigo pensar em nada."

    scene bg writing room

    hide jack_disgust
    show jack_sad at left

    jack "Talvez se eu sair um pouco de casa, eu consiga alguma inspiração para terminar meu livro."

    menu:
        "Sair de casa.":
            $ is_candle_lit = True # 
        "Apagar as velas e sair de casa.":
            $ is_candle_lit = False

    # Debug
    #if is_candle_lit == True:
    #    jack "Apaguei a vela"
    #else:
    #    jack "Não apaguei a vela"

    jump main_square

    return
