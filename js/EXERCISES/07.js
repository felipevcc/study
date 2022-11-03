// Hallar mediana

// sort  organiza los numeros de menor a mayor

var numsDes = [2,5,1,4];
const nums = numsDes.sort();

console.log('Nums organizados:', nums);

function par(nums){
    if (nums.length % 2 == 0){
        return true;
    } else{
        return false;
    }
}

function mediana(n){
    if (par(n)){
        let pos = parseInt(n.length / 2);
        let promedio = (n[pos-1] + n[pos]) / 2;
        return promedio;
    } else{
        let pos = parseInt(n.length / 2);
        return n[pos];
    }
}
console.log('\nLa mediana es:', mediana(nums));
