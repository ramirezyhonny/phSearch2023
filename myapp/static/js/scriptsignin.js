//efect to visivility password User
let eyeButtonOp=document.getElementById('togglePassword');
let inpPassword=document.getElementById('id_password');
//efect mousedown canceled
let isMouseDown = false;
eyeButtonOp.addEventListener('mousedown', function () {
    //active
    isMouseDown = true;
    togglePasswordVisibility();
  });
  //cancel in mouseup
  document.addEventListener('mouseup', function revertVisibility() {
    if (inpPassword.type === 'text') {
      inpPassword.type = 'password';
    }
    document.removeEventListener('mouseup', revertVisibility);
  });
  // Detener el cambio cuando se suelta el clic
function togglePasswordVisibility() {
    if(isMouseDown){
        if(inpPassword.type==='password'){
            inpPassword.type='text';
        } else{
            inpPassword.type='password'
        }
    }
  }