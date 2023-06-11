import React, { useState, useEffect } from 'react';
import axios from 'axios';


function ApiList() {
    const [relations, setRelations] = useState([]);
    const [searchTerm, setSearchTerm] = useState('');

    useEffect(() => {
        axios.get(`/api/relations?sefaria_link=${searchTerm}`)
            .then(response => setRelations(response.data.relations));
    }, [searchTerm]);

    function handleSearchChange(event) {
        setSearchTerm(event.target.value);
    }

    return (
        <div>
        <h1>API List</h1>
        <label>
        Search relations with seferelation api (by @ykaner):
        <input type="text" value={searchTerm} onChange={handleSearchChange} />
        </label>
        <ul>
        {relations.map(item => (
            <li key={item[0]}>{item[1]}: {item[0]}</li>
        ))}
        </ul>
        </div>
    );
}

export default ApiList;

