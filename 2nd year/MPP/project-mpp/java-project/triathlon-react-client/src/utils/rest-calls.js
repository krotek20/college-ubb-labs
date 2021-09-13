import {TRIATHLON_REFEREES_BASE_URL} from './consts';

function status(response) {
    console.log('response status ' + response.status);
    if (response.status >= 200 && response.status < 300) {
        return Promise.resolve(response)
    } else {
        return Promise.reject(new Error(response.statusText))
    }
}

function json(response) {
    return response.json()
}

export function GetReferees() {
    console.log('Before ' + TRIATHLON_REFEREES_BASE_URL + ' FETCH')

    const headers = new Headers();
    headers.append('Accept', 'application/json');

    const myInit = { method: 'GET',
        headers: headers,
        mode: 'cors'};
    const request = new Request(TRIATHLON_REFEREES_BASE_URL, myInit);

    return fetch(request)
        .then(status)
        .then(json)
        .then(data => {
            console.log('Request succeeded with JSON response', data);
            return data;
        }).catch(error=>{
            console.log('Request failed', error);
            return error;
        });
}

export function AddReferee(referee) {
    console.log('Before POST FETCH' + JSON.stringify(referee));

    const myHeaders = new Headers();
    myHeaders.append("Accept", "application/json");
    myHeaders.append("Content-Type", "application/json");

    const antet = { method: 'POST',
        headers: myHeaders,
        mode: 'cors',
        body:JSON.stringify(referee)};

    return fetch(TRIATHLON_REFEREES_BASE_URL, antet)
        .then(status)
        .then(response=>{
            console.log('Add status ' + response.status);
            return response.text();
        }).catch(error=>{
            console.log('Request failed', error);
            return Promise.reject(error);
        });
}

export function UpdateReferee(updatedReferee, id) {
    console.log('Before PUT FETCH' + JSON.stringify(updatedReferee));

    const myHeaders = new Headers();
    myHeaders.append("Accept", "application/json");
    myHeaders.append("Content-Type", "application/json");

    const antet = { method: 'PUT',
            headers: myHeaders,
            mode: 'cors',
            body:JSON.stringify(updatedReferee)};

    return fetch(TRIATHLON_REFEREES_BASE_URL + '/' + id, antet)
            .then(status)
            .then(response=>{
                console.log('Update status ' + response.status);
                return response.text();
            }).catch(error=>{
                console.log('Request failed', error);
                return Promise.reject(error);
            });
}

export function DeleteReferee(id) {
    console.log('Before delete FETCH')
    const myHeaders = new Headers();
    myHeaders.append("Accept", "application/json");

    const antet = { method: 'DELETE',
        headers: myHeaders,
        mode: 'cors'};

    return fetch(TRIATHLON_REFEREES_BASE_URL + '/' + id, antet)
        .then(status)
        .then(response=>{
            console.log('Delete status ' + response.status);
            return response.text();
        }).catch(e=>{
            console.log('error '+e);
            return Promise.reject(e);
        });
}