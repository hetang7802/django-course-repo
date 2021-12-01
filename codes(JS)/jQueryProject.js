var playerOneColor='red'
var playerTwoColor='blue'

function promptForName(player){
  var name=""
  while(name==""){
    name=prompt(player+" enter your name ");
  }
  return name
}

var player1=promptForName("player1")
var player2=promptForName("player2")

var game_on=true;
var cells=$('button')
var table=$('table tr')

function reportWin(rowNum,colNum) {
  console.log("You won starting at this row,col");
  console.log(rowNum);
  console.log(colNum);
  game_on=false;
}

function findColor(rowIndex,colIndex){
  return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color')
}

//to find the bottom of the column
function checkBottom(colIndex){
  var colorReport=findColor(5,colIndex)
  for(var row=5;row>=0;row--){
    colorReport=findColor(row,colIndex)
    if(colorReport==='rgb(128, 128, 128)'){
      return row
    }
  }
}

function colorMatchCheck(one, two, three, four) {
	return (one === two & one === three & one === four & one !== 'rgb(128, 128, 128)' & one !== undefined)
}

// Check for Horizontal Wins
function horizontalWinCheck() {
  for (var row = 0; row < 6; row++) {
    for (var col = 0; col < 4; col++) {
      if (colorMatchCheck(findColor(row,col), findColor(row,col+1) ,findColor(row,col+2), findColor(row,col+3))) {
        console.log('horiz');
        reportWin(row,col);
        return true;
      }else {
        continue;
      }
    }
  }
}

// Check for Vertical Wins
function verticalWinCheck() {
  for (var col = 0; col < 7; col++) {
    for (var row = 0; row < 3; row++) {
      if (colorMatchCheck(findColor(row,col), findColor(row+1,col) ,findColor(row+2,col), findColor(row+3,col))) {
        console.log('vertical');
        reportWin(row,col);
        return true;
      }else {
        continue;
      }
    }
  }
}

// Check for Diagonal Wins
function diagonalWinCheck() {
  for (var col = 0; col < 5; col++) {
    for (var row = 0; row < 7; row++) {
      if (colorMatchCheck(findColor(row,col), findColor(row+1,col+1) ,findColor(row+2,col+2), findColor(row+3,col+3))) {
        console.log('diag');
        reportWin(row,col);
        return true;
      }else if (colorMatchCheck(findColor(row,col), findColor(row-1,col+1) ,findColor(row-2,col+2), findColor(row-3,col+3))) {
        console.log('diag');
        reportWin(row,col);
        return true;
      }else {
        continue;
      }
    }
  }
}

function changeColor(rowIndex, colIndex, color) {
	return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color', color);
}

var currentPlayer=1;
var currentName=player1;
var currentColor=playerOneColor;

$('p').text(player1 + " its your turn, pick a column")


  cells.click(function(){
    if(game_on){
      var column=$(this).closest("td").index();

      var row=checkBottom(column)


      changeColor(row,column,currentColor)

      // Check win or tie
    	if (horizontalWinCheck() || verticalWinCheck() || diagonalWinCheck()) {
    		$('h1').text(currentName + " You have won!")
        $('p').fadeOut('fast');
    		$('h2').fadeOut('fast');
    	}

      // Switch the player
    	currentPlayer = currentPlayer * -1

    	if (currentPlayer === 1) {
    		currentName = player1;
    		$('p').text(currentName + " it is your turn, please pick a column to drop your blue chip.")
    		currentColor = playerOneColor;
    	} else {
    		currentName = player2;
    		$('p').text(currentName + " it is your turn, please pick a column to drop your red chip.")
    		currentColor = playerTwoColor;
    	}
    }

  })
