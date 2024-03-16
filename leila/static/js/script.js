/*
var nome = prompt('Qual o seu nome?');
const pi = 3.14;

console.log('Nome: '+ nome)
let idade = prompt('Qual a sua idade?')

function maiorDeIdade(idade){
    if(idade >= 18){
    alert("Maior de idade")
} else {
    alert("Menor de idade")
}
}

for (let i=0; i<3; i++){
    confirm('Confirme'+i+' vezes.');
}

switch (nome){
    case "Murilo":
        maiorDeIdade(prompt('Qual a sua idade?'));
        break;

    case "Werlon":
        alert("Pedir revisão");
        break;

    case "Grilo":
        alert("cri cri cri cri cri");
        break;
}*/

// Seleciona elementos
const btnLogout = document.getElementById('logout');
const modal = document.getElementById('modal');

// Ao clicar no botão logout, mostra o modal
btnLogout.addEventListener('click', () => {
    modal.style.display = "block";
})
const modalContainer = document.getElementById('modal-container');
btnLogout.addEventListener('click', () => {
    modalContainer.style.display = "block";
})


// Obter referência ao elemento <body>
const body = document.querySelector('body');

// Função para alternar entre os modos
function toggleMode() {
    body.classList.toggle('dark-mode');
    body.classList.toggle('light-mode');
}

// Exemplo de uso: alternar o modo ao clicar em um botão
const modeToggleButton = document.getElementById('modeToggleButton');
modeToggleButton.addEventListener('click', toggleMode);