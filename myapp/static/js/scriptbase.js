
//menu resp in mobile
let buttonResp=document.getElementById('buttonresp')
let listResp=document.getElementById('listresp')
buttonResp.addEventListener('click', ()=>{
    if(listResp.style.display='none'){
       listResp.style.display='flex'; 
    }else{
        listResp.style.display='none'
    }

})

//information of user
let activeProfile=document.getElementById("profile_link");
let contProfile=document.getElementById("profile_container");
let closeProfile=document.getElementById("butt_close");
activeProfile.addEventListener('click', (event)=>{
    event.preventDefault()
    contProfile.style.opacity="1";
    contProfile.style.display="block";
    contProfile.style.animation="profileAnim 0.5s forwards ease"
});
closeProfile.addEventListener('click', ()=>{
    if(contProfile.style.opacity==="1" && contProfile.style.display==="block"){
        contProfile.style.opacity="0";
        contProfile.style.display="none";
        contProfile.style.animation=false;
    }
})