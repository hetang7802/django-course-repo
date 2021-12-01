//Reset Game button
var restart=document.querySelector("#b")

//get all the squares
var squares=document.querySelectorAll("td")

//clear all the squares
function clearBoard(){
  // console.log("inside for loop");
  for(var i=0;i<squares.length;i++){
    squares[i].textContent='';
  }
}

restart.addEventListener('click',clearBoard);


//change the square marker
function changeMarker(){
  if(this.textContent===''){
    this.textContent='X';
  }else if(this.textContent==='X'){
    this.textContent='O'
  }else{
    this.textContent=''
  }
}

for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener('click',changeMarker)
}
