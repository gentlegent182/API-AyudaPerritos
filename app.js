console.log('funcionando')
const formulario = document.querySelector('#formulario')

formulario.addEventListener('submit',(e)=>{
    console.log('me diste click')
    e.preventDefault()
})
