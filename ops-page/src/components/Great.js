import React from "react";

//function Great() {
//    return <h1>Hello 2</h1>;
//}

const Great = (props) => {
    console.log(props);
    return (
        <div>
            <h1>Hello {props.name} aka {props.nickName}</h1>
            <div>{props.children}</div>
        </div>);
};

export default Great;