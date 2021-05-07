const abinet_control=document.getElementById('abinet_btn')

const table_1=document.getElementById('table_1')
const table_2=document.getElementById('table_2')
const table_3=document.getElementById('table_3')


const address_shower_btn=document.getElementById("address_shower_btn")
const sene_melekot_btn=document.getElementById('sene_melekot_btn')
const abinet_btn=document.getElementById('abinet_btn')



address_shower_btn.addEventListener("click",function(){ermias_2(table_1)})




sene_melekot_btn.addEventListener('click',function(){ermias_2(table_2)})

abinet_btn.addEventListener('click',function(){ermias_2(table_3)})






function ermias_2(makeitrl){
    
    makeitrl.style.pointerEvents="auto";
    makeitrl.style.opacity=1;
    console.log("ckeck it")
    makeitrl.style.backgroundcolor=" rgb(234, 245, 86)"

    // background-color: rgb(234, 245, 86);
   
  


}