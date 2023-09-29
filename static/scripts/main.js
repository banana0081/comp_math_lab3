async function requestEquation(event) {
    event.preventDefault()
    const method = getMethod(),
        equation = getEquation(),
        left = isFloat(getLeft()),
        right = isFloat(getRight()),
        eps = isFloat(getEps())

    if (equation === false || method === false) return
    if (left === false || right === false || eps === false) {fire('Входные данные должны содержать числа');return}
    if (left >= right) {fire('Правый край должен быть больше левого');return}

    const resp =  await recieveData(await requestData(EQ_LINK, {method, equation, left, right, eps}), extractJSON)

    if (resp === false) return
    console.log(resp)

    fire('Значение интеграла - ' + resp.answer + ', найдено за ' + resp.itr + ' итераций')
}

document.getElementById('submit_eq').addEventListener('click', (event) => {requestEquation(event)})