let table = document.getElementById("table")
let arr =[]
let k=1
let displayNum = document.getElementById("displayNum")
for (var i=0;i<9;i++){
    let row = document.createElement('tr')
    for(let p=0;p<10;p++){
        let button = document.createElement('button')
        button.classList.add("style")
        button.textContent = k
        button.id ="num" + k 
        row.appendChild(button) 
        k+=1
    }
    table.appendChild(row)
}
function addStyles(){
    document.getElementById("textStart").textContent = "";
    if (arr.length === 90){
        alert('Game over')
    }
    else{
    let randomNumber = Math.ceil(Math.random() * 90);
    for (let i=0;i<arr.length;i++){
        if (arr.includes(randomNumber)){
            randomNumber = Math.ceil(Math.random() * 90);
            i=0
        }
    }
    arr.push(randomNumber);
    let btnId = "num" + randomNumber;
    console.log(btnId);
    let re = document.getElementById(btnId) ;
    re.classList.add("btn-style")
    displayNum.textContent = randomNumber;
    displayNum.classList.add("circle");

}
} 
