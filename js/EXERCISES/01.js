// JUEGO PIEDRA, PAPEL O TIJERA

var opciones = ['Piedra', 'Papel', 'Tijera'];

function jugador(){
    let jugador = parseInt(prompt('[1]Piedra, [2]Papel, [3]Tijera'));
    if (jugador === 1 || jugador === 2 || jugador === 3){
        return jugador;
    } else{
        return jugador();
    }
}
var jugador = jugador();

//jugador();

function cpu(){
    return parseInt(Math.random()*opciones.length);
}

var cpu = cpu();

function validacion(){
    // let pos = cpu--;
    // opcion cpu en texto
    for(let i=0;i<=3;i++){
        if (cpu-1 === i){
            var opcion_cpu = opciones[i];
        }
    }

    // empate
    if (jugador === cpu){
        console.log(`EMPATE, cpu eligió ${opcion_cpu}`);

    // cpu gana
    } else if((jugador === 1 && cpu === 2) || (jugador === 2 && cpu === 3) || (jugador === 3 && cpu === 1)){
        console.log(`GANÓ CPU, con: ${opcion_cpu}`);
    } else{
        console.log(`GANASTE, cpu eligió: ${opcion_cpu}`);
    }
}
validacion()

