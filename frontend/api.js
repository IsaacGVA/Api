// Função assíncrona
async function buscarUsuarios() {

  // Faz a requisição para a API
  const resposta = await fetch(
    "https://jsonplaceholder.typicode.com/users"
  );

  // Converte a resposta para JSON
  const usuarios = await resposta.json();

  // Pega a lista do HTML
  const lista = document.getElementById(
    "listaUsuarios"
  );

  // Limpa a lista antes de adicionar novos itens
  lista.innerHTML = "";

  // Percorre todos os usuários
  usuarios.forEach(usuario => {

    // Adiciona cada usuário na lista
    lista.innerHTML += `
      <li>
        ${usuario.name}
      </li>
    `;

  });

}