// CUPONES DE DESCUENTOS

const cupones = [
    {name: "cupon1", discount:0.15},
    {name: "cupon2", discount:0.30},
    {name: "cupon3", discount:0.25}
];

function validacion(opcion){
    var validar = cupones.find(function(coupon){
         var cupon_name = coupon.name == opcion;
         return cupon_name;
    });
    return validar;
    
} 

const reloj = 1000

function opcionDescuento(){
    let input = document.getElementById("InputCupon");
    const opcion_cupon = input.value;
    var c = validacion(opcion_cupon);
    if (!c){
        alert(`El cupón "${opcion_cupon}" no es valido`);
    } else{
        var outputP = document.getElementById("ValorP");
        var dis = c.discount;
        var valor = reloj - (reloj * dis);
        outputP.innerText = 'Valor a pagar: $' + valor;
    }
}

