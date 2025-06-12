document.addEventListener('DOMContentLoaded', function () {
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            const btn = document.querySelector('.button_close');
            if (btn) {
                btn.click();
            } else {
                console.log("Botão não encontrado.");
            }
        }
    });
});

document.addEventListener('htmx:afterSwap', (event) => {
    // Se o input ainda existir na nova página, recoloque o foco nele
    const input_busca = document.querySelector("input[name='busca']");
    if (input_busca) {
        input_busca.focus();
        // Coloca o cursor no final do texto
        input_busca.selectionStart = input_busca.selectionEnd = input_busca.value.length;
    }
    const input_nome_usuario = document.querySelector("input[name=nome_usuario]")
    if (input_nome_usuario) {
        input_nome_usuario.focus();
        input_nome_usuario.selectionStart = input_nome_usuario.selectionEnd = input_nome_usuario.value.length;
    }

});

function BaixarPDF(button) {
    const urlGerarPDF = button.getAttribute('data-url');    
    fetch(urlGerarPDF)
        .then(response => response.blob())
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = "ramais.pdf";
            document.body.appendChild(a);
            a.click();
            a.remove();
            window.URL.revokeObjectURL(url);
        })
        .catch(error => console.error("Erro ao baixar PDF:", error));
}