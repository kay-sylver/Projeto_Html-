const touchEvent = 'ontouchstart' in window ? 'touchstart' : 'click';
document.getElementById('kirby_image').addEventListener(touchEvent, animate);

alert("JavaScript carregado!");
function animate(e) {
	if (!e) var e = window.event;
	e.cancelBubble = true;
	if (e.stopPropagation) e.stopPropagation();

	if (animate.isRunning) return;
	animate.isRunning = true;

	console.log('animate');
	image = document.getElementById('kirby_image');
	image.src = '../Estética/gif/kirby-awake.gif';

	setTimeout(() => {
		image.src = '../Estética/gif/kirby-asleep.gif';
		animate.isRunning = false;
	}, 3675);
}


function abrirRota(rota){
    alert("A função abriu!");
    

	fetch(rota)
	.then(response => response.text())
	.then(resultado=>{

		document.getElementById("conteudo-rota").innerHTML = resultado;
		document.getElementById("tela-secundaria").style.display = "block";

	    
	});
}

function fecharRota(){
	document.getElementById("tela-secundaria").style.display = "none";


}
