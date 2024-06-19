document.getElementById('menu-btn').addEventListener('click', () => {
    console.log('Button clicked')
    var menu = document.getElementById('menu')
    menu.classList.toggle('hidden')
})

console.log("Hello")