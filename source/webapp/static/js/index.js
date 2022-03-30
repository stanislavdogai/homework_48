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

console.log('JS')