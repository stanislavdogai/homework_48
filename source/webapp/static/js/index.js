async function makeRequest(url, method) {
    let response = await fetch(url, method);
    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        error.response = response;
        err_response = await response.json()
        return err_response
    }
}

let addBasket = async function(event){
    let url = event.target.dataset.addBasketUrl
    let id = event.target.dataset.productId
    let count = document.getElementById(`count${id}`).value
    if (!count){
        console.log('IF')
        count = 1
    }
    let info = {
        'amount' : count
    }
    console.log(count)
    let data = await makeRequest(url, {
            method: 'POST',
            body: JSON.stringify(info),
            headers: {
                'Content-Type': 'application/json',
                'Authorization' : 'Token 796081efd707eb3f023212a6ba66a1e3ba4555a8'
            }
        }
    )
    // console.log('data', data)
    let inputs = document.querySelectorAll('input[type=text]');
    for (let i = 0;  i < inputs.length; i++) {
    inputs[i].value = '';
    };
}





// let token = async function () {
//     let log = {
//         'username': 'admin',
//         'password': 'admin',
//     }
//     let url = 'http://localhost:8000/api/login'
//     let data = await makeRequest(url, {
//         method: 'POST',
//         body: JSON.stringify(log),
//         headers: {
//             'Content-Type': 'application/json',
//         }
//     })
//     console.log(data)
// }
//
// token()

