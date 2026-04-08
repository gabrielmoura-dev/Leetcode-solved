function weekMoney () {
    let resultMoney = [];
    
    for (i = 1; i < 8; i++) {
        resultMoney.push(i);
    }

    return resultMoney;
}

const weekValues = weekMoney();
console.log(weekValues);
