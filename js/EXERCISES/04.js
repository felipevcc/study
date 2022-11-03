// Calculo altura de triangulo isosceles

function altura(l, b){
    h = Math.sqrt(l**2-((b**2)/4));
    return h;
}

function calculoAltura(){
    var inputLados = document.getElementById("InputLados");
    var inputBase = document.getElementById("InputBase");

    const lados = inputLados.value;
    const base = inputBase.value;

    alert(altura(lados, base));
}