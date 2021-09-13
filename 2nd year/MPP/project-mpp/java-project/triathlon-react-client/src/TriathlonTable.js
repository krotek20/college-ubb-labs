import React from 'react';

function TriathlonRow({referee, deleteFunction}) {
    return (
        <tr>
            <td> {referee.id} </td>
            <td> {referee.name} </td>
            <td>
                <button className="btn btn-danger" onClick={() => deleteFunction(referee.id)}>
                    Delete
                </button>
            </td>
        </tr>
    );
}

export default function TriathlonTable({referees, deleteFunction}) {
console.log("referees2: ", referees)
    return (
        <div className="container">
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th>ID</th>
        				<th>NAME</th>
        				<th>#</th>
        			</tr>
        		</thead>
        		<tbody>
        		    {referees.map(referee => {
        		        return (
        		            <TriathlonRow
        		                referee = {referee}
        		                deleteFunction = {deleteFunction}
        		            />
        		        )
        		    })}
        		</tbody>
        	</table>
        </div>
    );
}