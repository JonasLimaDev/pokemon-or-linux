const getData = () => ({
    topJogadores: [],

    async getTopPlayers() {
      
      await fetch('/game/api/top/jogadores')
          .then((response) => response.json())
          .then(data => {
            this.topJogadores = data;
          });
    },
})