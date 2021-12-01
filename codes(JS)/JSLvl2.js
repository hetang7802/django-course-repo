//FUNCTIONS
// syntax:
// function name(par1,par2){
//   //code
//   return something
// }


// ARRAYS
// arrays can contain multiple datatypes unlike c++
// we can push/pop in array just like a stack in c++
// myArr.length->returns the length of array
// iteration: (forof loop)
// for(element of arr){
//   code
// }
//use the splice function to delete the any particular element from the array
//example arr.splice(index,1)
// forEach loop:
// example: arr.forEach(alert)//remember to not use alert() and use alert
// for parsing string at a particular character use the function split of JS


// var arr=[]
// while(1){
//   var code=prompt("enter the code")
//   if(code==="add"){
//     var value=prompt("enter the value to add")
//     arr.push(value);
//   }else if(code==="remove"){
//     var value=prompt("enter the vale to delete")
//     var index=arr.indexOf(value)
//     if(index>-1){
//       arr.splice(index,1)
//     }
//   }else if(code==="display"){
//     console.log(arr)
//   }else if(code=="quit"){
//     break;
//   }else{
//     console.log("unrecognized input")
//   }
// }


// OBJECTS(similar to map/struct in c++)

//declaration example: var carInfo={make:"Toyota",year:1990,model:"camry"}
//to find the value for certain key carInfo['make'] (not the single quotes)
//to change value for certain key: carInfo['year']=2006
//console.dir(objectName) will display the whole object if it is not visible without using it
// access using forin loop
//for (var k in carInfo) {
//   console.log(k);  //this will give the name of key
//   console.log(carInfo[k]); //this will give the value corresponding to key k
// }
// METHODS in OBJECTS
// example:
// var myObj={
//   prop: 37,
//   reportProp: function(){
//     return this.prop;
//   }
// };
// console.log(myObj.reportProp());
