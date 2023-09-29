const EQ_LINK = '/integrate'

function getLeft() {
    return document.getElementById('left').value
}

function getRight() {
    return document.getElementById('right').value
}

function getEps() {
    return document.getElementById('eps').value
}

function getEquation() {
    try {
        return parseInt(document.querySelectorAll('input[name="eq"]:checked')[0].value)
    } catch(ex) {
        fire('Выберите уравнение')
        return false
    }
}

function getMethod() {
    try {
        return parseInt(document.querySelectorAll('input[name="mth"]:checked')[0].value)
    } catch(ex) {
        fire('Выберите метод')
        return false
    }
}
