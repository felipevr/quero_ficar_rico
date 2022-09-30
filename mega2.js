var saco = [];
var incremental = true;
var maior = 60;

function pegaUmNumero() {
    if(incremental) {
        var randomNumber;
		
		do {
			randomNumber = Math.floor(Math.random() * maior) + 1;
		} while (verificaRepetido(randomNumber, saco));
		
        saco.push(randomNumber);
		
		if(saco.length == 60) {
			incremental = false;
		}
    } else {
        randomNumber = removeElemento();
		
		if(saco.length == 0) {
			incremental = true;
		}
    }
	//console.log('gerei o numero ' + randomNumber);

    return randomNumber;
}

function removeElemento() {
    var tam = saco.length;

    if(tam == 1) {
        return saco.pop();
    }

    randomIndex = Math.floor(Math.random() * tam);

    return parseInt(saco.splice(randomIndex, 1));
}

function geraAih(tamanho, novo_maior) {

    if(novo_maior !== undefined) {
        maior = novo_maior;
    }

    var numbers = [];
    for(var i = 0; i < tamanho; i++) {
        numbers.push(pegaUmNumero());
    }

    //sort
    //console.log(numbers.join(", "));
    numbers = ordena(numbers);

    //document.getElementById("numbers").innerHTML = numbers.join(" - ");
    console.log(numbers.join(", "));
}

function ordena(numbers) {
    var highestNumber = 0;
    for(var m = 0; m < numbers.length; m++) {
        for(var n = m + 1; n < numbers.length; n++) {
            if(numbers[n] < numbers[m]) {
                //console.log(numbers[n] + " < " + numbers[m]);
                highestNumber = numbers[m];
                numbers[m] = numbers[n];
                numbers[n] = highestNumber;
            }
        }
    }
    return numbers;
}

function verificaRepetido(numero, lista) {
	for(var y = 0; y < maior; y++) {
		if(lista[y] == numero) {
			return true;
		}
	}
	return false;
}


function generate2(size, lowest, highest) {
	var numbers = [];
	for(var i = 0; i < size; i++) {
		var add = true;
		var randomNumber = Math.floor(Math.random() * highest) + 1;
		for(var y = 0; y < highest; y++) {
			if(numbers[y] == randomNumber) {
				add = false;
			}
		}
		if(add) {
			numbers.push(randomNumber);
		} else {
			i--;
		}
	}
  
	//sort
	numbers = ordena(numbers);
  
    //document.getElementById("numbers").innerHTML = numbers.join(" - ");
    console.log(numbers.join(", "));
}

const qtdJogos = 10;
// for(let n = 0; n < qtdJogos; n++) {
//     generate(6, 1, 60);
// }

function megaSena(qtdJogos, dezenas) {

    console.log('gerando ' + qtdJogos + ' jogos de ' + dezenas + ' dezenas:');

    for(let n = 0; n < qtdJogos; n++) {
        //generate2(dezenas, 1, 60);
		geraAih(dezenas);
    }

}

console.log('descartar o primeiro jogo:');
megaSena(1,10);

megaSena(2, 7);
megaSena(1, 8);
megaSena(1, 9);
megaSena(3, 8);
megaSena(6, 7);