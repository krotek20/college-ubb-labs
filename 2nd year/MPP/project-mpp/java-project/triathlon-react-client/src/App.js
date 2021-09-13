import React, { useState, useEffect } from 'react';
import './App.css';
import "bootstrap/dist/css/bootstrap.min.css";
import TriathlonTable from './TriathlonTable'
import TriathlonForm from './TriathlonForm'
import {GetReferees, AddReferee, UpdateReferee, DeleteReferee} from './utils/rest-calls'

export default function App() {
    const [referees, setReferees] = useState([])

    const addFunction = (referee) => {
        AddReferee(referee)
            .then(res => GetReferees())
            .then(referees => setReferees(referees))
            .catch(erorr => console.log('eroare add ', erorr));
    }

    const deleteFunction = (id) => {
        DeleteReferee(id)
            .then(res => GetReferees())
            .then(referees => setReferees(referees))
            .catch(error => console.log('Eroare delete ', error));
    }

    const updateFunction = (referee, id) => {
        UpdateReferee(referee, id)
            .then(res => GetReferees())
            .then(referees => setReferees(referees))
            .catch(error => console.log('Eroare delete ', error));
    }

    useEffect(() => {
        GetReferees().then(referees => setReferees(referees));
    }, []);

    return (
        <div className="App container">
            <TriathlonForm addFunction={addFunction} updateFunction={updateFunction}/>
            <br/>
            <TriathlonTable referees={referees} deleteFunction={deleteFunction}/>
        </div>
    );
}
