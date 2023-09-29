function fire(msg) {
    if (document.getElementById('my-alert')) return
    const div = document.createElement('div')
    div.setAttribute('id', 'my-alert')
    div.setAttribute('style', 'position: fixed; min-width: 300px; max-width: 500px; top:50%; left:50%;transform: translate(-50%, -50%);background-color: #323232; color: #eee;border: 2px solid #eee; border-radius: 10px;z-index: 10000; text-align: center; padding: 20px; user-select: none; cursor: pointer;')
    div.innerHTML = msg + '<br> <br>'
    const button = document.createElement('button')
    button.innerHTML = 'OK'
    button.setAttribute('class', 'player-but')

    button.addEventListener('click', () => {
        document.querySelector('body').removeChild(div)
    })
    div.appendChild(button)
    document.querySelector('body').appendChild(div)
}