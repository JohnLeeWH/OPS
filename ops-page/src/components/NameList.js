import React from 'react'
import Person from './Person';

function NameList() {
    const persons = [
        {
            id: 1,
            name: "John",
            age: 11,
            skill: "react",
        },
        {
            id: 2,
            name: "Bob",
            age: 12,
            skill: "js",
        },
        {
            id: 3,
            name: "Peter",
            age: 13,
            skill: "python",
        },
    ]
    const personList = persons.map((person) => (
        <Person key={person.id} person={person} />
    ));
    return (
        <div>
            {personList}
        </div>
    );
}

export default NameList;