const getData = () => ({
    resultado: "",
    nome_sorteado: "",
    pokemon_click: false,
    distro_click: false,
    pontuacao:{
        resposta:'',
        pontos:0,
    },
    info_resposta:{
        nome:'',
        imagem:'',
    },
    

    async sorteiaNome() {
      await fetch('/game/api/sorteia_nome')
          .then((response) => response.json())
          .then(data => {
            this.nome_sorteado = data.name;
          }) 
    },

    async pegarDadosDistro() {
        await fetch(`/game/api/linux/${this.nome_sorteado}`)
            .then((response) => response.json())
            .then(data => {
              this.info_resposta.nome = data.nome;
              this.info_resposta.imagem = data.imagem;
            }) 
      },
      
      async pegarDadosPokemon() {
        await fetch(`/game/api/pokemon/${this.nome_sorteado}`)
            .then((response) => response.json())
            .then(data => {
              this.info_resposta.nome = data.nome;
              this.info_resposta.imagem = data.imagem;
            });
      },

    async pontuar(){
        // pega qual o tipo do nome
        await fetch(`/game/api/verificar?nome_search=${this.nome_sorteado}`)
        .then((response) => response.json())
          .then(data => {
            this.resultado = data.resultado;
          })
        console.log(this.resultado)
        if(this.resultado == 'Distribuição Linux' && this.distro_click){
            this.pontuacao.resposta = "Você Acertou!!!";
            this.pontuacao.pontos++;
            await this.pegarDadosDistro();
            console.log(this.info_resposta)
        }
        else if (this.resultado != 'Distribuição Linux'  && this.distro_click){
            this.pontuacao.resposta = "Você Errou!!!";
            await this.pegarDadosPokemon();
            console.log(this.info_resposta)
        }
        else if(this.resultado == 'Pokemon' && this.pokemon_click){
            this.pontuacao.resposta = "Você Acertou!!!";
            this.pontuacao.pontos++;
            await this.pegarDadosPokemon();
            console.log(this.info_resposta)
        }
        else if (this.resultado != 'Pokemon' && this.pokemon_click){
            this.pontuacao.resposta = "Você Errou!!!";
            await this.pegarDadosDistro();
            console.log(this.info_resposta)
        }
        this.pokemon_click = false;
        this.distro_click = false;
    },

});
