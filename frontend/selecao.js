function openPopup(option) {
    // Exibir o pop-up
    document.getElementById('popup').style.display = 'block';
    
    // Definir o texto da opção selecionada
    document.getElementById('popup').querySelector('h2').innerHTML = option;
}

function closePopup() {
    // Fechar o pop-up
    document.getElementById('popup').style.display = 'none';
}

function confirmVote() {
    // Aqui você pode adicionar lógica para registrar a votação
    alert('Votação confirmada!');
    closePopup();
}

