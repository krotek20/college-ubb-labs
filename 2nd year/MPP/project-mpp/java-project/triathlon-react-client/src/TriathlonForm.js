import React, { useState } from 'react';

export default function TriathlonForm(props) {
    const [id, setId] = useState('')
    const [name, setName] = useState('')
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [gameId, setGameId] = useState('')

	const handleSave = (e) => {
		const referee = {
			id: id,
			name: name,
			username: username,
			password: password,
			game: {
			    id: gameId
			}
		}
		props.addFunction(referee);
		e.preventDefault();
	}

	const handleUpdate = (e) => {
	    const referee = {
	        id: id,
	        name: name,
	        username: username,
	        password: password,
	        game: {
	            id: gameId
	        }
	    }
	    props.updateFunction(referee, referee.id);
	    e.preventDefault();
	}

    return (
        <form className="container">
    	    <label>
    		    ID:
    			<input className="form-control" type="text" value={id} onChange={e => setId(e.target.value)} />
    		</label>
    		<br/>
    		<label>
    		    NAME:
    			<input className="form-control" type="text" value={name} onChange={e => setName(e.target.value)} />
    		</label>
    		<br/>
    		<label>
    			USERNAME:
    			<input className="form-control" type="text" value={username} onChange={e => setUsername(e.target.value)} />
    		</label>
    		<br/>
            <label>
    			PASSWORD:
    			<input className="form-control" type="password" value={password} onChange={e => setPassword(e.target.value)} />
    		</label>
    		<br/>
            <label>
    			GAME ID:
    			<input className="form-control" type="text" value={gameId} onChange={e => setGameId(e.target.value)} />
    		</label>
    		<br/>
    		<div className="btn-group-justified">
                <input className="btn btn-primary" type="submit" value="Save" onClick={handleSave} />
                <input className="btn btn-info" type="submit" value="Update" onClick={handleUpdate} />
    		</div>
    	</form>
    );
}